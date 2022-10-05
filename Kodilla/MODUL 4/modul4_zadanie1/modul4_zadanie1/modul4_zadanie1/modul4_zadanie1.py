def is_palindrom(keyword):
    '''
    Funkcja sprawdza czy podane słowo jest palindromem.
    Przyjmuje SŁOWO podane przez użytkownika jako zmienną.
    Przetwarza SŁOWO na składające się z małych liter.
    Tworzy nową zmienną z odwróconą kolejnością SŁOWA.
    Konwertuje stringi na listy, składające się z liter tworzących SŁOWO.
    Przyrównuje obie listy i w zależności czy są identyczne wypisuje wynik.

    '''
    keyword = keyword.casefold()
    if list(keyword) == list(reversed(keyword)):
        print("to palindrom")
    else:
        print("nie jest palindromem")

keyword = input('Słowo: ')
is_palindrom(keyword)