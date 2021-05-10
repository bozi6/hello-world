import json
import socket
from pythonosc import osc_message_builder
from pythonosc import udp_client
import threading


class Listener:
    def __init__(self):
        print('starting listener')
        self.sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
        # Sometime it works only if set socket.AF_INET to socket.AF_INET6

        self.sock.bind(('::1', 53001))
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
        self.client = udp_client.UDPClient('::1', 53000)

    def send_message(self, address, value=None, val2=None, val3=None):
        msg = osc_message_builder.OscMessageBuilder(address=address)
        #  print('sent addr: {} - send__messageból_value: {}'.format(address,value))
        if value:
            msg.add_arg(value)
        if val2:
            msg.add_arg(val2)
        if val3:
            msg.add_arg(val3)
        self.client.send(msg.build())


class Interface:
    def __init__(self):
        self.server = Listener()
        self.client = Client()
        self.wpid = self.getwid()

    def getwid(self):
        """
        Returns actual workspace ID
        :return: Workspace ID
        """
        self.client.send_message('/workspaces')
        response = self.server.get_message()
        if response:
            return response['data'][0]['uniqueID']

    def newcue(self, cuetype):
        self.client.send_message('/new', cuetype)

    def get_cue_text(self, cue_no):
        """
        :param cue_no: a cue sorszáma
        :return: a cue text paraméterének visszaadása
        """
        return self.get_cue_property(cue_no, 'text')

    def get_cue_property(self, cue_no, name):
        """
        A cue tulajdonságainak visszaadása
        :param cue_no: a cue sorszáma
        :param name: a kérdéses paraméter
        :return: a válasz adat
        """
        self.client.send_message('/cue/{cue_no}/{name}'.format(**locals()))
        response = self.server.get_message()
        if response:
            return response.get('data')

    def movecue(self, cueid, gid, index=1):
        """ a cueid a mozgatandó cue id-je
        az index az hova kerüljön az új helyen
        a gid meg az amelyik csoportba akarod id-je
        /workspace/{id}/move/{cue_id} {new_index} {new_parent_cue_id}
        """
        wpid = self.wpid
        self.client.send_message("/workspace/{}/move/{}".format(wpid, cueid), index, gid)

    def get_surfaces(self):
        self.client.send_message('/settings/video/surfaces')
        response = self.server.get_message()
        if response:
            return response.get('data')

    def get_cue_id(self, cue_no='selected'):
        """
        :param cue_no: a cue sorszáma, alapból a kiválasztott
        :return: az egyedi azonsító
        """
        self.get_cue_property(cue_no, 'uniqueID')
        response = self.server.get_message()
        if response:
            return response.get('data')

    def set_cue_property(self, cue_no, name, value):
        self.client.send_message('/cue/{cue_no}/{name}'.format(**locals()), value=value)
        # response = self.server.get_message()
        # if response:
        #    print(response.get('data'))


def main():
    # example script using the interface to
    # run through cues one by one and print
    # any titles' cue numbers and text
    interface = Interface()
    interface.client.send_message('/select/1')


if __name__ == '__main__':
    main()
