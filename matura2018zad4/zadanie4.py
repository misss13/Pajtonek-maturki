from collections import Counter

def wczytaj( nazwa ):
    list = []
    with open(nazwa) as file:
        for line in file:
            list.append(line.strip())
        return list

def pierw(lista):
    wyn = ""
    for i in range(39,1000,40):
        wyn += lista[i][9]
    return wyn

def drug(lista):
    for i in lista:
        maxx = 0
        line = ""
        count = Counter(i)
        if maxx < (len(count)):
            maxx = len(count)
            line = i
    return line, maxx

def trzec(lista):
    for i in lista:
        count = Counter(i)
        sorted(count.keys())
        #print(count)
        a = ord((list(count.keys())[0]))
        b = ord((list(count.keys())[len(list(count.keys()))-1]))
        val = abs(a - b)
        if(val <= 10):
            print(i)

if __name__ == '__main__':
    lis = wczytaj("sygnaly.txt")
    print("zad 4.1: " + pierw(lis))
    print("zad 4.2: ")
    print(drug(lis))
    print("zad 4.3: ")
    trzec(lis)
