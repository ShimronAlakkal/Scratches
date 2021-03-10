
import mysql.connector as mc
connection = mc.connect(host='localhost',user='root',passwd='qwertyuiopasdfghjkl')
crs = connection.cursor()
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
crs.execute("insert into books values('Harry Potter','JK Rowling', 101 , 13 ,100)")
crs.execute("insert into books values('In Search of Lost Time','Marcel Proust', 102 , 20,100 )")
crs.execute("insert into books values('Sapiens','Yuval Noah Harari', 103 , 231,650 )")
crs.execute("insert into books values('The Great Gatsby','F. Scott Fitzgerald', 104 , 113 ,230)")
crs.execute("insert into books values('A Brief History of Time','Stephen Hawking', 105 , 303 ,230)")
crs.execute("insert into books values('Brief Answers to the Big Questions','Stephen Hawking', 106 , 13,100)")
connection.commit()
	

while True:
	do_yo = input('''
	DO YOU HAVE A BOTNET ACCOUNT ? (y/n)
	>>>  ''')
	if do_yo =='y':
		print('LOGIN')
		name =  str(input('Please enter your USER-NAME > '))
		passw = input('Please enter your pass for Botnet >')
		print(crs.execute("select name from user where name like %s",(name)))

	# 		print('''
	# 			Login Successful

	# 		''')
	# 		mainRun()
	# 		break

	# 	else :
	# 		print('No such user found. Please retry !!! ')
		
	elif do_yo == 'exit':
		break	
		
	elif do_yo == 'n' :
		print('''

	 LET'S GET YOU SIGNED UP

	 ''')

		name = str(input('Please enter your USER NAME > '))
		passw = str(input('Please enter a password for your Botnet account >'))
		crs.execute("select name from user where name like %s",(name))
		res = crs.fetchone()
		if name != res :
			print('Username Already Taken. Please Try again ( type exit to exit )')

		elif name == res:

			crs.execute("insert into user values %s",(name, passw))
			connection.commit()
			print("account creation successful")
			mainRun()
			break
