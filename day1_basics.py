words = ["apple", "banana", "apple", "orange", "banana", "apple"]

counts = {}

for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

with open("result.txt", "w", encoding="utf-8") as file:
    for word, count in counts.items():
        file.write(f"{word}: {count}\n")

print("Script finished")