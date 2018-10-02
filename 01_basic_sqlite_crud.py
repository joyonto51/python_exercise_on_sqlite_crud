import sqlite3

db = sqlite3.connect("01_author.sqlite3")
cursor = db.cursor()

cursor.execute(''' CREATE TABLE IF NOT EXISTS author(
			id INTEGER PRIMARY KEY,
			username TEXT unique,
			author_name TEXT
			)
	''')

authors = [
	(1, 'almasud', 'Abdullah AL Masud'),
	(2, 'rimon', 'Rimon Ali'),
	(3, 'niloy', 'Nloy Roy'),
	(4, 'sourav', 'Sourav Deb Sharma'),
	(5, 'sathi', 'Sathi Rani Roy')
]

try:
	cursor.executemany('''INSERT INTO author(id,username,author_name) 
						VALUES(?,?,?)''', authors)
except:
	pass
	
cursor.execute('''SELECT id, author_name FROM author''')
all_authors = cursor.fetchall()

for author in all_authors:
	print("{}-{}".format(author[0], author[1]))


db.commit()
db.close()