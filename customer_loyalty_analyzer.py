# Unos imena i provera broja reci
while True:
    ime_kupca = input("Molimo Vas da unesete ime i prezime kupca: ")
    rec = ime_kupca.split()
    
    if len(rec) >= 2:
        ime = rec[0]
        prezime = " ".join(rec[1:])
        break
    else:
        print("Greška! Neophodno je uneti ime i prezime.")
        

# Koliko je bilo kupovina i njihovi iznosi
broj_kupovina = int(input("Uneti broj ostvarenih kupovina\
u proteklih godinu dana: "))

lista_cena = [0] * broj_kupovina

for iznos in range(broj_kupovina):
    cena = float(input(f"Unesite iznos u RSD za {iznos + 1}. kupovinu: "))
    
    lista_cena[iznos] = cena


# Ukupan iznos
ukupna_potrosnja = sum(lista_cena)


# Koliko je bilo velikih kupovina
broj_velikih_kupovina = 0

for iznos in range(broj_kupovina):
    if lista_cena[iznos] > 10000:
        broj_velikih_kupovina += 1


print(f"Poštovani/a {ime}, ukupno ste potrošili {ukupna_potrosnja}\
RSD, od toga je bilo {broj_velikih_kupovina} kupovina iznad 10 000 RSD.")


# Da li je kupac VIP ili STADARD
if ukupna_potrosnja > 100000 and broj_kupovina > 10:
    status = "VIP" 
    print(f"Korisnik {ime} {prezime}, ima status VIP korisnika!")
else:
    status = "STANDARD"
    print(f"Korisnik {ime} {prezime}, ima status STANDARD korisnika!")

# Koliko dobijaju popusta na osnovu statusa
cena_novog_proizvoda = float(input(f"Poštovani/a {ime} \
unesite cenu artikla koji želite da kupite: "))

if status == "VIP":
    popust_vip = cena_novog_proizvoda * (10 / 100)
    cena_sa_popustom_vip = cena_novog_proizvoda - popust_vip
    print(f"Cena artikla iznosi {cena_sa_popustom_vip} RSD.")

else:
    popust_standard = cena_novog_proizvoda * (5 / 100)
    cena_sa_popustom_standard = cena_novog_proizvoda - popust_standard
    print(f"Cena artikla iznosi {cena_sa_popustom_standard} RSD.")
