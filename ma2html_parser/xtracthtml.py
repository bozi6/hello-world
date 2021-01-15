from bs4 import BeautifulSoup

sql = "INSERT INTO help (sorsz, id, rel, `data-id`, title, class, `data-keyword`, `data-jstree`) VALUES "
sqlfile = open('./mahtm2sql.sql', 'w+')
file = open('C:\\ProgramData\\MA Lighting Technologies\\grandma\\gma2_V_3.9.51\\lang\\hu\\help\\structure.html', 'r')
soup = BeautifulSoup(file, 'html.parser')
for x in soup.find_all('li'):
    sql += (
        f"(NULL, '{x.attrs['id']}', '{x.attrs['rel']}', '{x.attrs['data-id']}', '{x.attrs['title']}', '{x.attrs['class']}','{x.attrs['data-keyword']}', '{x.attrs['data-jstree']}'), ")
sql = sql[:-2]
sql = sql+';'
sqlfile.write(sql)
sqlfile.close()
file.close()
print('ok')

