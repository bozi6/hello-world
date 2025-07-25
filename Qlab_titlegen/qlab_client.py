import socket
import json
import threading
from oscpy.client import OSCClient


class Listener:
    """
    Setup a server for listening to QLab /reply messages

    """

    def __init__(self, address, port):
        # print("Starting listener")
        self.address = address
        self.port = port
        self.sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
        self.sock.bind((self.address, self.port))
        self.last_message = None

    def _get_message(self):
        data, address = self.sock.recvfrom(8192)
        raw = data.decode("utf8")
        parts = list(filter(bool, raw.split("\x00")))
        json_message = parts[2]
        try:
            self.last_message = json.loads(json_message)
        except json.decoder.JSONDecodeError as e:
            print("Error. server raw response:", repr(raw))
            print("parts", parts)
            print(e)
            self.last_message = None

    def get_message(self):
        """
        Get a OSC message from OSC server

        :return: message from OSC server
        :rtype: str

        """
        t = threading.Thread(target=self._get_message, daemon=True)
        t.start()
        t.join(timeout=0.1)
        return self.last_message


class Interface:
    """
    Interface for QLab
    """

    def __init__(self):
        """
        Create a client connection to QLab
        """
        self.client = OSCClient("127.0.0.1", 53000, encoding="utf8")
        self.server = Listener("127.0.0.1", 53001)
        self.wpid = self.get_wpid()
        self.encoding = "utf8"
        # print("WPID: {}".format(self.wpid))

    def get_wpid(self):
        """
        Get a Workspace ID from QLab

        :return: workspace ID from QLab

        """
        self.client.send_message(b"/workspaces", [])
        response = self.server.get_message()
        if response:
            return response.get("data")[0]["uniqueID"]
        else:
            return None

    def get_uniqid(self):
        """
        Try to get an unique id of main que list

        :return:  Unique id of first cuelist

        """
        self.client.send_message(b"/cueLists/uniqueID", [])
        response = self.server.get_message()
        if response:
            return response.get("workspace_id")
        else:
            return None

    def bundi(self, messages):
        self.client.send_bundle(messages)

    def set_cue_prop(self, cue_no, name, value):
        """
        Set a cue parameters in QLab

        :param cue_no: cue number, also accept selected
        :param name: changeable parameter name eg.: name
        :param value: parameter value eg.: 120
        :return: return any response from QLab

        """
        self.client.send_message("/cue/{cue_no}/{name}".format(**locals()), value)
        """response = self.server.get_message()
        if response:
            return response.get('data')
        """

    def newcue(self, mit="memo"):
        """
        Create new cue in QLab when no parameter default to memo

        in QLab 4: Supported strings include:
        audio, mic, video, camera, text, light,
        fade, network, midi, midi file,
        timecode, group, start, stop, pause,
        load, reset, devamp, goto, target, arm,
        disarm, wait, memo, script, list, cuelist,
        cue list, cart, cuecart, or cue cart.

        :param mit: type of newly created cue
        :return: nothing

        """
        wpid = self.wpid
        try:
            self.client.send_message("/workspace/{}/new".format(wpid), [mit])
        except Exception as e:
            print(f"Error sending message to QLab: {e}")

    def select_all_cues(self):
        """
        Try to select all cues in current workspace

        :return: Null

        """
        wpid = self.wpid
        uniqid = self.get_uniqid()
        self.client.send_message("/workspace/{}/select/*".format(wpid), [])

    def renumber(self, start, step):
        """
        Try to renumber cues

        :param start: new starting number
        :param step: steps through unmbers
        :return: nothing

        """
        wpid = self.wpid
        self.select_all_cues()
        self.client.send_message("/workspace/{}/renumber".format(wpid), [start, step])

    def getques(self):
        """
        Receive quelists information

        :return: cue list

        """
        wpid = self.wpid
        # self.client.send_message("/workspace/{}/cueLists".format(wpid), "")
        self.client.send_message(f"/workspace/{wpid}/cueLists", "")
        response = self.server.get_message()
        if response:
            return response.get("data")