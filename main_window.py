# for the users account in BOTNET  library
import mysql.connector as mc
import 
dbs = mc.connect(host='localhost',user='root',passwd='qwertyuiopasdfghjkl')
crs = dbs.cursor()

def productView():
	print()
	print("ID  |     Book Name          |  Qty") 
	crs.execute("select id,book,qty from books ")
	for i in crs:
		print(i)


def productPurchase():
	print()# list altering 
	print('BOOKS THAT WE HAVE AT BOTNET ...')
	print()

	productView()

	print()

	ask_b = int(input('which book do you want to buy ? (enter the  book id)'))
	crs.execute ("select book,qty from books where id ="+str(ask_b))
	for i in crs :
		print('Book : ',i[0],' |  Qty : ',i[1])
	print()

	ask_n = int(input("how many do you want to buy "))
	cnfrm = input('can we confirm your order ? (y/n)')

	if cnfrm == 'y':
		crs.execute ("select book,qty from books where id ="+str(ask_b))		
		for i in crs:
			if i[1] - ask_n <0: #negative qty is avoided
				print('')
				print('''Since your order contains a greater qty than that in the stocks,
your order will be modified to match the stocks''')
				ask_n -= -1*(i[1]-ask_n) 
				print()
				print('altered qty for buy = ',ask_n)
				print()
				crs.execute('update books set qty = qty-'+str(ask_n)+' where id='+str(ask_b))
				print('thank you for your puchase from BOTNET ')
				dbs.commit()
				mainView(1)
			else:
				crs.execute('update books set qty = qty-'+str(ask_n)+' where id='+str(ask_b))
				dbs.commit()
				mainView(1)
	else:
		print()
		mainView(1)


def orderCancel():
	c_ask = input('do you want to cancel your order ? (y/n)')
	if c_ask == 'y':

		print()
		productView()
		print()
		sk = input('enter the id of the book to cancel order >>>  ')
		y2= str(input(' how many books did you order ? ... '))
		y = input('are you sure you want to cancel the order ? (y/n)')
		print()
		if y=='y':
			crs.execute('update books set qty=qty+'+y2+' where id ='+str(sk)+';')
			dbs.commit()
			print('order cancelled  ...')
			mainView(1)
		else:
			mainView(1)



def mainView(val):
	if val != 0:

		print('''

			1. View books that we have 
			2. Purchase a book
			3. cancel your order 
			4. Logout

			''')
		opt = int(input('''
	>>>
			'''))
		if opt == 1:
			productView()
			mainView(1)

		elif opt == 2:
			productPurchase()

		elif opt == 3:
			orderCancel()

		elif opt == 4:
			exit()
	else:
		print('''

			WELCOME TO BOTNET

     ########\  ##     ##         ##
     ##     ##  ##     ##/####\   ##
     ##     ##  ####   ##/   ##   ####
     ########/  ####   ##    ##   ####
     ########\  ##     ##    ##   ##
     ##     ##  ##     ##    ##   ##
     ##     ##  #####  ##    ##   #####
     ########/  \####  ##    ##   \#### 

    ''')


		crs.execute('use botnet')
		mainView(1)

