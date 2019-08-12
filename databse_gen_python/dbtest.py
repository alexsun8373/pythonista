import sqlite3


def creat_database():
	conn = sqlite3.connect('wanglu_linguistic_material.db')
	c=conn.cursor()
	
	#create table
	c.execute("CREATE TABLE wanglu_linguistic_material (id integer primary key,chapter integer, section integer, number integer, word text)")
	
	#c.execute("INSERT INTO stocks VALUES ('2006-03-28','BUY','IBM',1000,45.00)")
	
	#conn.commit()
	#t = ('IBM',)
	#c.execute('SELECT * FROM stocks WHERE symbol=?',t)
	#print(c.fetchall())
	
	#t=('IBM')
	#c.execute('SELECT * FROM stocks1 WHERE symbol=?',t)
	#print(c.fetchone())
	
	purchases=[ (1,3,2,1,'ability'),
							(2,3,2,2,'abstract'),
							(3,3,2,3,'accountant'),
							(4,3,2,4,'accuracy'),
							(5,3,2,5,'acid'),
							(6,3,2,6,'action'),
							(7,3,2,7,'activity'),
							(8,3,2,8,'actor'),
							(9,3,2,9,'adult'),
							(10,3,2,10,'adventure')
							]
	c.executemany("INSERT INTO wanglu_linguistic_material VALUES (?,?,?,?,?)",purchases)
	conn.commit()
	for row in c.execute('SELECT * FROM wanglu_linguistic_material ORDER BY number'):
		print(row)
	conn.close
	
def db_length():
	conn = sqlite3.connect('wanglu_linguistic_material.db')
	cursor = conn.cursor()
	cursor.execute("select * from wanglu_linguistic_material")
	results = cursor.fetchall()	
	length = len(results)
	conn.close

creat_database()
