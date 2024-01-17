import sympy as sp
def my_tailor(f,N):
    x0 = sp.symbols('x0')
    result = f.subs(x, x0)
    f_diff = f.diff()
    div = 1
    for i in range(0, N):
        result = result + f_diff.subs(x, x0)*(x-x0)**(i+1) / div
        div = div * (i+2)
        f_diff = f_diff.diff()

    return(result + sp.O((x-x0)**N))
if __name__ == "__main__":
    x,x0=sp.symbols('x x0')
    my_f=x**2+sp.sin(x)*sp.cos(x)+4*x**3
    #my_f=x**4+x**3+x**2
    print(my_tailor(my_f,3))
