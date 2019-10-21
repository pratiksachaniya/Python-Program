def inc(fun):
    def runner(a):
        fun(a+3)
    return runner
@inc
def st(a):
    print(a)

st(10)
