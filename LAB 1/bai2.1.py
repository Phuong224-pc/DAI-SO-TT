from sympy import Symbol
x = Symbol('x')
f = x + x + x + 2
print("f =", f) 
a = Symbol('Noi')
b = Symbol('Chim')
expr = 3*b + 7*a
print("Biểu thức 3*b + 7*a =", expr)  
# 3. Truy xuất tên của Symbol
print("Tên của a:", a.name) 
print("Tên của b:", b.name)   
# 4. Phép toán với nhiều symbol
y = Symbol('y')
s = x*y + y*x
print("s =", s) 
# 5. Phép nhân biểu thức
p = x*(x + 2*x)
print("p =", p)  
# 6. Biểu thức chưa khai triển
p = (x + 2)*(y + 3)
print("p =", p) 
# Biểu thức phức tạp hơn chưa khai triển
p = (x + 2)*(y + 3) + (x + 2)*(x - 3)
print("p =", p)  
# 7. Biểu thức tự động rút gọn
p = x*(-x + 2*x - x)
print("p =", p) 
# 8. Khai triển biểu thức bằng lệnh expand()
p = (x + 2)*(y + 3)
print("p khai triển:", p.expand())  
