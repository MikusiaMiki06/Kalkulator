import kalkulator

print("Jeśli chcesz obliczyć objętość donuta wybierz '1'.")
print("Jeśli chcesz obliczyć pole całkowite kuli wybierz '2'.")
print("Jeśli chcesz obliczyć objętość piramidy wybierz '3'.")
print("Jeśli chcesz obliczyć twierdzenie pitagorasa wybierz '4'.")
print("Jeśli chcesz obliczyć poziom natężenia dźwięku wybierz '5'.")
print("Jeśli chcesz obliczyć deltę wybierz '6'.")
print("Jeśli chcesz obliczyć pole sześciokąta foremnego wybierz '7'.")

while True:
    inp = input()
    if inp == "1":
        print('r = ')
        r = float(input())
        print('R = ')
        R = float(input())
        od = kalkulator.objetosc_donuta(r, R)
        print("Wynik: ")
        print(od)
    elif inp == "2":
        kalkulator.pole_calkowite_kuli()
    elif inp == "3":
        print('a = ')
        a = float(input())
        print('h = ')
        h = float(input())
        op = kalkulator.objetosc_piramidy(a,h)
        print("Wynik: ")
        print(op)
    elif inp == "4":
        print('a = ')
        a = float(input())
        print('b = ')
        b = float(input())
        tp = kalkulator.twierdzenie_pitagorasa(r,h)
        print("Wynik: ")
        print(tp)
    elif inp == "5":
        kalkulator.poziom_natezenia_dzwieku()
    elif inp == "6":
        kalkulator.delta()
    elif inp == "7":
        kalkulator.pole_sześciokąta_foremnego()

