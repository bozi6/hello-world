from configparser import  ConfigParser


def read_db_config(filename='../config.ini', section='mysql'):
    """
    Read config.ini file for MySQL settings
    :param filename: name of the configuration file
    :param section: section of database configuration
    :return: a dictionary of database parameters
    """
    # create a parser and read ini configuration files
    parser = ConfigParser()
    parser.read(filename)

    # get section to mysql
    db = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            db[item[0]] = item[1]
    else:
        raise Exception('Nem találom a {} részt a {} fileban.'.format(section, filename))

    return db
