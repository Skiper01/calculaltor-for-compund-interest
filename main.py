
princaple = 0
rate = 0
time = 0


while princaple <= 0:
    princaple = float(input("Enter pricaple amount: "))
    if princaple <= 0:
         print("Princaple cant't be less than or equal zero.")

while rate <= 0:
    rate = float(input("Enter the interest rate: "))
    if rate <= 0:
        print("interest rate can't be less than equal zero.")


while time <= 0:
    time = float(input("Enter time in years: "))
    if time <=0:
        print("Time can't be less than equal zero.")

print(princaple)
print(rate)
print(time)

total = princaple*pow((1 + rate / 100), time)
print(f"Total amount after {time} years is: {total:.2f}")


