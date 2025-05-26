from sympy import Symbol, factor, expand

x = Symbol('x')
y = Symbol('y')
bieuthuc = x**3 - y**3
print("factor(bieuthuc) =", factor(bieuthuc))
bieuthuc2 = (x - y)*(x**2 + x*y + y**2)
print("expand(bieuthuc2) =", expand(bieuthuc2))
print("expand(x**3 - y**3) =", expand(x**3 - y**3))
z = Symbol('z')
bieuthuc3 = x + y + z
print("bieuthuc3 =", bieuthuc3)
