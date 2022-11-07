def MaxBilangan (e, f, g, h):
    e = int (e); f = int (f); g = int (g); h = int (h)
    if e > f and e > g and e > h :
        return e
    elif f > g and f > h and f > e :
        return f
    elif g > h and g > e and g > e:
        return g
    elif h > e and h > f and h > g : 
        return h
a, b, c, d = map (int, input ().split ())
hasil = MaxBilangan (a, b, c, d)
print (hasil)