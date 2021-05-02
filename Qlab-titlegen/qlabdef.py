# import asyncio
import json
import socket
from pythonosc import osc_message_builder
from pythonosc import udp_client

import threading


class Listener:
    def __init__(self):
        print('starting listener')
        self.sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
        # Valamiért ezt kellett INET6-ra állítani AF_INET-ről

        self.sock.bind(('localhost', 53001))
        self.last_message = None

    def _get_message(self):
        data, address = self.sock.recvfrom(8192)
        raw = data.decode('utf8')
        parts = list(filter(bool, raw.split('\x00')))
        #  print(parts)
        json_message = parts[2]
        try:
            self.last_message = json.loads(json_message)
        except json.decoder.JSONDecodeError as e:
            print('Error. server raw response:', repr(raw))
            print('parts', parts)
            print(e)
            self.last_message = None

    def get_message(self):
        t = threading.Thread(target=self._get_message, daemon=True)
        t.start()
        t.join(timeout=0.3)
        return self.last_message


class Client:
    def __init__(self):
        self.client = udp_client.UDPClient('localhost', 53000)

    def send_message(self, address, value=None):
        msg = osc_message_builder.OscMessageBuilder(address=address)
        if value:
            msg.add_arg(value)
        self.client.send(msg.build())


class Interface:
    def __init__(self):
        self.server = Listener()
        self.client = Client()

    def newcue(self, cuetype):
        self.client.send_message('/new', cuetype)
        return self.get_cue_id()

    def get_cue_text(self, cue_no):
        return self.get_cue_property(cue_no, 'text')

    def get_cue_property(self, cue_no, name):
        self.client.send_message('/cue/{cue_no}/{name}'.format(**locals()))
        response = self.server.get_message()
        if response:
            return response.get('data')

    def movecue(self, cueid, gid, index=1):
        """ a cueid a mozgatandó cue id-je
        az index az hova kerüljön az új helyen
        a gid meg az amelyik csoportba akarod id-je"""
        self.client.send_message('/move/{cueid} {index} "{gid}"'.format(**locals()))

    def get_cue_id(self, cue_no='selected'):
        return self.get_cue_property(cue_no, 'uniqueID')

    def set_cue_property(self, cue_no, name, value):
        self.client.send_message('/cue/{cue_no}/{name}'.format(**locals()), value=value)

    def select_next_cue(self):
        old = self.get_cue_property('selected', 'number')
        self.client.send_message('/select/next')
        cue_no = self.get_cue_property('selected', 'number')
        while cue_no == old:
            cue_no = self.get_cue_property('selected', 'number')
        return cue_no


def main():
    # example script using the interface to
    # run through cues one by one and print
    # any titles' cue numbers and text
    interface = Interface()
    interface.client.send_message('/select/1')
    while True:
        caption_type = interface.get_cue_property('selected', 'type')
        #  print("elfogott típus: {}".format(caption_type))
        if caption_type == 'Text':
            text = interface.get_cue_text('selected')
            cue_no = interface.get_cue_property('selected', 'number')
            print(cue_no, text)
            if text.lower().strip() == 'the end':
                break
        print()
        if caption_type == 'Group':
            cue_no = interface.get_cue_property('selected', 'number')
            gid = interface.get_cue_id('selected')
            print("Típus: {}, Cue sorszám: {} - azonosító: {}".format(caption_type, cue_no, gid))
        interface.select_next_cue()


if __name__ == '__main__':
    main()
