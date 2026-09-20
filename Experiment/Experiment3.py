word1 = input("Enter first word: ")
word2 = input("Enter second word: ")
common = []
for i in word1:
    if i in word2:
        common.append(i)
print("Common letters:", common)
if common:
    print(True)
else:
    print(False)
