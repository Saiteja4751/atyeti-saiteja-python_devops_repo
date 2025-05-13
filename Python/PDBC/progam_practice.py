'''
#prime number blw the range
start=int(input())
end=int(input())
for i in range(start,end+1):
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            break
    else:
        print('the prime is',i)
'''


#sum of square of  first n nutural numbers
'''sum1=0
n=int(input())
for i in range(1,n+1):
    sum1=sum1+i**2
print(sum1)'''


#sum of the square of the number
'''from functools import reduce5
n=int(input())
res= reduce(lambda x,y:x+y*y ,range(1,n+1),0)

print(res)'''


'''
left roation
l=[1,2,3,4,5,6]
r=7
k=l[-r:]+l[0:-r]
print(k)

right rotation
l=[1,2,3,4,5,6]
r=2
k=l[r:]+l[0:r]
print(k)
'''