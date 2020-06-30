import os

from mako.template import Template

myTemplate = Template(filename='template.html', strict_undefined=True)

# The installed gobos picture folder
src_dir = "C:/ProgramData/MA Lighting Technologies/grandma/gma2_V_3.9/gobos"
# The generated filename. Default into gobo folder
genfile = open(src_dir + "./generated.html", "w")

i = 1
egysor = {1: {'sorszam': 0, 'filename': 'lófasz'}, }
for r, d, f in os.walk(src_dir):
    for file in f:
        if ".png" in file or ".bmp" in file:
            filename = os.path.join(r, file)
            egysor[i] = {'filename': filename}
            i += 1
genfile.write(myTemplate.render(rows=egysor, mappa=src_dir))
genfile.close()
