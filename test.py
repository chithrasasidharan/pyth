import MySQLdb

conn = pymssql.connect(server=server, user=user,password=password,
	database=db)
cursor = conn.cursor()

conn.close()