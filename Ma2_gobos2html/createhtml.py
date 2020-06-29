import os

# The installed gobos picture folder
src_dir = "C:\ProgramData\MA Lighting Technologies\grandma\gma2_V_3.9\gobos"
# The generated filename. Default into gobo folder
genfile = open(src_dir + "\generated.html", "w")

# Generate HTML Head and title
genfile.write("<!DOCTYPE html>\n<html>\n<head>><title>Gobók listaja</title></head><body style=\"background-color:Black;\">\n")
# r = root
# d = directories
# f = files

i = 1
egysor = ""
for r, d, f in os.walk(src_dir):
    for file in f:
        if ".png" in file or ".bmp" in file:
            if i % 5 == 0:
                egysor = '<br>{}<img src="file:///{}" title="{}" width="128" height="128" style="border:3px solid blue">\n'.format(i, os.path.join(r, file), os.path.join(r, file))
            else:
                egysor = '{}<img src="file:///{}" title="{}" width="128" height="128" style="border:3px solid blue">\n'.format(i, os.path.join(r, file), os.path.join(r, file))
            i += 1
        genfile.write(egysor)

genfile.write("</body>\n</html>\n")
genfile.close()
