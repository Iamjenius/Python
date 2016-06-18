import MySQLdb

try:	
	db = MySQLdb.connect(host = 'localhost',user='username',passwd='password',db='dbname',port=3306)
	cur = db.cursor()
#°õ¦æDB´À´«ªº«ü¥O
 	sql_statement = """REPLACE INTO python.test1(no,price)
                       VALUES (4, 21)"""
    	print sql_statement

	cur.execute(sql_statement)
	db.commit()

except MySQLdb.Error as e:
	print "Error %d: %s" % (e.args[0], e.args[1])

