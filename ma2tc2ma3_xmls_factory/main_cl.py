import os.path
import xml.etree.ElementTree as ett
import random
import string
import unidecode
import logging
import platform


__author__ = 'Konta Boáz'
__email__ = 'kontab6@gmail.com'
__version__ = '2.0'
__license__ = "MIT"
__copyright__ = "Copyright (c) 2022 Konta Boáz"
__title__ = 'from csv to MA3 xmls'
__description__ = "Ma3 classes to create xml to timecode and sequence"
__url__ = "https://www.git.org/bozi6/"
__uri__ = __url__
__doc__ = __description__ + " <" + __uri__ + ">"

# For debugging remove # from next line.
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


class CreateMacroFromXml(object):
    def __init__(self, bemenet_file, seq_szam, projekt_nev):
        """

        :param bemenet_file: input csv file
        :param seq_szam: the number of generated sequence in sequence pool.
        :param projekt_nev: The name of generated macro and sequence and timecode pool objects.
        """
        self.bemenet_file = bemenet_file
        self.seq_szam = seq_szam
        self.projekt_nev = projekt_nev
        if logging.getLogger().getEffectiveLevel() == 30:  # ha nem debuggolunk akkor mehet élesben
            if platform.system() == 'Darwin':
                self.kimeneti_mappa = "/Users/mnte/MALightingTechnology/gma3_library/datapools/"
            elif platform.system() == 'Windows':
                self.kimeneti_mappa = "C:/ProgramData/MALightingTechnology/gma3_library/datapools/"
        else:
            self.kimeneti_mappa = "./debugtest/"
            self.pathexist(self.kimeneti_mappa)
        self.csv_dict = []
        self.tree = ett.ElementTree
        self.read_xml()
        logging.debug("Init called.")
        self.create_xml_macro()
        self.create_xml_time()

    @staticmethod
    def pathexist(path):
        if os.path.exists(path):
            return True
        else:
            os.mkdir(path)
            os.mkdir(path + "/macros")
            os.mkdir(path + "/timecodes")
            return False

    @staticmethod
    def uidgen():
        """
        Create a uuid for xml attributes
        :return: the generated uid with spaces between two numbers
        """
        szoveg = "".join([random.choice(string.hexdigits[:16]) for x in range(32)])
        uid = ' '.join(szoveg[i:i + 2] for i in range(0, len(szoveg), 2))
        logging.debug(f"Generated UUID: {uid.upper()}")
        return uid.upper()

    def read_xml(self):
        """
        Read given xml file and convert it to dictionary
        :return: Readad xml file into dictionary
        """
        try:
            tree = ett.parse(self.bemenet_file)
            root = tree.getroot()
            """for child in root.iter():
                print("Tag: ", child.tag, " Attrib: ", child.attrib)"""
            for child in root.findall('.//{http://schemas.malighting.de/grandma2/xml/MA}SubTrack'):
                # print("child attrib: ", child.attrib)
                logging.debug(f"SubTrack index attrib: {child.get('index')}")
                for cue in child.findall('.//{http://schemas.malighting.de/grandma2/xml/MA}Event'):
                    logging.debug(f"child command attrib: {child.get('command')}")
                    if cue.get('time') is not None:
                        ido = self.sectotime(int(cue.get('time')))
                        ido = "{:.2f}".format(ido)
                    else:
                        ido = '0'
                    logging.debug(f"Ido érték:  {ido}")
                    logging.debug(f"Cue name:  {cue[0].get('name')}")
                    cuename = cue[0].get('name')
                    # logging.debug(f"cue: {cue[0].text}")
                    logging.debug(f"cue: {cue[0][1].text}")
                    logging.debug(f"cue: {cue[0][2].text}")
                    cuenum = cue[0][2].text
                    egy = [cuenum, cuename, ido]
                    self.csv_dict.append(egy)

                logging.debug('-' * 32)
                return self.csv_dict
        except FileNotFoundError:
            print('File not found...')
            exit(1)
        except IndexError:
            print('File format mismatch...')
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
        macroline.set("Command", "Store Sequence {} Cue 1 thru {}".format(self.seq_szam, cuek_szama - 1))
        macroline.set("Wait", "0.10")

        for sorsz in range(1, cuek_szama):
            macroline = ett.SubElement(macro, "MacroLine")
            cueneve = unidecode.unidecode(self.csv_dict[sorsz - 1][1])
            cueneve = cueneve.replace(" ", "_")
            macroline.set("Command", "Label Sequence {} Cue {} \"{}\"".format(self.seq_szam, sorsz, cueneve))
            macroline.set("Wait", "0.10")

        macroline = ett.SubElement(macro, "MacroLine")
        macroline.set("Command", "Label Sequence {} \"{}\"".format(self.seq_szam, self.projekt_nev))
        macroline.set("Wait", "0.10")
        macroline = ett.SubElement(macro, "MacroLine")
        macroline.set("Command", "Drive 1")
        macroline = ett.SubElement(macro, "MacroLine")
        macroline.set("Command", "import timecode \"{}_timecode\"".format(self.projekt_nev))

        self.tree = ett.ElementTree(root)
        ett.indent(self.tree)
        self.write_xml_file(self.kimeneti_mappa + "macros/" + kimeneti_file)

    def create_xml_time(self):
        """
            Create the {project_name}_timecode.xml file in output folder
        """
        kimeneti_file = self.projekt_nev + "_timecode.xml"
        cuek_szama = len(self.csv_dict) - 1
        utolso_marker = float(self.csv_dict[cuek_szama][2]) + 1
        logging.debug("Create timceode called")
        logging.debug(f"Cues numbers: {cuek_szama}")
        logging.debug(f"Last marker: {utolso_marker}")
        root = ett.Element("GMA3")
        root.set("DataVersion", "1.8.1.0")

        idocode = ett.SubElement(root, "Timecode")
        idocode.set("Name", self.projekt_nev)
        idocode.set("Guid", self.uidgen())
        idocode.set("Cursor", "00.00")
        idocode.set("Duration", str(utolso_marker))
        idocode.set("LoopCount", "0")
        idocode.set("TCSlot", "-1")
        idocode.set("AutoStop", "No")
        idocode.set("SwitchOff", "Keep Playbacks")
        idocode.set("Goto", "as Go")
        idocode.set("TimeDisplayFormat", "<Default>")
        idocode.set("FrameReadout", "Default")

        trackgroup = ett.SubElement(idocode, "TrackGroup")
        trackgroup.set("Play", "")
        trackgroup.set("Rec", "")

        markertrack = ett.SubElement(trackgroup, "MarkerTrack")
        markertrack.set("Name", "Marker")
        markertrack.set("Guid", self.uidgen())

        track = ett.SubElement(trackgroup, "Track")
        track.set("Name", self.projekt_nev)
        track.set("Guid", self.uidgen())
        track.set("Target", "ShowData.DataPools.Default.Sequences.{}".format(self.projekt_nev))
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
            realtime_attribs = {"Type": "Key", "Source": "Original", "UserProfile": "0",
                                "User": "1", "Status": "On", "IsRealtime": "0",
                                "IsXFade": "0", "IgnoreFollow": "0", "IgnoreCommand": "0",
                                "Assert": "0", "IgnoreNetwork": "0", "FromTriggerNode": "0",
                                "IgnoreExecTime": "0", "IssuedByTimecode": "0",
                                "FromLocalHardwareFader": "1", "IgnoreExecXFade": "0",
                                "IsExecXFade": "0",
                                "ExecToken": "Go+",
                                "ValCueDestination":
                                    "12.12.0.4.{}.{}000".format(self.seq_szam - 1, ertekek + 1)
                                }
            # old value: "ValCueDestination": "12.12.0.4.49.{}000".format(ertekek + 1)
            # az Object is ugyanaz 12.12.0.4.99
            realtimecmd = ett.SubElement(cmdevent, "RealtimeCmd", realtime_attribs)
        self.tree = ett.ElementTree(root)
        ett.indent(self.tree)
        self.write_xml_file(self.kimeneti_mappa + "timecodes/" + kimeneti_file)

    def write_xml_file(self, mitirokki):
        print("Files created in: " + mitirokki)
        with open(mitirokki, "wb") as files:
            self.tree.write(files, xml_declaration=True, encoding="UTF-8", method="xml")

    @staticmethod
    def sectotime(secs):
        return secs / 30


if __name__ == "__main__":
    print("MA2 exported xml to Ma3 timecode converter for MA3 version:1.8.1.0.")
    """
    bem = input("csv file name:")
    seq = input("Sequence number")
    pnev = input("Project name:")
    """
    bem = "halaltimecode.xml"
    seq = 10
    pnev = "halali"
    logging.debug(f"input file:{bem}")
    logging.debug(f"Sequence number:{seq}")
    logging.debug(f"Project name:{pnev}")
    new_test = CreateMacroFromXml(bem, seq, pnev)
