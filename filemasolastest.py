import os
import sys
import shutil
import time

source = r'z:\boz\progz\Adobe.Photoshop.CC.2018.v19.1.6.HUN.x86-x64-D.G\d.g-ad.ps.2018.v19.1.6.iso'
target = r'c:\temp\fotoshopp.iso'

# assert not os.path.isabs(source)
# target = os.path.join(target, os.path.dirname(source))
print(target)
# create the folders if not already exists
# os.makedirs(target)

# hibakezelés
try:
    k = time.time()
    shutil.copy(source, target)
except IOError as e:
    print("Nem lehet másolni a fájlt. %s" %e)
except:
    print("Nem várt hiba történt:", sys.exc_info())

print("Időben: ", time.time()-k)
