import mysql.connector

mydb = mysql.connector.connect(
    host="debian.hedomain.local",
    user="root",
    password="qwe",
    port=3306,
    database="honved2"
)


def helykerd(hely):
    retval = [hely]
    mycursor = mydb.cursor()
    mycursor.execute("select * from helyszinek where hely like \"%{}%\"".format(hely))
    myresult = mycursor.fetchall()
    if len(myresult) != 0:
        for eredmenyek in myresult:
            retval.append(eredmenyek)
    else:
        return None
    return retval


def helyeklista():
    retval = []
    mycursor = mydb.cursor()
    mycursor.execute("select distinct hely from helyszinek")
    myresult = mycursor.fetchall()
    if myresult is not None:
        for eredmenyek in myresult:
            retval.append(eredmenyek)
    else:
        return None
    return retval


if __name__ == '__main__':
    helyszin = input("Adjál meg egy helyszínt!")
    x = helykerd(helyszin)
    if x:
        for egy in x:
            print(egy)
