import math
counter=0
counter1=0
maxx = { "dl":2, "gcd":0, "pier":0}
temp = { "dl":2, "gcd":0, "pier":0}
file = open(".\\2014zad5\liczby.txt")
lista=[]
#-----------------zadanko 4.1 ----------------------------#
for line in file:
    line = line.strip()
    if int(line) % 3 == 0:
        for i in range(13):
            a = 3 ** i
            if int(line) == a:
                counter+=1
            if a > int(line): #nie działało dla int(line) > int(a)
                #print(str(a) + " " + str(line) + "\n")
                break
#-----------------zadanko 4.2 ----------------------------#
    b=0
    for i in line:
        b += math.factorial(int(i))
        if b > int(line):
            break
    if b == int(line):
        counter1+=1
        print(line)
#-----------------zadanko 4.3 i jest źle ----------------------------#
    lista.append(int(line.strip()))
file.close()
temp["pier"] = lista[0]
temp["gcd"] = math.gcd(lista[0],lista[1])
for i in range(1,(len(lista)-1)):
    pier = lista[i]
    dru = lista[i+1]
    k = math.gcd(pier,dru)
    if k != 1:
        if k == temp["gcd"]:
            temp["dl"] += 1
        else:
            temp["gcd"] = k
            temp["pier"] = lista[i]
            temp["dl"] = 2
        if maxx["dl"] < temp["dl"]:
            maxx["dl"] = temp["dl"]
            maxx["pier"] = temp["pier"]
            maxx["gcd"] = temp["gcd"]
    else:
        temp["pier"] = lista[i+1]
    #print(str(temp["pier"])  + " " + str(temp["gcd"]) + " " + str(k) + " " + str(temp["dl"]))
    #print(str(maxx["pier"]) + " " + str(maxx["gcd"]) + " " + str(maxx["dl"]) + "\n")
#-----------------zadanka konic---------------------------#
print("odp do zadania 4.1 : " + str(counter))
print("odp do zadania 4.2 : " + str(counter1))
print("odp do zadania 4.2 : " + str(maxx["pier"]) + " " + str(maxx["dl"]) + " " + str(maxx["gcd"]))
