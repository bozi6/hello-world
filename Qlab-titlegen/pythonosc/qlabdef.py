from pyOSC3 import OSCClient, OSCMessage
import socket
import threading
import json


class Interface:
    def __init__(self):
        self.client = OSCClient()
        self.client.connect(('localhost', 53000))
        self.server = Listener()
        self.wpid = self.get_wpid()

    def set_cue_prop(self, cue_no, name, value):
        self.client.send(OSCMessage('/cue/{cue_no}/{name}'.format(**locals()), [value]))
        response = self.server.get_message()
        if response:
            return response.get('data')

    def get_wpid(self):
        self.client.send(OSCMessage('/workspaces'))
        response = self.server.get_message()
        if response:
            return response.get('data')[0]['uniqueID']

    def newcue(self, mit='memo'):
        wpid = self.wpid
        self.client.send(OSCMessage('/workspace/{}/new/{}'.format(wpid, mit)))


class Listener:
    def __init__(self):
        print('Starting listener')
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # Sometime it works only if set socket.AF_INET to socket.AF_INET6
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
