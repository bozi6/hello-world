import csv
import xml.etree.ElementTree as ett
import random
import string
import unidecode

__author__ = 'kontab6@gmail.com'
__copyright__ = 'Konta Boáz@2020'


def uidgen():
    szoveg = "".join([random.choice(string.hexdigits[:16]) for x in range(32)])
    uid = ' '.join(szoveg[i:i + 2] for i in range(0, len(szoveg), 2))
    return uid.upper()


def create_macro_xml(xml_file_name, cuefile, szekszam, elnevezes):
    cuekszama = len(cuefile) + 1
    root = ett.Element("GMA3")
    root.set("DataVersion", "1.8.1.0")

    macro = ett.SubElement(root, "Macro")
    macro.set("Name", elnevezes)
    macro.set("Guid", uidgen())

    macroline = ett.SubElement(macro, "MacroLine")
    macroline.set("Command", "Store Sequence {} Cue 1 thru {}".format(szekszam, cuekszama - 1))
    macroline.set("Wait", "0.10")

    for sorszam in range(1, cuekszama):
        macroline = ett.SubElement(macro, "MacroLine")
        cueneve = unidecode.unidecode(cuefile[sorszam - 1][1])
        cueneve = cueneve.replace(" ", "")
        macroline.set("Command", "Label Sequence {} Cue {} \"{}\"".format(szekszam, sorszam, cueneve))
        macroline.set("Wait", "0.10")
    # ez kell a végére
    macroline = ett.SubElement(macro, "MacroLine")
    macroline.set("Command", "Drive 1")
    macroline = ett.SubElement(macro, "MacroLine")
    macroline.set("Command", "import timecode \"{}_timecode\"".format(elnevezes))
    macroline.set("Wait", "0.10")

    tree = ett.ElementTree(root)
    ett.indent(tree)  # A sorok tördelése enterrel
    with open(xml_file_name, "wb") as files:
        tree.write(files, xml_declaration=True, encoding='UTF-8', method='xml')


def create_timecode_xml(xml_timecode_file_name, project_neve, csv_file, sekvencia_szam):
    cuekszama = len(csv_file)-1
    utolso_marker = float(csv_file[cuekszama][2])+1
    root = ett.Element("GMA3")
    root.set("DataVersion", "1.8.1.0")

    timecode = ett.SubElement(root, "Timecode")
    timecode.set("Name", project_neve)
    timecode.set("Guid", uidgen())
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
    markertrack.set("Guid", uidgen())

    track = ett.SubElement(trackgroup, "Track")
    track.set("Guid", uidgen())
    track.set("Target", "ShowData.DataPools.Default.Sequences.Sequence {}".format(sekvencia_szam))
    track.set("Play", "")
    track.set("Rec", "")

    timerange = ett.SubElement(track, "TimeRange")
    timerange.set("Guid", uidgen())
    timerange.set("Duration", "To End")
    timerange.set("Play", "")
    timerange.set("Rec", "")

    cmdsubtrack = ett.SubElement(timerange, "CmdSubTrack")
    for ertekek in range(0, cuekszama + 1):
        cmdevent = ett.SubElement(cmdsubtrack, "CmdEvent")
        cmdevent.set("Name", "Go+")
        cmdevent.set("Time", csvfile[ertekek][2])
        cueneve = unidecode.unidecode(csvfile[ertekek][1])
        cueneve = cueneve.replace(" ", "")
        realtime_attribs = {"Type": "Key", "Source": "Original", "UserProfile": "0",
                            "User": "1",  "Status": "On", "IsRealtime": "0",
                            "IsXFade": "0",  "IgnoreFollow": "0", "IgnoreCommand": "0",
                            "Assert": "0", "IgnoreNetwork": "0", "FromTriggerNode": "0",
                            "IgnoreExecTime": "0", "IssuedByTimecode": "0",
                            "FromLocalHardwareFader": "1",  "IgnoreExecXFade": "0",
                            "IsExecXFade": "0",  "Object": "12.12.0.4.99",
                            "ExecToken": "Go+",
                            "ValCueDestination":
                                "12.12.0.4.49.{}000".format(ertekek+1)
                            }
        realtimecmd = ett.SubElement(cmdevent, "RealtimeCmd", realtime_attribs)
    tree = ett.ElementTree(root)
    ett.indent(tree)
    with open(xml_timecode_file_name, "wb") as files:
        tree.write(files, xml_declaration=True, encoding="UTF-8", method="xml")


if __name__ == "__main__":
    """ GrandMa3 Create Timecode showfile from 
    Reaper DAW exported markers
    Create two files 
    first: 
    create xxx_macro.xml
    This contain the importable macro file that creates 
    cues from the exported marker files in the given Sequence number.
    The second creates the timecode view of inserted go commands at the 
    propieatry marker points in seconds.
    
    To create this you need:
    -In reaper set markers with shift+m to give a name of a marker
    -Set timeline units to seconds in View/Time Unit for Ruler/Seconds
    -in Reaper select action list and in the list find the export markers to file
    Actions/Markers/Regions: Export markers/regions to file
    - export markers to a file
    - set in program the input file
    - satrt program
    - give a project name
    - give the sequence that contains all the data
    - copy created files to:
    grandMA3/gma3_library/datapools/timecodes/ <-- xxx_timecode.xml file
    grandMa3/gma3_library/datapools/macros/ <-- xxx_macro.xml file
    - on GrandMa3 right-click in macro pool.
    - click import.
    - it creates a seqence in sequence pool with prepared cues for each Marker
    - and creates a Timecodeshow with connections to the Sequence.
    - in macro if the drive 2 is wrong you can check it with
    the 
    List drive 
    command where the timecode xml is copyed
    Idea: fiets.de/maplace
    But this is offline version of it. 
    
    """
    print("Ma3 converter 1.8.1.0.")
    print("REAPER exported markers convert to Timecodew for Ma3.")

    kimenet_mappa = "/Users/mnte/MALightingTechnology/gma3_library/datapools/"
    # projnev = input("Projekt neve:")
    projnev = "vadi"
    seqnum = input("Szekvencia száma:")
    c = open('vivaldi_regions_markers.csv', 'r')
    print("csv file ready to read.")
    o = csv.reader(c)
    csvfile = []
    for r in o:
        csvfile.append(r)
    c.close()
    csvfile.pop(0)
    # print(csvfile)
    for i in range(0, len(csvfile)):
        csvfile[i][1] = "".join(csvfile[i][1])
    create_macro_xml(kimenet_mappa + "macros/{}_macro.xml".format(projnev), csvfile, seqnum, projnev)
    create_timecode_xml(kimenet_mappa + "timecodes/{}_timecode.xml".format(projnev), projnev, csvfile, seqnum)
