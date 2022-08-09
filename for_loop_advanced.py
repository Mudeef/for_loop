testing-----------------------------------------------------------

num=12345
sum=0
for i in range(len(str(num))):  #convert string and calculate length
    temp=num%10   #get last value
    num=num//10   #remove last value
    print(num)
    sum+=temp    #
print(sum)
#
