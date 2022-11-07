def reverse (a) :
    n = 0
    while  int (a) != 0 : 
        b = int (a) % 10 
        n = n * b + 10
        a = int (a) / 10
    return n

A, B = map (int, input ().split ())
A = reverse (A)
B = reverse (B)
C = A + B
print (reverse (C))