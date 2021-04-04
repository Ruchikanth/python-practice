date=input("Enter date in format dd/mm/yyyy ")
dd,mm,yy=date.split('/')
dd=int(dd)
if (mm=='1' or mm=='3' or mm=='5' or mm=='7' or mm=='8' or mm=='10' or mm=='12'):
    if(dd<0 or dd>=31):
        print('date is invalid')
    else:
        print("date is valid")    
elif (mm=='4' or mm=='6' or mm=='9' or mm=='11'):
    if(dd<0 or dd>=30):
        print("date is invalid")
    else:
        print("date is valid")
elif (mm=='2'):
    if(int(yy)%4==0 and (dd>29)):
        print("date is invalid feb")
    elif(int(yy)%4!=0 and (dd>28)):
       print("date is invalid feb")
    else:
        print("date is valid 2")       
else:
    print("invalid date")
    
          
