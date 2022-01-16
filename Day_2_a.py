print("Hello World"[8])

s = "thinker"[2:5]

print(s)

print(set("Mississippi"))


num_of_phrases = int(input())
phrases = []
for phrase in range(num_of_phrases):
    phrase = input()
    phrases.append(phrase)
for phrase in phrases:
    if phrase == phrase[::-1]:
        print("Y")
    else:
        print("N")
