from sympy import Symbol, solve

x = Symbol('x')
y = Symbol('y')


pt1 = 2*x + 3*y - 12
pt2 = 3*x - 2*y - 5

nghiem = solve((pt1, pt2), dict=True)
print("Nghiệm của hệ phương trình là:", nghiem)

nghiem = nghiem[0]

kq1 = pt1.subs({x: nghiem[x], y: nghiem[y]})
kq2 = pt2.subs({x: nghiem[x], y: nghiem[y]})

print("Thay nghiệm vào pt1:", kq1)
print("Thay nghiệm vào pt2:", kq2)
