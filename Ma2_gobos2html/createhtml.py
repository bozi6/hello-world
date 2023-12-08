import os
import sys
from mako.template import Template


if __name__ == "__main__":
    myTemplate = Template(filename="template.html", strict_undefined=True)

    # The installed gobos picture folder
    if sys.platform == "darwin":
        src_dir = os.path.expanduser(
            "~/MALightingTechnology/gma3_1.8.8/shared/lib_fixture_types/gobos/"
        )
    elif sys.platform == "nt":
        src_dir = "C:/ProgramData/MA Lighting Technologies/grandma/gma2_V_3.9.60/gobos/"

    print(src_dir)
    # The generated filename. Default into gobo folder
    genfile = src_dir + "generated.html"
    i = 1
    egysor = {
        1: {"sorszam": 0, "filename": "lófasz"},
    }
    with open(genfile, "w", encoding="utf-8") as f:
        for root, d, files in os.walk(src_dir):
            for file in files:
                if file.endswith((".png", ".bmp")):
                    filename = os.path.join(root, file)
                    egysor[i] = {"filename": filename}
                    i += 1
        f.write(myTemplate.render(rows=egysor, mappa=src_dir))
    f.close()
