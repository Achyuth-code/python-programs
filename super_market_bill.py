# from datetime import datetime

# name=input("Enter the name:")

# list='''
# rice       rs 20/kg
# sugar      rs 30/kg
# maida      rs 40/kg
# atta flour rs 34/kg
# maggie     rs 50/kg
# corn flour rs 35/kg
# salt       rs 20/kg
# nuts       rs 34/kg
# dry fruits rs 500/kg
# '''

# price=0
# pricelist=[]
# totalprice=0
# finalamount=0
# ilist=[]
# qlist=[]
# plist=[]

# items={"rice":20,"sugar":30,"maida":30,"atta flour":34,"maggie":50,"corn flour":35,"salt":20,"nuts":34,"dry fruits":500}
# option=int(input("for list items press 1"))
# if option==1:
#     print(list)
# for i in range(len(items)):
#     inp1=int(input("if you want to buy press 1 or 2 for exit"))
#     if inp1==2:
#         break
#     if inp1==1:
#         item=input("Enter your items:")
#         quantity=int(input("Enter your quantity:"))
#         if item in items.keys():
#             price=quantity*(items[item])
#             pricelist.append((item,quantity,items,price))
#             totalprice+=price
#             ilist.append(item)
#             qlist.append(quantity)
#             plist.append(price)
#             gst=totalprice*5/100
#             Finalamount=gst+totalprice
#         else:
#             print("sorry you entered item is not available")
#     else:
#         print("you entered wrong number")
#     inp=input("can i bill the items yes or no:")
#     if inp=='yes':
#         pass
#         if Finalamount!=0:
#             print(25*"=","Achyuth supermarket",25*"=")
#             print(28*"","Pulivendula")
#             print("Name:",name,30*" ","Date:",datetime.now())
#             print("sno",5*" ","items",3*" ","quantity",3*" ","price")
#             for i in range(len(pricelist)):
#                 print(i,8*' ',1*' ',ilist[i],1*' ',qlist[i],6*" ",plist[i])
#                 print(50*" ", 'totalamount:','rs',totalprice)
#                 print("gst amount",50*" ",'rs',gst)
#                 print(75*"-")
#                 print(50*" ",'finalamount:',finalamount)
#                 print(75*"-")
#                 print(20*" ","Thanks for visiting")
#                 print(75*"-")
                
                
                
        
