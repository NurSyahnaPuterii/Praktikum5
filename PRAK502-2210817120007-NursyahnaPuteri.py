def hitung (nilai1, nilai2) :
    nilai1= int (nilai1) 
    nilai2 = int (nilai2)
    return nilai1-nilai2
def mutlak (angka) :
    angka = int (abs(angka))
    return abs (angka)

a, b, c, d = map (int, input ().split ())
hasil = hitung (a, c) + hitung (b, d)
print (mutlak(hasil))