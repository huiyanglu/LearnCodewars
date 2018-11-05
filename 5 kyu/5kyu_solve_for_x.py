def solve_for_x(equation):
    for x in range(-1000,1001):
        if eval(equation.replace('=','==')):
            return x

print(solve_for_x('2*x+1=5'))