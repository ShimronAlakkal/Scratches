# for the users account in BOTNET  library
import mysql.connector as mc
dbs = mc.connect(host='localhost',user='root',passwd='qwertyuiopasdfghjkl')
crs = dbs.cursor()
print('''

    ########\  ##     ##         ##
    ##     ##  ##     ##/####\   ##
    ##     ##  ####   ##/   ##   ####
    ########/  ####   ##    ##   ####
    ########\  ##     ##    ##   ##
    ##     ##  ##     ##    ##   ##
    ##     ##  #####  ##    ##   #####
    ########/  \####  ##    ##   \#### 

    ''')



while 1:
    if val ==1:    # list displaying
        print("ID  |     Book Name          |  Qty") 
        crs.execute("select id,book,qty from books ")
        for i in crs:
            print(i)
        mainRun(opt())
    elif val == 2 :
        print()# list altering 
        print('we have only the below books left ...')
        print()
        print("ID  |     Book Name          |  Qty")
        crs.execute("select id,book,qty from books ;")
        for i in crs:
            print(i)
        print()
        ask_b = int(input('which book/books do you want to buy ? (enter the  book id)'))
        crs.execute ("select book,qty from books where id ="+str(ask_b))
        for i in crs :
            print(i)
        print()
        print('we only have the above quantity for the selected book  ...')
        ask_n = int(input("how many do you want to buy "))
        cnfrm = input('can we confirm your order ? (y/n)')

        if cnfrm=='y':
            crs.execute ("select book,qty from books where id ="+str(ask_b))
            for i in crs :
                if i[1] - ask_n < 0 :
                    print('Your order will be modified to match the stock')
                    ask_n = i[1]
            print()
            print('ORDER PLACED SUCCESFULLY')
            print()
            crs.execute('update books set qty = qty-'+str(ask_n)+' where id='+str(ask_b))
            print('thank you for your puchase from BOTNET ')
            dbs.commit()
        mainRun(opt())


                
    elif val == 3 :        # list deleting 
        c_ask = input('do you want to cancel your order ? (y/n)')
        if c_ask == 'y':
            crs.execute("select id,book from project ;")
            for i in crs:
                print(i)
                print()
            sk = input('enter the id of the book to cancel order >>>  ')
            y = input('are you sure you want to cancel the order ? (y/n)')
            y2= str(input(' how many books did you order ? ... '))
            print()
            if y=='y':
                crs.execute('update books set qty=qty+'+y2+' where id ='+str(sk)+';')
                dbs.commit()
                print('order cancelled  ...')
                mainRun(opt())

    elif val ==4:
        print('logging out ')
        exit()
        break
