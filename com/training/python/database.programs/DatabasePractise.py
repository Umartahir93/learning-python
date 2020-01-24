import sqlite3

connection = sqlite3.connect("arsenalfootballclub.sqlite")
emaildbcursor = connection.cursor()

emaildbcursor.execute('''DROP TABLE IF EXISTS COUNT''')
emaildbcursor.execute('''Create table count (
                        word varchar(250), count integer );''')


filehandle = open("arsenalvschelsea")
text = filehandle.read().strip()
words = text.split()

for word in words:
    emaildbcursor.execute("Select * from count where word = ?",(word,))
    row = emaildbcursor.fetchone()
    if row is None:
        emaildbcursor.execute("INSERT INTO COUNT(word,count) VALUES (? , ?);",(word,1,))
    else:
        emaildbcursor.execute("UPDATE COUNT SET count = ? where word = ? ",(row[1]+1,word,))

for row in emaildbcursor.execute("Select * from count"):
    print(row[0],row[1])








