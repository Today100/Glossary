import sqlite3


conn = sqlite3.connect('contact.db')
c = conn.cursor()



c.execute("""INSERT INTO posts(title,body)
VALUES('Learn SQlite FTS5','This tutorial teaches you how to perform full-text search in SQLite using FTS5'),
('Advanced SQlite Full-text Search','Show you some advanced techniques in SQLite full-text searching'),
('SQLite Tutorial','Help you learn SQLite quickly and effectively');""")

conn.commit()
print("""SELECT rowid, * FROM posts WHERE posts MATCH 'show'""")
c.execute("""SELECT rowid, * FROM posts WHERE posts MATCH ''""")
            #"""SELECT rowid, * FROM [goods] WHERE [goods] MATCH ['a']"""
items = c.fetchall()

print(items)
