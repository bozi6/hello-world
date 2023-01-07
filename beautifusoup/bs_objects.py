from bs4 import BeautifulSoup

html_doc = """
<html>
<head>
    <title>The Dormouse's story</title>
</head>
<body>
<p class="title">
    <b>The Dormouse's story</b>
</p>
<p class="story">Once upon a time there were three little sisters; their names:
    <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>
    <a href="http://example.com/lacie class=" sister" id="link2">Lacie</a>
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.
</p>
<p class="story">...</p>
<b class="boldest">Extremely bold</b>
<blockquote class="boldest">Extremely bold</blockquote>
<b id="1">Test</b>
<b another-attribute="1" id="verybold">Test 2</b>
<p id="my id"></p>
</body>
</html>
"""

menu_opciok = {
    1: 'HTML kiiratása',
    2: 'Tag kiíratása',
    3: 'Öszes Tag kiíratása',
    4: 'Több tag kiíratásas',
    5: 'Kilépés',
}

soup = BeautifulSoup(html_doc, 'lxml')


def print_menu():
    for key in menu_opciok.keys():
        print(key, '--', menu_opciok[key])


def elso_pont():
    print(soup.prettify())


with open('index.html', 'w') as f:
    f.write(html_doc)

f.close()


def masodik_pont():
    """
    Tag
    Finds the first pccurence of usage for a "b"
    bold tag
    """
    print(soup.b)


def harmadik_pont():
    # If we want to find all of the elements on the page
    # with the "b" tag, we can use  the "find_all" function
    print('soup.find_all(b): ', soup.find_all('b'))


def negyedik_pont():
    tag = soup.find_all('b')[3]
    print('tag id 3: ', tag)
    #  We can even access multiple attributes that are
    #  non standard HTML attributes
    print('id tag: ', tag['id'])
    print('another-attrib tag: ', tag['another-attribute'])


# The "find" function also does the same, where it
# only finds the first occurence in the HTML doc
# of a tag with "b"
##print('soup.find.b: ', soup.find('b'))


# Name

# This gives the name of the tag. In this case, the_
# tag name is "b".
##print('soup.b.name: ', soup.b.name)

# We can alter the name and have the reflected in the
#  source. For instance
# tag = soup.b
# print('tag: ', tag)
# tag.name = "blockquote"
# print('tag: ', tag)

#  Attributes:

print(soup.find_all('b'))
print('-' * 24)

##tag = soup.find_all('b')[2]
##print('souptag: ', tag)

# This specific tag has the attribute "id", which
# which can be accessed like so:
##print('tag id 2 : ', tag['id'])



#  If we want to see all attributes, we can access them
#  as dictionary object:
##tag = soup.find_all('b')[3]
##print('tag 3: ', tag)

##print('tag attribs: ', tag.attrs)

# These properties are mutable, and we can alter them
# in the following manner.
##print('tag 3 : ', tag)
##tag['another-attribute'] = 2
##print('chtag: ', tag)

# We can also use Python's del command for lists to 
# remove attributes:
##del tag['id']
##del tag['another-attribute']
##print('deleted tag: ', tag)

# NavigableStrin
tag = soup.find_all('b')[3]
print('tag: ', tag)
print('tag.string: ', tag.string)

# We can use the "replace_with" function to replace
#  the content of the string with something different:
tag.string.replace_with("This is another string")
print('newtag: ', tag)

if __name__ == '__main__':
    while (True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        # Check what choice was entered and act accordingly
        if option == 1:
            elso_pont()
        elif option == 2:
            masodik_pont()
        elif option == 3:
            harmadik_pont()
        elif option == 4:
            negyedik_pont()
        elif option == 5:
            print('Köszönjük a használatot.')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 5.')
