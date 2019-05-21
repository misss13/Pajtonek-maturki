#PR 2014 Zadanie 1.2.W wybranej przez siebie notacji (lista kroków, wybrany język programowania) napiszalgorytm:umieszczającyposzczególne  cyfry  liczby kwtablicy tab_cyfr[]wkolejności odnajmniej do najbardziej znaczącejzwracający liczbę cyfr jej zapisu dziesiętnego.
a = input("Podaj liczbe\n")
b = int(a)
n = len(a)
print(n)
num = list(a)
num.sort()
s=0
print(num)
for i in num:
    s+=(int(i))**n
if b == s:
    print("PRAWDA")
else:
    print("FALSZ")
