# Write a program to print given number is an armstrong number or not using classes and objects.

class Solution:
    def arm(self,n):
        s=0
        t=n
        while n!=0:
            r=n%10
            s=s+(r*r*r)
            n=n//10
        if(s==t):
            return 1
        else:
            return 0
t=int(input())
for i in range(t):
    n=int(input())
    obj=Solution()
    u=obj.arm(n)
    if u==1:
        print('Armstrong')
    else:
        print('Not an Armstrong')
 
