import json
from pythonosc.dispatcher import Dispatcher
# Set up server and client for testing
from pythonosc.osc_server import BlockingOSCUDPServer
from pythonosc.udp_client import SimpleUDPClient

dispatcher = Dispatcher()

ip = "127.0.0.1"
port1 = 53000
port2 = 53001


def get_new_id(address, *args):
    arg = json.loads(*args)
    return arg["data"]


def default_handler(address, *args):
    print(f"DEFAULT {address}: {args}")


#  dispatcher.map("/reply*", set_filter)  # Map wildcard address to set_filter function
dispatcher.map("/reply/*", get_new_id)
dispatcher.set_default_handler(default_handler)


server = BlockingOSCUDPServer((ip, port2), dispatcher)
client = SimpleUDPClient(ip, port1)

# Send message and receive exactly one message (blocking)
client.send_message("/new", "group")
# /workspace/{id}/move/{cue_id} {new_index} {new_parent_cue_id}
server.handle_request()
client.send_message("/new", "text")
server.handle_request()
client.send_message("/move/"+txtid, 1)

