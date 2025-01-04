#  read.py Copyright (C) 2024  Konta Boáz
#      This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
#      This is free software, and you are welcome to redistribute it
#      under certain conditions; type `show c' for details.
#   Last Modified: 2024. 12. 31. 20:46
import struct

f = open('/Users/mnte/Desktop/2B3A0EE3A80F.cky', 'rb')
content = f.read()
print(content)
# ints = struct.unpack('IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIiIIiI', content[:255])
# ints = struct.unpack('cccccccccccccccccccc', content[:20])
ints = struct.unpack('<h62I', content[:250])
print(ints)
i = 1
for egesz in ints:
    print(i, egesz)
    i = i + 1
f.close()
