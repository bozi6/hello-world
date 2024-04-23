#  artnet_test.py Copyright (C) 2024  Konta Boáz
#      This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
#      This is free software, and you are welcome to redistribute it
#      under certain conditions; type `show c' for details.
#   Last Modified: 2024. 03. 26. 22:58
import asyncio

from pyartnet import ArtNetNode


async def main():
    # Run this code in your async function
    node = ArtNetNode("192.168.0.171", 6454)

    # Create universe 0
    universe = node.add_universe(0)

    # Add a channel to the universe which consist of 3 values
    # Default size of a value is 8bit (0..255) so this would fill
    # the DMX values 1..3 of the universe
    # A csatorna itt lehet akármekkora is.
    for i in range(1, 14, 2):
        channel = universe.add_channel(start=i, width=2)

    channel = universe["1/2"]  # alap elnevezés a start és a width értékekből
    # channel.set_values([64])  # érték megadása azonnal
    # channel = universe["1/1"]
    channel.add_fade([255, 255], 15000)  # fade megadása:
    # # a []-ban az értékek ha a width > 1 utána a fade idő ms-ben
    # channel = universe["3/1"]  # 3as cím kiválasztása
    # channel.add_fade([255], 1500)
    # channel = universe["4/1"]
    # channel.add_fade([64], 1500)
    # channel = universe["5/1"]
    # channel.add_fade([255], 1500)
    # channel = universe["10/1"]
    # channel.add_fade([255], 1500)
    # channel = universe["6/1"]
    # randint = random.randrange(0, 255)
    # channel.add_fade([randint], 3000)
    # print(randint)
    # # A width adja meg hány címet foglaljon el.

    # Fade channel to 255,0,0 in 5s
    # The fade will automatically run in the background
    # channel.add_fade([255, 0, 0], 1000)
    # channel = universe["1/4"]
    # channel.set_values([128, 0, 0, 0])
    # channel = universe.get_channel("1/4")

    # universe.add_channel(start=2, width=3, channel_name="Dimmer1")
    # channel = universe["Dimmer1"]
    # channel = universe.get_channel("Dimmer1")
    # channel.set_fade([64, 0, 128], 1000)
    # this can be used to wait till the fade is complete
    await channel
    for i in range(1, 14, 2):
        channel = universe.get_channel(f"{i}/1")
        print(f"{i} - {channel.get_values()}")


asyncio.run(main())
