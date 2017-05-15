def repeated(f):
    def g(n,x):
        return f(x) if n==1 else g(n-1,f(x))
    return g
