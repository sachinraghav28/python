x=int(input("enter number"))
n=x
y=x%10
x=x//10
z=x%10
x=x//10
rev=y*100+z*10+x
if rev==n:
  print(rev)
else:
    print("not palendrom")
