from collections import Counter
n = int(input())
book = [0 for _ in range(n)]
for i in range(n):
    book[i] = input()
book.sort()
count_book = Counter(book)
max_book = count_book.most_common(n=1)
print(max_book[0][0])