word = input("Enter a word: ")
duplicate = []
for i in word:
    if word.count(i) > 1:
        duplicate.append(i)
print("Duplicate letters:", duplicate)
if duplicate:
    print(True)
else:
    print(False)
