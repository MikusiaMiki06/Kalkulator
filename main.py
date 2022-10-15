import kalkulator

print("Objętość donuta - 1")
print("Pole całkowite kuli - 2")
print("Objętość piramidy - 3")
print("Twierdzenie pitagorasa - 4")
print("Poziom natężenia dźwięku - 5")
print("Delta - 6")
print("Pole sześciokąta foremnego - 7")

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

