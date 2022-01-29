import math
print("       ITS A QUARDRATIC EQUATION SOLVER\n")
print("       MADE BY SURAJ\n\n")
print(" Equation is likely to be -  ax2+bx+c\n")
s=str(input("Give Its UNIT -     "))
a=float(input("Give a -  "))
b=float(input("Give b -  "))
c=float(input("Give c -  "))
d=math.pow(b,2)-(4*a*c)
h=round(d)
i=math.fabs(h)
j=round(i)
e=math.sqrt(j)
f=(-b+e)/2
g=(-b-e)/2
print(f     ,"and",    g)
if(g<0):
  print("So positive VALUE OF",s,"is =",f)
elif(g>0):
  print("So positive VALUE OF",s,"is =",g)
else:
  print(f,g)
