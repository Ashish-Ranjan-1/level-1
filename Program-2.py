li=[]
inpu = int(input("Enter the input : "))
if inpu%2==0:
    inpu-=1
else:
    pass
for i in range (inpu):
    itm=(2*i)+1
    li.append(itm)
print(li)    