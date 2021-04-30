import argparse

from pythonosc import osc_message_builder
from pythonosc import udp_client


def send_msg(client, address, *args):
    msg = osc_message_builder.OscMessageBuilder(address=address)
    for arg in args:
        msg.add_arg(arg)
    client.send(msg.build())


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--server', default='127.0.0.1', help='Az OSC szerver IP címe')
    parser.add_argument('--passcode', type=str, default=None, help='A jelszó a QLabhoz való csatlakozáshoz')
    # parser.add_argument('file', nargs='?', help='A beolvasni kívánt fájl neve')
    args = parser.parse_args()

    client = udp_client.UDPClient(args.server, 53000)

    if args.passcode is not None:
        send_msg(client, '/connect', args.passcode)
    else:
        send_msg(client, '/connect')

    # file = open(args.file)
    try:
        file = open("./example-input.txt")
    except IOError:
        print("Nem található a fájl.")
    # A lényeg, hogy előbb jönnek a fade cuek, amik eltüntetik az előző szöveget.
    # és csak aztán jelenik meg az újabb szöveg.
    last_cue = 100  # az újonnan kezdődő cue-k száma
    last_blank = True  # utolsó sor üres volt-e?
    last_titles_was_decimal = False
    """
    Ide akaorm a groupokat beszúrni, de nem akaraj az új que-t belecsinálni.
    
    """
    send_msg(client, '/new', 'group')
    send_msg(client, '/cue/selected/number', str(last_cue))
    send_msg(client, '/cue/'+str(last_cue)+'/mode', 1)

    for line in file.readlines():  # sorok beolvasása
        line = line[:-1]
        this_cue = last_cue + 1  # Kezdőérték + 1
        this_blank = line == '.'
        broken_line = line.replace('/', '\n')
        if not last_blank:  # A fade cuek beállításai
            send_msg(client, '/new', 'fade')
            send_msg(client, '/cue/selected/stopTargetWhenDone', 1)
            send_msg(client, '/cue/selected/duration', 0.5)
            send_msg(client, '/cue/selected/doOpacity', 1)
            send_msg(client, '/cue/selected/opacity', 0)
            send_msg(client, '/cue/selected/number', str(this_cue))
            send_msg(client, '/cue/selected/cueTargetNumber',
                     str(last_cue) + '.1' if last_titles_was_decimal else str(last_cue))
            send_msg(client, '/cue/selected/name', 'ÜRES' if this_blank else str(last_cue)+' FO')
            if not this_blank:
                send_msg(client, '/cue/selected/continueMode', 2)
        if not this_blank:
            send_msg(client, '/new', 'text')
            send_msg(client, '/cue/selected/number', str(this_cue) + '.1' if not last_blank else str(this_cue))
            send_msg(client, '/cue/selected/text/format/fontSize', 64)
            send_msg(client, '/cue/selected/colorName', "green")
            send_msg(client, '/cue/selected/text', broken_line)
            # send_msg(client, '/cue/selected/name', line if last_blank else '--')
            send_msg(client, '/cue/selected/name', line)
        last_cue = this_cue
        last_titles_was_decimal = not last_blank
        last_blank = this_blank

    send_msg(client, '/disconnect')


if __name__ == '__main__':
    main()
