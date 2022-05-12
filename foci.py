from operator import indexOf
import random
golokA= []
golokB = []

print("1. feladat - Eredmények:")
print("")
for i in range(5):
    golA = random.randint(0, 5)
    golB = random.randint(0, 5)
    print(str(i + 1) + ". forduló: " + str(golA) + ":" + str(golB))
    golokA.append(golA)
    golokB.append(golB)

print("")
print("2. feladat")
osszesen=sum(golokA) + sum(golokB)
print(round(osszesen/5, 1))


print("3. feladat")

gyozelmek= [0,0,0,0,0]
for i in range(5):
    if golokA[i]<golokB[i]:
        gyozelmek[i]="V"
    elif golokA[i]>golokB[i]:
        gyozelmek[i]="H"
    else:
        gyozelmek[i]="D"

print(gyozelmek)

h=0
v=0
d=0

for sor in gyozelmek:
    if sor=="H":
        h+=1
    if sor=="V":
        v+=1
    if sor=="D":
        d+=1

if h>v:
    print("A hazai csapat győzött többször.")
elif h<v:
    print("A vendég csapat győzött többször.")  
else:
    print("A két csapat ugyanannyiszor győzött.")  


print("4. feladat")

if d>0 :
    print("Volt döntetlen mérkőzés.")
else:
    print("Nem volt döntetlen mérkőzés.")

print("5. feladat - Hazai gyozelmek:")

for i in range(5):
    if gyozelmek[i]=="H":
        print(f"{i+1}. fordulo")

print("6. feladat")

kulonbseg =[]
for i in range(5):
    kulonbseg.append(abs(golokA[i]-golokB[i]))

print(kulonbseg)

print(f"A legnagyobb golkulonbseget a(z) {kulonbseg.index(max(kulonbseg))+1} forduloban ertek el, ami {max(kulonbseg)} gol volt.")