import logging 
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename="logfile.log")


def kalkulator (rodzaj_dzialania, a, b):
    if rodzaj_dzialania == 1:
        czynnosc = "Dodaję"
        wynik = a + b
    if rodzaj_dzialania == 2:
        czynnosc = "Odejmuję"
        wynik = a - b
    if rodzaj_dzialania == 3:
        czynnosc = "Mnoze"
        wynik = a * b
    if rodzaj_dzialania == 4:
        czynnosc = "Dzielę"
        wynik = a / b
    logging.info(f"{czynnosc} {a} i {b}")
    logging.info(f"Wynik to: {wynik}")
    return(f"{czynnosc} {a} i {b} \nWynik to: {wynik}")
    
while True:
    try:
        typ_dzialania = int(input("Podaj działanie, posługując się odpowiednią liczbą:  1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "))
        logging.debug(f"Podaj działanie, posługując się odpowiednią liczbą:  1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: {typ_dzialania}")
    except ValueError:
        logging.info("Niewlasciwa wartosc!")
        continue
    if typ_dzialania > 4:
        logging.info("Niewlasciwy typ dzialania!")
        continue
    else:
        break
    
while True:
    try:
        skladnik_1 = float(input("Podaj składnik 1:"))
        skladnik_2 = float(input("Podaj składnik 2:"))
        logging.info(f"Podaj składnik 1: {skladnik_1}")
        logging.info(f"Podaj składnik 2: {skladnik_2}")
        break
    except ValueError:
        logging.info("Niewlasciwa wartosc!")
        continue


print(kalkulator(typ_dzialania, skladnik_1, skladnik_2))