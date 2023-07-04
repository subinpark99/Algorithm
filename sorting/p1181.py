wordlist = []
for i in range(int(input())):
    word = input()
    wordlist.append(word)

wordlist = list(set(wordlist))
wordlist.sort()  # 사전 순
wordlist.sort(key=len)  # 길이 순

for i in wordlist:
    print(i)
