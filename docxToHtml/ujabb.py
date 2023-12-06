import pypandoc

def main():
    output = pypandoc.convert_file('21.09.27.-10.03.docx', 'html', outputfile='file_converted.html')

if __name__ == "__main__":
    main()

