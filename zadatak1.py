broj = int(input("Molim vas unesite broj: "))
broj2 = int(input("Molim vas unesite broj: "))
broj3 = int(input("Molim vas unesite broj: "))

print("Unijeli ste brojeve {0}, {1} i {2}.".format(broj, broj2, broj3))

#Provjera tri broja:
#maxBroj = broj
#if broj2 > broj and broj2 > broj3:
#    maxBroj = broj2
#elif broj3 > broj and broj3 > broj2:
#    maxBroj = broj3
#elif broj > broj2 and broj > broj3:
#    maxBroj = broj3
#print(maxBroj)

brojevi = [broj, broj2, broj3]
maxBroj = broj

brojevi2 = { 1:broj, 2:broj2, 3:broj3}

#Provjera tri broja na drugačiji način:
for i in brojevi:
    i > maxBroj
    maxBroj = i

maxBroj2 = brojevi2[1]

#Korištenjem for petlje
for i in brojevi2:
   brojevi2[i] > maxBroj2
   maxBroj2 = brojevi2[i]

#Printam korisniku:
print("Max broj 2: ", maxBroj2)
print("Max broj:" , maxBroj)
print("Korištenjem MAX funkcije: ", max(brojevi))

# / normalno dijeljenje
# // ostavlja ostatak
# /// modulo operator