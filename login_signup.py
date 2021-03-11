
import mysql.connector as mc
import main_window

connection = mc.connect(host='localhost',user='root',passwd='qwertyuiopasdfghjkl')
crs = connection.cursor()

def userSingIn(Username, Password):

	crs.execute('SELECT name from USER ')
	result = crs.fetchall()
	if name in result:
		crs.execute("SELECT pass FROM user where name='" +
                    str(Username)+"';")
		passwd = crs.fetchone()
		if passwd in Password or Password == passwd :
			print('''

				Signing into your Botnet account

				''')

			main_window.mainView()
		else:
			print('Wrong Password for the entered username ')
			mainAuth()
	else:
		print('Entered username or password is wrong. Please try again ')
		mainAuth()


def userSignUp(Username, Password):
	try:
		crs.execute("INSERT INTO USER values ('"+str(Username)+"','"+str(Password)+"')")
		connection.commit()
	except:
		print('Please try again ')
		mainAuth()


def mainAuth():

	print('\t\t\t\t Welcome to Botnet \n\t\t\t\t login/signup')
	print('\n Already a user?? press 1 \n New to Botnet?? press 2 \n or press 0 to exit ')
	crs.execute('use Botnet')
	auth = int(input('>>>'))
	if auth == 1:
		username = input('Please enter your Botnet username ')
		passwd = eval(input("Please enter your password for Botnet "))
		try:
			userSingIn(username,passwd)
		except :
			print('Please try again')
			mainAuth()
	elif auth == 2:
		username = input('Please enter your username for Botnet ')
		passwd = eval(input("Please enter your password for Botnet "))
		userSignUp(username,passwd)

	elif auth == 0:
		exit()


print('''
                     ___      __ ___
                |) /\ | |\ | |__  |
                |) \/ | | \| |__  |

				   Login/signup 

        ''')

crs.execute('create database IF NOT EXISTS botnet')
crs.execute('use botnet ')
crs.execute('create table IF NOT EXISTS user (name varchar(30) primary key , pass varchar(20) not null )')
crs.execute('create table IF NOT EXISTS books (book varchar(50) not null ,author varchar(30), ID int(4) primary key, qty int(4) ,price int(4) )')
connection.commit()
crs.execute("insert into user values('Admin', 12344 )")
crs.execute("insert into user values('Sample', 1234 )")
connection.commit()
crs.execute("insert into books values('In Search of Lost Time','Marcel Proust', 102 , 20,100 )")
crs.execute("insert into books values('Sapiens','Yuval Noah Harari', 103 , 231,650 )")
crs.execute("insert into books values('Harry Potter','JK Rowling', 101 , 13 ,100)")
crs.execute("insert into books values('The Great Gatsby','F. Scott Fitzgerald', 104 , 113 ,230)")
crs.execute("insert into books values('A Brief History of Time','Stephen Hawking', 105 , 303 ,230)")
crs.execute("insert into books values('Brief Answers to the Big Questions','Stephen Hawking', 106 , 13,100)")
connection.commit()

mainAuth()