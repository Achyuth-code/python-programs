name="achyuth"
passwords="achyuth143"
user_name=input("enter the user name:")
password=input("enter the password:")
s='''
    1.Credit
    2.debit
    3.mini statement
    4.exit
    '''
Amount=12000
if name==user_name and passwords==password:
    while True:
        print(s)
        option=int(input("enter the option:"))
        if option==1:
            credit_amount=float(input("enter the amount:"))
            print("Amount after credit:",Amount+credit_amount)
        elif option==2:
            debit_amount=float(input("enter the amount:"))
            print("Amount after debit:",Amount-debit_amount)
        elif option==3:
            print("## mini statement ##",Amount)
        elif option==4:
            break
        else:
            print("incorrect")
                        
                        