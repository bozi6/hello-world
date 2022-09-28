import main_cl as mc
import logging

__author__ = 'Konta Boáz'
__email__ = 'kontab6@gmail.com'
__version__ = '2.0'
__license__ = "MIT"
__copyright__ = "Copyright (c) 2022 Konta Boáz"
__title__ = 'from csv to MA3 xmls'
__description__ = "Ma3 classes to create xml to timecode and sequence"
__url__ = "https://github.com/bozi6/hello-world/tree/master/ma3_xmls_factory"
__uri__ = __url__
__doc__ = __description__ + " <" + __uri__ + ">"

if __name__ == "__main__":
    bem = input("Input csv file:")
    seq = input("Sequence Number:")
    pnev = input("Project name:")
    logging.debug(f"input file:{bem}")
    logging.debug(f"Sequence number:{seq}")
    logging.debug(f"Project name:{pnev}")
    mc.CreateMacroFromCsv(bem, seq, pnev)
