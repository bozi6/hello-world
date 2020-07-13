import os

# The installed gobos picture folder
src_dir = "C:/ProgramData/MA Lighting Technologies/grandma/gma2_V_3.9/gobos"
# The generated filename. Default into gobo folder
genfile = open(src_dir + "./generated.csv", "w")
idx = len(src_dir)+1
genfile.write('sorszam,utvonal,kep;\n')
i=1
for r, d, f in os.walk(src_dir):
    for file in f:
        if ".png" in file or ".bmp" in file:
            filename = os.path.join(r, file)
            genfile.write('{},{},{};\n'.format(i,r[idx:], file))
            i += 1
genfile.close()
