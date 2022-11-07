def MaxBilangan (a, b, c, d):
    a = int (a); b = int (b); c = int (c); d = int (d)
    if a > b and a > b and a > b :
        return a
    elif b > a and b > c and b > d :
        return b
    elif c > a and c > b and c > d:
        return c
    elif d > a and d > b and d > c: 
        return d
a, b, c, d = map (int, input ().split ())
hasil = MaxBilangan (a, b, c, d)
print (hasil)