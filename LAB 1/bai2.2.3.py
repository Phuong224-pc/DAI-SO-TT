from sympy import Symbol
x = Symbol('x')
y = Symbol('y')
bieuthuc = x*x - x*y + y*y
print("bieuthuc =", bieuthuc)  
giatri = bieuthuc.subs({x: 3, y: 2})
print("giatri =", giatri) 
print("x =", x)  
print("y =", y)  
