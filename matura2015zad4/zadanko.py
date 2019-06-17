jed = 0
zer = 0
counter = 0
przez_2 = 0
przez_8 = 0
minn = 123124124
maxx = 0
wiersz_maly = 0
wiersz_duzy = 0
w = 0
file = open(".\\2015zad4\liczby.txt")
for line in file:
    w += 1
    line = line.strip()
    for i in line:
        if int(i) == 1:
            jed +=1
        else:
            zer +=1
    if zer > jed:
        counter +=1
    jed = 0
    zer = 0

    a = len(line)
    if line[a-1] == "0":
        przez_2 += 1
    if line[a-1] == line[a-2] == line[a-3] == "0":
        przez_8 += 1
    a = minn
    b = maxx
    minn = min(minn, int(line, 2))
    maxx = max(maxx, int(line, 2))
    if a != minn:
        wiersz_maly = w
    if b != maxx:
        wiersz_duzy = w
#----------------------------------------------#
print("Odpowiedz zad 4.1 : " + str(counter))
print("Odpowiedz zad 4.2 : podzielnych przez 2 jest: " + str(przez_2) + " podzielnych przez 8 jest: " + str(przez_8))
print("Odpowiedz zad 4.3 : najwieksza liczba jest w wierszu: " + str(wiersz_duzy) + " najmniejsza w wierszu : " + str(wiersz_maly))
