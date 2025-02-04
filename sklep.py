# sklep.py

import kwiaciarnia

def main():
    # Obliczanie kosztu bukietu z 15 róż (1 róża = 5 zł)
    liczba_kwiatow = 15
    cena_za_sztuke = 5
    koszt = kwiaciarnia.cena_bukietu(liczba_kwiatow, cena_za_sztuke)
    print(f"Koszt bukietu z {liczba_kwiatow} róż wynosi: {koszt} zł")

    # Obliczanie czasu świeżości bukietu przechowywanego w temperaturze 10°C
    temperatura = 10
    dni_swiezosci = kwiaciarnia.czas_trwania_swiezosci(temperatura)
    print(f"Przy temperaturze {temperatura}°C bukiet pozostanie świeży przez {dni_swiezosci} dni.")

    # Sprawdzenie dostępności kwiatów w sklepie (początkowo 100, sprzedano 35)
    suma_kwiatow = 100
    sprzedane = 35
    dostepne = kwiaciarnia.dostepnosc_kwiatow(suma_kwiatow, sprzedane)
    print(f"W sklepie pozostało {dostepne} kwiatów.")

    # Przykładowe dane sprzedaży kwiatów do wyznaczenia najczęściej sprzedawanego rodzaju
    dane_sprzedazy = [
        ("róża", 15),
        ("tulipan", 10),
        ("lilia", 12),
        ("gerbera", 8)
    ]
    najpopularniejszy = kwiaciarnia.najczesciej_sprzedawany(dane_sprzedazy)
    print(f"Najczęściej sprzedawany kwiat to: {najpopularniejszy}")

if __name__ == "__main__":
    main()
