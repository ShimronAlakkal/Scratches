
def setUp():
	import mysql.connector 
	import login_signup

	connection = mc.connect(host='localhost',user='root',passwd='qwertyuiopasdfghjkl')
	crs = connection.cursor()
	
	login_signup.mainAuth()
		
setUp()