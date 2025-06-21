from collections import Counter

words = open("cars.txt").read().lower().split()
for word, count in Counter(words).items():
    print(f"{word}: {count}")