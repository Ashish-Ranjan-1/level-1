input_li=[1,2,3,4,5,6,7,8,9]
input_multiple_li=[1,2,8,9,12,46,76,82,15,20,30]
result_dic={}
for i in input_li:
    keys = i 
    temp=[]
    for j in input_multiple_li:
        if j%i==0:
            temp.append(j)
        else:
            continue
    values = len(temp) 
    result_dic[keys] = values
print(result_dic)
