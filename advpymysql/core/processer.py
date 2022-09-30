import pymysql
from advpymysql.core.pyProperties import parse
from advpymysql.core.pyBases import *

datas = None

def setConnectionData(data):
	# global conn
	# if conn != None:
	# 	return
	# datas = parse(data)
	# conn = pymysql.connect(datas.get("db.host"),datas.get("db.username"),datas.get("db.password"),datas.get("db.database"))
	global datas
	datas = parse(data)

def execute(sql):
	global conn
	if datas == null:
		raise Exception("Connection didn't setup.")
	try:
		conn = pymysql.connect(host=datas.get("db.host"), user=datas.get("db.username"), password=datas.get("db.password"), database=datas.get("db.database"))
		cursor = conn.cursor()
		cursor.execute(sql)
		result = cursor.fetchall()
		cursor.close()
		conn.commit()
		conn.close()
		return result
	except Exception as e:
		conn.rollback()
		conn.close()
		raise e