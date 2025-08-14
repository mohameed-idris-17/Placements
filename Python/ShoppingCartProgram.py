products = list(map(str, input().split(" ")))
print(products)
while(True):
    x = str(input())
    if(x=='a'):
      products.append(str(input()))
    elif(x=='r'):
       i = str(input())
       products.remove(i)
    elif(x=='g'):
        
        products[str(input())]
    else:
       break
print(products)

