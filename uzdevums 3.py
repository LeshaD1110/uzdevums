questions = [
    ["Cik ir 5 + 3?", "8"],
    ["Kāda ir Latvijas galvaspilsēta?", "riga"],
    ["Cik ir 10 * 2?", "20"],
    ["Kā sauc Python datu tipu tekstam?", "str"],
    ["Cik ir 15 - 7?", "8"]
]

score = 0

for q in questions:
    answer = input(q[0] + " ").lower()

    if answer == q[1]:
        print("Pareizi!")
        score += 1
    else:
        print("Nepareizi!")

print("Pareizo atbilžu skaits:", score, "/ 5")

if score == 5:
    print("Novērtējums: Izcili!")
elif score >= 3:
    print("Novērtējums: Labi!")
else:
    print("Novērtējums: Jāmācās vēl!")