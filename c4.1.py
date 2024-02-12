# Write a program to print given number is armstrong number or not.

def arm(n):
    s=0
    while n!=0:
        r=n%10
        s=s+(r*r*r)
        n=n//10
    return s
t=int(input())
for i in range(t):
    n=int(input())
    u=arm(n)
    if(u==n):
        print('Armstrong')
    else:
        print('Not an Armstrong')
        
