import first

def f():
    print('First:')
    n=first.read_numbers()
    print('Second:')
    s=first.read_numbers()
    F=first.List()
    F._to_list(n)
    S=first.List()
    S._to_list(s)
    Res=first.List()
    Res=F+S
    print('Result:')
    Res.output()
    F.delete()
    S.delete()
    Res.delete()

f()
