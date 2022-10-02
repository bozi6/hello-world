from twisted.trial import unittest
from ma2tc2ma3_xmls_factory import main_cl


class TestCreateMacroFromXml(unittest.TestCase):
    def test_pathexist(self):
        te = main_cl.CreateMacroFromXml
        result = te.pathexist('./test')
        self.assertEquals(result, False)

    def test_sectotime(self):
        te = main_cl.CreateMacroFromXml
        result = te.sectotime(450)
        self.assertEquals(result, 15)

    def test_read_xml(self):
        self._passed
