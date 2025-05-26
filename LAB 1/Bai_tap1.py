from sympy import Symbol, solve


x = Symbol('x')


bieuthuc = x + 3 - 5
ketqua = solve(bieuthuc)
print(ketqua)  

bieuthuc2 = x**2 + 3 - 5
nghiemx = solve(bieuthuc2)
print(nghiemx)      
print(nghiemx[0])   
print(nghiemx[1])   