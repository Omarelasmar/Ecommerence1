h0=int(input("h0="))
v0=int(input("v0="))
t1=int(input("t1="))
t2=int(input("t2="))
g=9.8
h=h0+v0-(1/2*g*(t1**2))
print(h)
v=v0-(g*t1)
print(v)
v=v0-(g*t2)
print(v)