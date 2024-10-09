import random

reader = open("python/Text-generator/mobydick.txt", encoding="utf-8")

successor_map = {}
window = []

for line in reader:
    for word in line.split():
        clean_word = word.strip('.;,-“’”:?—‘!()_').lower()
        window.append(clean_word)
        if len(window) >= 5:
            key = (window[0], window[1], window[2], window[3])
            value = window[4]
            if key in successor_map:
                successor_map[key].append(value)
            else:
                successor_map[key] = [value]
            window.pop(0)

word1 = "so"
word2 = "fare"
word3 = "thee"
word4 = "well"

generated_text = []

print(word1, word2, word3, word4, end=' ')
generated_text.append(f"{word1} {word2} {word3} {word4}")

for i in range(1000000):
    successors = successor_map.get((word1, word2, word3, word4))
    
    if not successors:
        break
    word5 = random.choice(successors)
    print(word5, end=' ')
    generated_text.append(f" {word5}")
    
    word1 = word2
    word2 = word3
    word3 = word4
    word4 = word5

print()
print(''.join(generated_text))
