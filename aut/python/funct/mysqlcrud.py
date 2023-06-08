import mysql.connector

mydb = mysql.connector.connect(
    host="ds718.lan",
    user="root",
    password="qwe",
    port=3307,
    database="honved2"
)


def helykerd(hely):
    retval = [hely]
    mycursor = mydb.cursor()
    mycursor.execute("select * from helyszinek where hely like '%{}%'".format(hely))
    myresult = mycursor.fetchall()
    if myresult is not None:
        for eredmenyek in myresult:
            retval.append(eredmenyek)
    else:
        return None
    return retval


if __name__ == '__main__':
    x = helykerd('pécs')
    print(len(x))
    if x:
        for egy in x:
            print(egy)
