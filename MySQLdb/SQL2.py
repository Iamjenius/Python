import MySQLdb

#連結資料庫
try:	
	db = MySQLdb.connect(host = 'localhost',user='username',passwd='password',db='dbname',port=3306)
	
#利用Cursor來將資料集合中的每筆資料錄進行固定的處理工作
	cur = db.cursor()
#DB插入的指令
 	sql_statement = """INSERT INTO python.test1(no,price)
                       VALUES (4, 20)"""
#插入完成後印出結果
    	print sql_statement

	cur.execute(sql_statement)
	db.commit()
#如果在存取資料庫時出現錯誤，就把產生錯誤的欄位印出來
except MySQLdb.Error as e:
	print "Error %d: %s" % (e.args[0], e.args[1])

