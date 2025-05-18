s=""
current = ""
words = []
with open("palavras.txt", "r") as file:
    s = file.read()

for char in s:
    if char == "\n":
        words.append(current)
        current = ""
    else:
        current += char

words = sorted(words, key=len)

s = "\n".join(words)
with open("palavras.txt", "w") as file:
    file.write(s)