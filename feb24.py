'''#P1.Iterate 0 to 10 using for loop, do the same using while loop.
a=range(0,11)
for i in a:
    print(i)
#from while loop
b=0
while(b<11):
    print(b)
    b=b+1

#P2.Iterate 10 to 0 using for loop, do the same using while loop.
b=range(10,-1,-1)
for i in b:
    print(i)
#form while loop
d=10
while(d>-1):
    print(d)
    d=d-1

#Write a loop that makes seven calls to print(), so we get on the output the following triangle:
a=range(1,8) 
for i in a:
    for j in a:
        if j<=i:
             print("#",end=" ")
        else:
            print(" ",end="")
    print()  
  
#Use nested loops to create the following:
b=range(1,9)
for i in b:
    for j in b:
        print("#",end="")
    print()

#Q5Print the following pattern:
for i in range(0,11):
    print(i,"x",i,"=",i*i)

#Q7Use for loop to iterate from 0 to 100 and print only even numbers
print("even number is:")
for i in range(0,101):
    if(i%2==0):
        print(i,end=" ")
#Q8Use for loop to iterate from 0 to 100 and print only odd numbers
print("odd number is:")
for i in range(0,101):
    if(i%2!=0):

#Q9Use for loop to iterate from 0 to 100 and print the sum of all numbers.   
sum=0
for i in range(0,101):
    sum=sum+i
print(sum)
'''


