import MySQLdb

#�s����Ʈw
try:	
	db = MySQLdb.connect(host = 'localhost',user='username',passwd='password',db='dbname',port=3306)
	
#�Q��Cursor�ӱN��ƶ��X�����C����ƿ��i��T�w���B�z�u�@
	cur = db.cursor()
#DB���J�����O
 	sql_statement = """INSERT INTO python.test1(no,price)
                       VALUES (4, 20)"""
#���J������L�X���G
    	print sql_statement

	cur.execute(sql_statement)
	db.commit()
#�p�G�b�s����Ʈw�ɥX�{���~�A�N�ⲣ�Ϳ��~�����L�X��
except MySQLdb.Error as e:
	print "Error %d: %s" % (e.args[0], e.args[1])

