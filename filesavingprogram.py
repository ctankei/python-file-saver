username = raw_input('What is your name? ')
print 'Welcome', username, '!'
print 'This is the File Saving Program.'
print 'This program will allow you to create, name, and save text, image, and database files consecutively.'
print '--------------'

choice = None
while choice == None:
    print 'What would you like to do?'
    print '1. Save a text file.'
    print '2. Save an image file.'
    print '3. Save a database file.'
    print '4. Quit.'
    print '*Enter 1, 2, 3, or 4.*'
    choice = raw_input('> ')
    
    if choice == '1':
        name_of_text_file = raw_input("Name your text file: ")
        fullTextName = name_of_text_file + ".txt"
        text1 = open(fullTextName, "w")
        toText = raw_input("Enter content for your text file: ")
        text1.write(toText)
        print "*Your file", fullTextName, "has been saved.*"
        print '--------------'
        text1.close()
        choice = None
            
    elif choice == '2':
        import urllib
        fname = raw_input('Enter image URL: ')
        name_of_image_file = raw_input('Name your image: ')
        try:
            img = urllib.urlopen(fname).read()
            fullImageName = name_of_image_file + '.jpg'
            image1 = open(fullImageName, 'w')
            image1.write(img)
            print '*Your file', fullImageName, 'has been saved.*'
            print '--------------'
            image1.close()
        except:
            print 'Image cannot be saved.'
        choice = None

    elif choice == '3':
        import sys
        import sqlite3 as lite
        dname = raw_input('Name your 2-column database file: ')
        con = lite.connect(dname + '.db')
        cur = con.cursor()
        cur.execute("CREATE TABLE if not EXISTS dname(Column1, Column2)")
        print '*Your database', dname, 'has been created.*'
        print '--------------'
        choice = None
                
    elif choice == '4':
        print '*Program is complete. Thanks', username, 'for using the File Saving Program.*'
        print '--------------'
        quit()
    
    else:
        print '*Invalid Command. Enter 1, 2, 3, or 4.*'
        choice = None
        print '-------'