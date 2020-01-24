n2000 = 0
n500 = 0
n200 = 0
n100 = 0
CoUnT = 3
while(CoUnT>0):
    if(CoUnT == 1):
        print("\nLast Attempt.")
    AmoUnT = int(input("Enter the amount : "))
    TmP = AmoUnT
    
    if(((AmoUnT%100 != 0)|(AmoUnT==0))&(CoUnT > 1)):
        print("Amount entered cannot be dispensed.\nEnter in the multiple of hundreds.")
        CoUnT -=1
    
    elif((AmoUnT%100 != 0)|(AmoUnT==0)&(CoUnT == 1)):
        print("Amount entered cannot be dispensed.")
        CoUnT -=1
        
    elif(AmoUnT > 10000):
        print("Amount limit excedded.")
        CoUnT -= 1
        
    else :
        while(AmoUnT):
            if(AmoUnT/2000>=1):
                n2000 = int(AmoUnT/2000)
                AmoUnT = AmoUnT % 2000
            elif(AmoUnT/500 >= 1):
                n500 = int(AmoUnT/500)
                AmoUnT = AmoUnT % 500
            elif(AmoUnT/200 >= 1):
                n200 = int(AmoUnT/200)
                AmoUnT = AmoUnT % 200
            elif(AmoUnT/100 >= 1):
                n100 = int(AmoUnT/100)
                AmoUnT = AmoUnT % 100
            
        print("Indexing notes for amount "+str(TmP)+" is : \n")
        print("Rs. 2000 : ",n2000)
        print("Rs. 500 : ",n500)
        print("Rs. 200 : ",n200)
        print("Rs. 100 : ",n100)
        break