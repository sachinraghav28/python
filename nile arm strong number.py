x=int(input("enter number"))
y=x%10
x=x//10
z=x%10
x=x//10
rev=y*y*y+z*z*z+x*x*x
print(rev)
