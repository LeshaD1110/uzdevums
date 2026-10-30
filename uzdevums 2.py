count = int(input("Cik preces tu pērc? "))
total = 0

for i in range(count):
    price = float(input("Ievadi preces cenu: "))
    total += price

if total > 50:
    total = total * 0.9

print("Gala cena:", round(total, 2), "EUR")