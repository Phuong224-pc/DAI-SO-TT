from sympy import Symbol, simplify, sin, cos

# Định nghĩa các biến Symbol
x = Symbol('x')
y = Symbol('y')

# Biểu thức đại số
bieuthuc = x**2 - x*y + y**2
print("bieuthuc =", bieuthuc)

# Tình huống 1: x = 3, y = x
giatri1 = bieuthuc.subs({x: 3, y: x})
print("Tình huống 1:", giatri1)  # x**2 - 3*x + 9

# Tình huống 2: x = y, y = 3
giatri2 = bieuthuc.subs({x: y, y: 3})
print("Tình huống 2:", giatri2)  # y**2 - 3*y + 9

# Tình huống 3: y = x, sau đó x = 3
giatri3 = bieuthuc.subs({y: x}).subs({x: 3})
print("Tình huống 3:", giatri3)  # 9

# Ví dụ simplify()
bieuthuc_moi = bieuthuc.subs({x: 1 - y})
print("bieuthuc_moi =", bieuthuc_moi)  # (1 - y)**2 - (1 - y)*y + y**2

dongian = simplify(bieuthuc_moi)
print("Đơn giản hóa:", dongian)  # 1 - y

# Ví dụ về lượng giác và simplify()
bt = sin(x)*cos(y) + cos(x)*sin(y)
bt_moi = simplify(bt)
print("Biểu thức lượng giác đã đơn giản hóa:", bt_moi)  # sin(x + y)
