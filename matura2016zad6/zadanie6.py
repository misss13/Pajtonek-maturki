def fyszr(slo : str, k : int):
    a = 1
    wyn = ""
    if k < 0:
        a = -1
    if abs(k) > 26:
        k = abs(k) % 26
    k *= a
    if(slo.isupper()):
        for i in slo:
            z = ord(i) + k
            if z >= 90:
                lit = ((z % 90) + 65)
            elif z < 65:
                while z < 65:
                    z += 26
                lit = z
            else:
                lit = z
            wyn += chr(lit)
    return wyn

def jed():
    with open("dane_6_1.txt") as file, open("wyniki_6_1.txt", 'w' ) as wyn:
        for line in file:
            line.strip()
            a = fyszr(line, 107)
#            print (str(a))
            wyn.write(str(a)+"\n")

def dwa():
    with open("dane_6_2.txt") as file, open("wyniki_6_2.txt", 'w') as wyn:
        for line in file:
            try:
                slo,klu = line.strip().split()
                a = fyszr(slo, -int(klu))
#               print(a)
                wyn.write(a + "\n")
            except:
                print("cos zle")
def trzy():
    with open("dane_6_3.txt") as file, open("wyniki6_3.txt", 'w') as wyn:
        q = 0
        for line in file:
            try:
                a , b = line.strip().split()
                c = 90 - ord(a[0])
                if string(fyszr(a, abs(c))) != b:
                    print(a + "\n" + b)
                    wyn.write(a + "\n" + b)
            except:
                q += 1
if __name__ == '__main__':
    print(fyszr("SMIGIELSKI",13))
    jed()
    dwa()
    trzy()
