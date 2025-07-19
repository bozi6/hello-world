import sys
from PIL import Image

for infile in sys.argv[1:]:
	try:
		with Image.open(infile) as im:
			print(f"filename: {infile}\nformat: {im.format}\nsize: {im.size[0]}x{im.size[1]} \nmode: {im.mode}")
	except OSError:
		pass
