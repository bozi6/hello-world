if __name__ == "__main__":
    """
    :description: Lófaszjoska
    """
    # -*- coding: utf-8 -*-
    befile = "C:\\ProgramData\\MA Lighting Technologies\\grandma\\gma2_V_3.9.60\\lang\\hu\\help\\structure.html"

    from bs4 import BeautifulSoup

    sql = "INSERT INTO help (sorsz, id, rel, `data-id`, title, class, `data-keyword`, `data-jstree`) VALUES "
    sqlfile = open("./mahtm2sql.sql", "w+", encoding="utf8")
    file = open(befile, "r", encoding="utf8")
    soup = BeautifulSoup(file, "html.parser")
    for x in soup.find_all("li"):
        did = x.attrs["id"]
        rel = x.attrs["rel"]
        dataid = x.attrs["data-id"]
        title = x.attrs["title"]
        attrclass = x.attrs["class"]
        datakeyword = x.attrs["data-keyword"]
        datajstree = x.attrs["data-jstree"]
        if not attrclass:
            attrclass = ""
        else:
            attrclass = attrclass[0]
        # sql += "( NULL, '{}', '{}', '{}', '{}', '{}', '{}', '{}'),".format(
        #     did, rel, dataid, title, attrclass, datakeyword, datajstree
        # )

        sql += f"(NUll '{did}', '{rel}', '{dataid}', '{title}', '{attrclass}', '{datakeyword}', '{datajstree}',)\n"
    sql = sql[:-1]
    sql = sql + ";"
    sqlfile.write(sql)
    sqlfile.close()
    file.close()
    print("ok")
