x=int(input("enter number"))
y=x%10
x=x//10
z=x%10
x=x//10
rev=y*100+z*10+x
print(rev)
