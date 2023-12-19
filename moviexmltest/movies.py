if __name__ == "__main__":
    import xml.etree.ElementTree as Et

    tree = Et.parse("movies.xml")
    root = tree.getroot()

    def childattrib(root):
        """
        Kiirja az gyermekobjekteket

        :param root: xml root
        :type root: str
        :return: prints children tags and attribs
        :rtype: str

        """
        for child in root:
            print(child.tag, child.attrib)

    def childrenwrite(root):
        """

        :param root: xml root object
        :type root: Etree
        :return: prints movie attribs
        :rtype: str

        """
        for movie in root.iter("movie"):
            print(movie.attrib)

    def descript(root):
        """
        Prints description field

        :param root: xml file with description field
        :type root: xml
        :return: prints description
        :rtype: str

        """
        for description in root.iter("description"):
            print(description.text)

    def moviedate(miko="1992"):
        """
        Prints 1992 films

        :param miko: year when released
        :type miko: str
        :return: prints finded films
        :rtype: str

        """
        for movie in root.findall(f"./genre/decade/movie/[year='{miko}']"):
            print(movie.attrib)

    def multipleformats(root):
        """
        Find movies that are available in multiple formats

        :return: print films
        :rtype: str

        """
        for movie in root.findall("./genre/decade/movie/format/[@multiple='Yes']"):
            print(movie.attrib)

    def multilpeparent(root):
        """
        Find movies that are available in multiple formats print the parent element

        :return: print multiformats parent element
        :rtype: str

        """
        for movie in root.findall("./genre/decade/movie/format/[@multiple='Yes']..."):
            print(movie.attrib)

    def cimcsere(mit, mire):
        """
        Kicseréli a film címét.

        :param: mit:Melyik címet keressük
        :type: mit: str
        :param: mire: Mire cseréljük
        :type: mire: str
        :return: kiirja ha kész
        :rtype: str

        """
        # Egy elem megkeresése és cserélése
        b2tf = root.find(f"./genre/decade/movie/[@title='{mit}']")
        print(b2tf)
        b2tf.attrib["title"] = mire
        print(b2tf.attrib)

    input("gyerek elemek listázása")
    childattrib(root)
    input("filmek attribútumai")
    childrenwrite(root)
    input("filmek leírása")
    descript(root)
    input("1992-es filmek listája")
    moviedate("1992")
    input("multiformátumú filmek listázása")
    multipleformats(root)
    input("multiformátum szülő lista")
    multilpeparent(root)
    input("Back 2 the future javítása")
    cimcsere("Vissza 2 jövőbe", "Vissza a jövőbe")

    """
    # Fájl kiírása vissza és a javított dolog elhelyezése
    tree.write("movies.xml")
    
    # Ismételt kiírás ellenőrzésileg
    tree.Et.parse('movies.xml')
    root = tree.getroot()
    
    for movie in root.iter('movie'):
        print(movie.attrib)
    """

    for form in root.findall("./genre/decade/movie/format"):
        print(form.attrib, form.text)
    input("multiformat kiirása")
    # A movie format multiple javítása csak Yes vagy No-ra
    """
    import re
    
    for form in root.findall("./genre/decade/movie/format"):
        # Search for the commas in the format text
        match = re.search(',',form.text)
        if match:
            form.set('multiple','Yes')
        else:
            form.set('multiple','No')
    
    # Write out the tree to the file again
    tree.write("movies.xml")
    
    tree = ET.parse('movies.xml')
    root = tree.getroot()
    
    for form in root.findall("./genre/decade/movie/format"):
        print(form.attrib, form.text)
    """

    # Évtized és évek kiírása
    for decade in root.findall("./genre/decade"):
        print(decade.attrib)
        for year in decade.findall("./movie/year"):
            print(year.text, "\n")
    input("Évtizedek és évek kiírása")
    # milyen filmek vannak 2000 ből
    for movie in root.findall("./genre/decade/movie/[year='2000']"):
        print(movie.attrib)
    input("Filmek listázása 2000-ből")
    # Új évtized hozzáadása az akciófilmek kategóriához
    action = root.find("./genre[@category='Akció']")
    new_dec = Et.SubElement(action, "decade")
    new_dec.attrib["years"] = "2000s"

    print(Et.tostring(action, encoding="utf8").decode("utf8"))
    input("Új kategória hozzáadva")
    # márcsak átrakjuk az X-ment a 90-esből a 2000-es évtizedbe
    xmen = root.find("./genre/decade/movie[@title='X-Men']")
    dec2000s = root.find("./genre[@category='Akció']/decade[@years='2000s']")
    dec2000s.append(xmen)
    dec1990s = root.find("./genre[@category='Akció']/decade[@years='1990s']")
    dec1990s.remove(xmen)

    print(Et.tostring(action, encoding="utf8").decode("utf8"))
    input("Csere megtörtént")
