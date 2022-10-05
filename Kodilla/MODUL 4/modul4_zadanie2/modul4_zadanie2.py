import logging
logging.basicConfig(level=logging.INFO)

'''
Prosty kalkulator który pozwala wykonywać działania na dwóch liczbach.
'''

def calculation_choice(number): #Funkcja która wykonuje odpowiednie działanie w zależności od wyboru opcji użytkownika
    if number == 1:
        logging.info(f'Dodaję {first_number} do {second_number}')
        print(f'Wynik to: {first_number + second_number}')
    elif number == 2:
        logging.info(f'Odejmuję {first_number} od {second_number}')
        print(f'Wynik to: {first_number - second_number}')
    elif number == 3:
        logging.info(f'Mnożę {first_number} razy {second_number}')
        print(f'Wynik to: {first_number * second_number}')
    elif number == 4:
        logging.info(f'Dzielę {first_number} przez {second_number}')
        print(f'Wynik to: {first_number / second_number}')

if __name__ == '__main__':

    while True:

        print('Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: \nAby wyjść wybierz 5')

        while True:
            try:
                choice_number = int(input('Opcja ')) #Wybór opcji działania

                if choice_number <= 4:
                    break;
                elif choice_number == 5:
                    exit()
                else:
                    logging.warning('Wybór nie jest liczbą od 1 do 4, spróbuj ponownie: \n1 Dodawanie, \n2 Odejmowanie, \n3 Mnożenie, \n4 Dzielenie: \nAby wyjść wybierz 5')

            except ValueError:
                logging.warning('Wybór nie jest liczbą od 1 do 4, spróbuj ponownie: \n1 Dodawanie, \n2 Odejmowanie, \n3 Mnożenie, \n4 Dzielenie: \nAby wyjść wybierz 5')

        while True: #Pętla która wypisuje treść błędu dopóki wpisane dane nie będą odpowiadać wymaganym (float)
            try:
                first_number = float(input('Podaj pierwszą liczbę: '))
                second_number = float(input('Podaj drugą liczbę: '))
                break;
            except ValueError:
                logging.warning('Wybór nie jest liczbą, spróbuj ponownie')

        calculation_choice(choice_number)
        print(choice_number)
    
    