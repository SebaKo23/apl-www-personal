## Rozwiązanie zadania 10:

### 1. Wyświetl wszystkie obiekty modelu Osoba
from polls.models import Osoba
Osoba.objects.all()

### 2. Wyświetl obiekt modelu Osoba z id = 3
Osoba.objects.get(id=3)

### 3. Wyświetl obiekty modelu Osoba, których nazwa rozpoczyna się na wybraną przez Ciebie literę alfabetu (tak, żeby był co najmniej jeden wynik)
Osoba.objects.filter(nazwisko__startswith='R') 

### 4. Wyświetl unikalną listę stanowisk przypisanych dla modeli Osoba
Osoba.objects.values('stanowisko').distinct() 

### 5. Wyświetl nazwy stanowisk posortowane alfabetycznie malejąco
from polls.models import Stanowisko 
Stanowisko.objects.order_by('-nazwa')

### 6. Dodaj nową instancję obiektu klasy Osoba i zapisz w bazie
nowa_osoba = Osoba(imie='Jan', nazwisko='Kowalski', plec=Osoba.Plec.mezczyzna, stanowisko=Stanowisko.objects.get(nazwa='Pracownik')) 
nowa_osoba.save()
