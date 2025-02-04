# kwiaciarnia.py

def cena_bukietu(liczba_kwiatow, cena_za_sztuke):
    """
    Oblicza koszt bukietu na podstawie liczby kwiatów i ceny za sztukę.
    """
    return liczba_kwiatow * cena_za_sztuke

def czas_trwania_swiezosci(temperatura):
    """
    Oblicza czas (w dniach), przez jaki bukiet pozostaje świeży, biorąc pod uwagę temperaturę przechowywania.
    
    Przyjmujemy, że:
      - przy temperaturze 0°C bukiet pozostaje świeży przez 7 dni,
      - za każde 5°C wzrostu temperatura świeżość zmniejsza się o 1 dzień,
      - minimalny czas świeżości to 1 dzień.
    """
    # Jeśli temperatura jest ujemna, traktujemy ją jako 0°C
    if temperatura < 0:
        temperatura = 0
    dni = 7 - (temperatura // 5)
    if dni < 1:
        dni = 1
    return dni

def dostepnosc_kwiatow(suma_kwiatow, sprzedane):
    """
    Zwraca liczbę dostępnych kwiatów w kwiaciarni.
    """
    return suma_kwiatow - sprzedane

def najczesciej_sprzedawany(sprzedaz):
    """
    Zwraca najczęściej sprzedawany rodzaj kwiatu.
    
    Parametr 'sprzedaz' to lista krotek, gdzie każda krotka zawiera (nazwa_kwiatu, liczba_sprzedanych).
    Jeśli lista jest pusta, funkcja zwraca None.
    """
    if not sprzedaz:
        return None
    # Używamy funkcji max z kluczem, aby znaleźć krotkę z największą liczbą sprzedanych sztuk.
    najpopularniejszy = max(sprzedaz, key=lambda x: x[1])
    return najpopularniejszy[0]
