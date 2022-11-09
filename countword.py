sentence = input("Enter text to calculate occurance of each word")
counts = dict()
words = sentence.split()

for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1
print(counts)