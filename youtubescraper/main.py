#  main.py Copyright (C) 2024  Konta Boáz
#      This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
#      This is free software, and you are welcome to redistribute it
#      under certain conditions; type `show c' for details.
#   Last Modified: 2024. 12. 04. 16:01

import scrapetube

# videos = scrapetube.get_channel("UCCezIgC97PvUuR4_gbFUs5g")
videos = scrapetube.get_channel("UC5WB1KlV0Vnw1D0rcfgCbvg")

for video in videos:
    # print(video['videoId'])
    print("https://www.youtube.com/watch?v=" + str(video['videoId']))
