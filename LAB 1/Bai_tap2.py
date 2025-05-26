from sympy import Symbol, solve, I
x = Symbol('x')

ptb2_1 = x**2 + 9*x + 8
nghiem1 = solve(ptb2_1, dict=True)
print("Nghiệm phương trình x^2 + 9x + 8 = 0:")
print(nghiem1)

ptb2_2 = x**2 + x + 10
nghiem2 = solve(ptb2_2, dict=True)
print("\nNghiệm phương trình x^2 + x + 10 = 0:")
print(nghiem2)
