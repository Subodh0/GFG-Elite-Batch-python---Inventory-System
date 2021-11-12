import json
import time
fd = open("Inventory_Records.json",'r')
js = fd.read()
fd.close()
dct = json.loads(js)

for i in dct.keys():
    print(i,dct[i])

print()
f=True
while(f):
    ui_prod = str(input("Enter Product ID    : "))
    ui_qn   = int(input("Enter the Quantity  : "))
    ui_phone = str(input("Please Enter your phone no. : "))
    ui_email = str(input("Please Enter your email id : "))


    #for i in dct[ui_prod].keys():
    if dct[ui_prod]["Qn"] >=ui_qn:
        print("-"*15)

        print("Name     :" , dct[ui_prod]['Name'])
        print("Price    :" ,dct[ui_prod]['Price'])
        print("Quantity :" ,ui_qn)
        print("-"*15)
        print("Total    :" ,dct[ui_prod]['Price'] * ui_qn)
        print("CGST     :" ,(dct[ui_prod]['Price'] * ui_qn)*.09)
        print("SGST     :" ,(dct[ui_prod]['Price'] * ui_qn)*.09)
        
        print("-"*15)
        print("Sub Total:" ,(dct[ui_prod]['Price'] * ui_qn) + (dct[ui_prod]['Price'] * ui_qn)*.18)
        print("-"*15)
        txn = dct[ui_prod]['Name']+","+ ui_phone+","+ ui_email +","+str(dct[ui_prod]['Price'])+","+str(+ui_qn)+","+str((dct[ui_prod]['Price'] * ui_qn) + (dct[ui_prod]['Price'] * ui_qn)*.18)+","+time.ctime()+"\n"
        dct[ui_prod]["Qn"]=dct[ui_prod]["Qn"]-ui_qn

        
        
    else:
        print("Sorry we don't have the minimum Qn ")
        print("We have only ", dct[ui_prod]["Qn"])
        Q=input("Do you we wish to purchase it ? Press Yes or No ")
        if Q=="Yes" or Q=="yes":
            print("-"*15)
            print("Name     :" , dct[ui_prod]['Name'])
            print("Price    :" ,dct[ui_prod]['Price'])
            print("Quantity :" ,dct[ui_prod]["Qn"])
            print("-"*15)
            print("Total    :" ,dct[ui_prod]['Price'] * dct[ui_prod]["Qn"])
            print("CGST     :" ,(dct[ui_prod]['Price'] * dct[ui_prod]["Qn"])*.09)
            print("SGST     :" ,(dct[ui_prod]['Price'] * dct[ui_prod]["Qn"])*.09)
            print("-"*15)
            print("Sub Total:" ,(dct[ui_prod]['Price'] * dct[ui_prod]["Qn"]) + (dct[ui_prod]['Price'] * dct[ui_prod]["Qn"])*.18)
            print("-"*15)
            txn = dct[ui_prod]['Name']+","+ ui_phone+","+ ui_email +","+str(dct[ui_prod]['Price'])+","+str(dct[ui_prod]["Qn"])+","+str((dct[ui_prod]['Price'] * dct[ui_prod]["Qn"]) + (dct[ui_prod]['Price'] * dct[ui_prod]["Qn"])*.18)+","+time.ctime()+"\n"
            dct[ui_prod]["Qn"]=0
        else:
            print("Thank you :), please visit us again ")

    print()
    print("-"*15)
    print("-"*15)
    for i in dct.keys():
            print(i,dct[i])

            
    js = json.dumps(dct)

    fd = open("Inventory_Records.json",'w')
    fd.write(js)
    fd.close()

    fd=open("Sales.txt","a")
    fd.write(txn)
    fd.close()
    
