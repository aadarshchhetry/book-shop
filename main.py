import sqlite3
import os

if __name__ == '__main__':
    data = sqlite3.connect("book.db")
    curdata = data.cursor()
    
    try:
        repeat = 'y'
        while(repeat == 'y' or repeat == 'Y'):
                    choice = int(input("Welcome to Library\n1.Add book to library\n2.Issue book to customer\n3.Exit\nEnter choice:"))
                    data = sqlite3.connect("book.db")
                    curdata = data.cursor()
                    if choice == 1:
                        
                        bname = input("Enter book name: ").title()
                        try:
                            curdata.execute('''SELECT Bname FROM libook WHERE Bname=? ;''',(bname,))
                            libook = curdata.fetchone()
                            libook =str(libook[0])
                            qtybook = int(input("Enter number of book added: "))
                            curdata.execute('''SELECT quantity FROM libook WHERE Bname=?;''',(bname,))
                            lqty = curdata.fetchone()
                            newqty = lqty[0]+qtybook
                            curdata.execute('''UPDATE libook
                                                        SET quantity=?
                                                        WHERE Bname=?;''',(newqty, bname,))
                        except:
                            bauthor = input("Enter the author name: ")
                            bprice = float(input("Enter price of book: "))
                            qtybook = int(input("Enter number of book added: "))
                            curdata.execute('''INSERT INTO libook(quantity, Bname, Bauthor, Bprice)
                                            VALUES(?,?,?,?);''',(qtybook, bname, bauthor, bprice))
                            
                    elif choice == 2:
                        try:
                            
                            cbook = input("Enter the name of the book you are looking for: ").title()
                            curdata.execute('''SELECT Bname FROM libook WHERE Bname=? ;''',(cbook,))
                            libook = curdata.fetchone()
                            libook = libook[0]
                            print('BOOK FOUND!')
                            
                            if cbook == libook:
                                curdata.execute('''SELECT quantity FROM libook WHERE Bname=?;''',(cbook,))
                                lqty = curdata.fetchone()
                                lqty = lqty[0]
                                print(f'Quantity of book {cbook}: {lqty}')
                                cqty = int(input("Enter number of quantity you want to take out: "))
                                
                                if cqty <= lqty:
                                    newqty = str(lqty-cqty)
                                    curdata.execute('''UPDATE libook
                                                        SET quantity=?
                                                        WHERE Bname=?;''',(newqty, cbook,))
                                    curdata.execute('''SELECT Bprice FROM libook WHERE Bname=?;''',(cbook,))
                                    price = curdata.fetchone()
                                    price = price[0]
                                    price *= cqty
                                    print("Total price = Rs",price)
                                    print('Book checkout success!')
                                    
                                else:
                                    print(f'Book quantity is less than you required try small number than {lqty}: ')
                                    continue
                                
                            else:
                                print("Sorry This book is currently not available in our library")
                                
                        except:
                            print("Book not found")

                            
                    else:
                        print("No valid choice")
                    data.commit()
                    repeat = input("Do you want to continue ? (Y/N)")
                    os.system('cls')
    except:
        data.rollback()
        print("Invalid value please try again next time")
    data.close()
