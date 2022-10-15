from math import log10, pi, sqrt


def objetosc_donuta(r, R):
    return 2*pi**2*r**2*R

def pole_calkowite_kuli():
    print('r = ')
    r = float(input())
    pck = 4*pi*r**2
    print("Wynik: ")
    print(pck)

def objetosc_piramidy(a, h):
    return (1/3)*a**2*h

def twierdzenie_pitagorasa(a, b):
    return sqrt(a**2 + b**2)

def poziom_natezenia_dzwieku():
    L = 10**-12
    print('I = ')
    I = float(input())
    pnd = 10*log10(I/L)
    print("Wynik: ")
    print(pnd)

def delta():
    print('a = ')
    a = float(input())
    print('b = ')
    b = float(input())
    print('c = ')
    c = float(input())
    delta = b**2-4*a*c
    print("Wynik: ")
    print(delta)   

def pole_sześciokąta_foremnego():
    print('a = ')
    a = float(input())
    psf = (3*a**2*sqrt(3))/2
    print("Wynik: ")
    print(psf)   






