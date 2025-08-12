while(True):
    num = int(input())
    if num==0:
        break
    elif(num<0):
        print("Negative number skipped")
    elif num>100:
        print("Number too large, exiting")
        break
    else:
        P = False
        for i in range(2,num):
            if(num%i==0):
                print(f"{num} is not a prime")
                P = True
                break 
        if not P:
            print("prime")


                