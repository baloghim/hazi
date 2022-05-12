lista = []

while True:
    x=int(input("Egész számokat kérek, kilépés 0-val. :"))
    if x==0:
        break
    else:
        lista.append(x)

print(lista)