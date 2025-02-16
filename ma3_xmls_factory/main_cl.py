import csv
import logging
import os.path
import random
import string
import xml.etree.ElementTree as ett

import unidecode

__author__ = "Konta Boáz"
__email__ = "kontab6@gmail.com"
__version__ = "2.0"
__license__ = "MIT"
__copyright__ = "Copyright (c) 2022 Konta Boáz"
__title__ = "from csv to MA3 xmls"
__description__ = "Ma3 classes to create xml to timecode and sequence"
__url__ = "https://www.gituhb.org/bozi6/"
__uri__ = __url__
__doc__ = __description__ + " <" + __uri__ + ">"

# For debugging remove # from next line.
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


class CreateMacroFromCsv(object):
    """
    MA3 Macro createer Class from csv file
    """

    projekt_nev: str
    seq_szam: int
    bemenet_file: object

    def __init__(self, bemenet_file, seq_szam, projekt_nev):
        """

        :param bemenet_file: input csv file
        :param seq_szam: the number of sequence pool where sequences generated.
        :param projekt_nev: The name of generated macro and sequence and timecode pool objects.

        """
        self.bemenet_file = bemenet_file
        self.seq_szam = int(seq_szam)
        self.projekt_nev = projekt_nev
        if (
            logging.getLogger().getEffectiveLevel() == 30
        ):  # ha nem debuggolunk akkor mehet élesben
            self.kimeneti_mappa = (
                "/Users/mnte/MALightingTechnology/gma3_library/datapools/"
            )
        else:
            self.kimeneti_mappa = "./test/"
            self.pathexist(self.kimeneti_mappa)
        self.csv_dict = []
        self.tree = ett.ElementTree
        self.read_xml()
        logging.debug("Init called.")
        self.create_xml_macro()
        self.create_xml_time()

    @staticmethod
    def pathexist(path):
        """
        Runtime path checker for folders available

        :param path: existing path
        :type path: str
        :return: Ture
        :rtype: bool

        """
        if os.path.exists(path):
            return True
        else:
            os.mkdir(path)
            os.mkdir(path + "/macros")
            os.mkdir(path + "/timecodes")
            return True

    @staticmethod
    def uidgen():
        """
        Create a uuid for xml attributes

        :return: the generated uid with spaces between two numbers
        :rtype: str

        """
        szoveg = "".join([random.choice(string.hexdigits[:16]) for x in range(32)])
        uid = " ".join(szoveg[i: i + 2] for i in range(0, len(szoveg), 2))
        logging.debug(f"Generated UUID: {uid.upper()}")
        return uid.upper()

    def read_xml(self):
        """
        Read given csv file and convert it to dictionary

        :return: Readad csv file into dictionary
        :rtype: dict

        """
        try:
            csv_file = open(self.bemenet_file)
            ofile = csv.reader(csv_file)
            logging.debug("Read XML called")
            for readline in ofile:
                self.csv_dict.append(readline)
            csv_file.close()
            self.csv_dict.pop(0)
            for i in range(0, len(self.csv_dict)):
                self.csv_dict[i][1] = "".join(self.csv_dict[i][1])
            logging.debug(f"Output dictionary first element: {self.csv_dict[0]}")
            return self.csv_dict
        except FileNotFoundError:
            print("File not found...")
            exit(1)
        except IndexError:
            print("File format mismatch...")
            exit(1)

    def create_xml_macro(self):
        """
        Create {projectname}_macro.xml file in destination folder


        """
        logging.debug("create_xml_macro called")
        kimeneti_file = self.projekt_nev + "_macro.xml"
        cuek_szama = len(self.csv_dict) + 1

        logging.debug(f"Output macroxml file name: {kimeneti_file}")
        logging.debug(f"Number of cues in file: {cuek_szama}")
        root = ett.Element("GMA3")
        root.set("DataVersion", "1.8.1.0")

        macro = ett.SubElement(root, "Macro")
        macro.set("Name", self.projekt_nev)
        macro.set("Guid", self.uidgen())

        macroline = ett.SubElement(macro, "MacroLine")
        macroline.set(
            "Command",
            "Store Sequence {} Cue 1 thru {}".format(self.seq_szam, cuek_szama - 1),
        )
        macroline.set("Wait", "0.10")

        for sorsz in range(1, cuek_szama):
            macroline = ett.SubElement(macro, "MacroLine")
            cueneve = unidecode.unidecode(self.csv_dict[sorsz - 1][1])
            cueneve = cueneve.replace(" ", "")
            cueneve = cueneve.capitalize()
            macroline.set(
                "Command",
                'Label Sequence {} Cue {} "{}"'.format(self.seq_szam, sorsz, cueneve),
            )
            macroline.set("Wait", "0.10")

        macroline = ett.SubElement(macro, "MacroLine")
        macroline.set(
            "Command", 'Label Sequence {} "{}"'.format(self.seq_szam, self.projekt_nev)
        )
        macroline.set("Wait", "0.10")
        macroline = ett.SubElement(macro, "MacroLine")
        macroline.set("Command", "Drive 1")
        macroline = ett.SubElement(macro, "MacroLine")
        macroline.set(
            "Command", 'import timecode "{}_timecode"'.format(self.projekt_nev)
        )

        self.tree = ett.ElementTree(root)
        ett.indent(self.tree)
        self.write_xml_file(self.kimeneti_mappa + "macros/" + kimeneti_file)

    def create_xml_time(self):
        """
        Create the {project_name}_timecode.xml file in output folder

        :return: output file
        :rtype: xml file

        """

        kimeneti_file = self.projekt_nev + "_timecode.xml"
        cuek_szama = len(self.csv_dict) - 1
        utolso_marker = float(self.csv_dict[cuek_szama][2]) + 1
        logging.debug("Create timceode called")
        logging.debug(f"Cues numbers: {cuek_szama}")
        logging.debug(f"Last marker: {utolso_marker}")
        root = ett.Element("GMA3")
        root.set("DataVersion", "1.8.1.0")

        timecode = ett.SubElement(root, "Timecode")
        timecode.set("Name", self.projekt_nev)
        timecode.set("Guid", self.uidgen())
        timecode.set("Cursor", "00.00")
        timecode.set("Duration", str(utolso_marker))
        timecode.set("LoopCount", "0")
        timecode.set("TCSlot", "-1")
        timecode.set("AutoStop", "No")
        timecode.set("SwitchOff", "Keep Playbacks")
        timecode.set("Goto", "as Go")
        timecode.set("TimeDisplayFormat", "<Default>")
        timecode.set("FrameReadout", "Default")

        trackgroup = ett.SubElement(timecode, "TrackGroup")
        trackgroup.set("Play", "")
        trackgroup.set("Rec", "")

        markertrack = ett.SubElement(trackgroup, "MarkerTrack")
        markertrack.set("Name", "Marker")
        markertrack.set("Guid", self.uidgen())

        track = ett.SubElement(trackgroup, "Track")
        track.set("Name", self.projekt_nev)
        track.set("Guid", self.uidgen())
        track.set(
            "Target", "ShowData.DataPools.Default.Sequences.{}".format(self.projekt_nev)
        )
        track.set("Play", "")
        track.set("Rec", "")

        timerange = ett.SubElement(track, "TimeRange")
        timerange.set("Guid", self.uidgen())
        timerange.set("Duration", "To End")
        timerange.set("Play", "")
        timerange.set("Rec", "")

        cmdsubtrack = ett.SubElement(timerange, "CmdSubTrack")
        for ertekek in range(0, cuek_szama + 1):
            cmdevent = ett.SubElement(cmdsubtrack, "CmdEvent")
            cmdevent.set("Name", "Go+")
            cmdevent.set("Time", self.csv_dict[ertekek][2])
            realtime_attribs = {
                "Type": "Key",
                "Source": "Original",
                "UserProfile": "0",
                "User": "1",
                "Status": "On",
                "IsRealtime": "0",
                "IsXFade": "0",
                "IgnoreFollow": "0",
                "IgnoreCommand": "0",
                "Assert": "0",
                "IgnoreNetwork": "0",
                "FromTriggerNode": "0",
                "IgnoreExecTime": "0",
                "IssuedByTimecode": "0",
                "FromLocalHardwareFader": "1",
                "IgnoreExecXFade": "0",
                "IsExecXFade": "0",
                "ExecToken": "Go+",
                "ValCueDestination": "12.12.0.4.{}.{}000".format(
                    self.seq_szam - 1, ertekek + 1
                ),
            }
            # old value: "ValCueDestination": "12.12.0.4.49.{}000".format(ertekek + 1)
            # az Object is ugyanaz 12.12.0.4.99
            realtimecmd = ett.SubElement(cmdevent, "RealtimeCmd", realtime_attribs)
        self.tree = ett.ElementTree(root)
        ett.indent(self.tree)
        self.write_xml_file(self.kimeneti_mappa + "timecodes/" + kimeneti_file)

    def write_xml_file(self, mitirokki):
        """
        Writes xml file

        :param: mitirokki: a kiirandó fájl neve
        :type: xml
        :return: Nothing
        :rtype: Null

        """
        print("Files created in: " + mitirokki)
        with open(mitirokki, "wb") as files:
            self.tree.write(files, xml_declaration=True, encoding="UTF-8", method="xml")


if __name__ == "__main__":
    print("REAPER exported csv to Ma3 timecode converter for MA3 version:1.8.1.0.")
    print("REAPER exported markers convert to Timecodew for Ma3.")
    """
    bem = input("csv file name:")
    seq = input("Sequence number")
    pnev = input("Project name:")
    """
    bem = "vrm.csv"
    seq = 3
    pnev = "vivaldi_neo"
    logging.debug(f"input file:{bem}")
    logging.debug(f"Sequence number:{seq}")
    logging.debug(f"Project name:{pnev}")
    new_test = CreateMacroFromCsv(bem, seq, pnev)
