# calculaltor-for-compund-interest

# Kalkulator procentu składanego / Compound Interest Calculator  

## 🇵🇱 Opis (Polski)

Ten projekt to prosty skrypt w Pythonie do obliczania wartości końcowej kapitału przy zadanej stopie procentowej i okresie inwestycji.  

### Jak działa?

Program pobiera od użytkownika trzy wartości:  
1. **Kapitał początkowy (principal)** – kwota, od której liczone są odsetki.  
2. **Stopa procentowa (rate)** – roczna stopa procentowa w %.  
3. **Czas (time)** – okres inwestycji w latach.  

Na tej podstawie oblicza końcową kwotę według wzoru na procent składany:  

\[
A = P \times \left(1 + \frac{r}{100}\right)^t
\]

gdzie:  
- \( A \) – końcowa wartość inwestycji,  
- \( P \) – kapitał początkowy,  
- \( r \) – stopa procentowa,  
- \( t \) – liczba lat.  

### Uruchomienie

1. Zainstaluj **Python 3**.  
2. Pobierz plik `main.py`.  
3. W terminalu wpisz:  

```bash
python main.py
```
Wprowadź kolejno wymagane wartości.

Przykład działania
```yaml
Enter principal amount: 1000
Enter the interest rate: 5
Enter time in years: 10
Total amount after 10 years is: 1628.89
```
##🇬🇧 Description (English)
This project is a simple Python script for calculating the final value of an investment with a given interest rate and investment period.

##How it works?
The program asks the user to enter three values:

Principal – the initial amount of money.

**1. Rate – annual interest rate in %.**

**2. Time – investment period in years.**

**3It then calculates the final amount using the compound interest formula:**
\[
𝐴=𝑃×(1+𝑟100)𝑡A=P×(1+ 100r)^t
 
where:

𝐴
A – final value of the investment,

𝑃
P – principal,

𝑟
r – interest rate,

𝑡
t – number of years.

Run
Install Python 3.

Download the main.py file.

In the terminal, run:
```bash
python main.py
```
Enter the requested values.

Example run
```yaml
Enter principal amount: 1000
Enter the interest rate: 5
Enter time in years: 10
Total amount after 10 years is: 1628.89
```
