sump = int(input())

book = []
for i in range(9):
    n = int(input())
    book.append(n)

print(sump - sum(book))
