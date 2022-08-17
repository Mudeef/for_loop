list=[1,2,3,4,5,6,7,8,9,10]
def add(list):
    sum = 0
    for i in list:
        sum=sum+i
    return sum
result=add(list)
print(result)
def product(list):
    sum=1
    for i in list:
        sum=sum*i
    return  sum
result=product(list)
print(result)
def square(list):
    new=[]
    for i in list:
        new.append(i*i)
    return new
result=square(list)
print(result)