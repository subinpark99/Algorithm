# seq_serach() 함수를 사용하여 특정 인덱스 검색

from search_while import seq_search

t = (1.27, 3.28, 100, 2.14, 1)
s = 'string'
a = ['NCT', 'WayV', 'EXO']

print(f'{t}에서 2.14의 인덱스는 {seq_search(t, 2.14)} 임')
print(f'{s}에서 n의 인덱스는 {seq_search(s, "n")} 임')
print(f'{a}에서 "EXO"의 인덱스는 {seq_search(a, "EXO")} 임')
