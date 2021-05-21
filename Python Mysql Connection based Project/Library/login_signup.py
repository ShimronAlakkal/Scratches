
import mysql.connector as mc
import main_window

connection = mc.connect(host='localhost',user='root',passwd='your pass')
crs = connection.cursor()

crs.execute('create database IF NOT EXISTS botnet')
crs.execute('use botnet ')
crs.execute('create table IF NOT EXISTS user (name varchar(30) primary key , pass varchar(20) not null )')
crs.execute('create table IF NOT EXISTS books (book varchar(50) not null ,author varchar(30), ID int(4) primary key, qty int(4) ,price int(4) )')
connection.commit()
try: 
	crs.execute("insert into user values('Admin', '12344' )")
	crs.execute("insert into user values('Sample', '1234' )")
	connection.commit()
	crs.execute("insert into books values('In Search of Lost Time','Marcel Proust', 102 , 20,100 )")
	crs.execute("insert into books values('Sapiens','Yuval Noah Harari', 103 , 231,650 )")
	crs.execute("insert into books values('Harry Potter','JK Rowling', 101 , 13 ,100)")
	crs.execute("insert into books values('The Great Gatsby','F. Scott Fitzgerald', 104 , 113 ,230)")
	crs.execute("insert into books values('A Brief History of Time','Stephen Hawking', 105 , 303 ,230)")
	crs.execute("insert into books values('Brief Answers to the Big Questions','Stephen Hawking', 106 , 13,100)")
	connection.commit()
except :
	pass


def userSingIn(Username, Password):

	crs.execute("SELECT name,pass from USER where name like '"+str(Username)+"'" )
	result = crs.fetchall()

	if result[0][0] == Username and result[0][1] == Password:
		main_window.mainView(0)
	else:
		print('Entered username or password is wrong. Please try again ')


def userSignUp(Username, Password):
	crs.execute("INSERT INTO USER values ('"+str(Username)+"','"+str(Password)+"')")
	connection.commit()
	main_window.mainView(0)


def userCheck(Username):
	crs.execute("SELECT name from USER where name like '"+str(Username)+"'" )
	result = crs.fetchall()
	try:
		if result[0][0] == Username :
			return True	
	except :
		return False
	return False


def Auth(val):

	if val != 0:
		print('\n Already a user?? press 1 \n New to Botnet?? press 2 \n or press 0 to exit \n ')
		crs.execute('use Botnet')
		auth = int(input('>>>'))
		if auth == 1:
			username = input('Please enter your Botnet username ')
			passwd = str(input("Please enter your password for Botnet "))
			
			userSingIn(username,passwd)
		elif auth == 2:
			username = input('Please enter your username for Botnet ')
			if userCheck(username) :	
				print('Username Already Taken. Try Again ')
				Auth(1)	
			else:
				passwd = eval(input("Please enter your password for Botnet "))		
				userSignUp(username,passwd)
			
		elif auth == 0:
			exit()

	else:
		print('''
                     ___      __ ___
                |) /\ | |\ | |__  |
                |) \/ | | \| |__  |

        ''')
		print('\t\t Welcome to Botnet \n\t\t login/signup')
		Auth(1)



if __name__ == '__main__':
	Auth(0)
