# 각 배열 원소의 최댓값을 구해서 출력(튜플, 문자열, 문자열리스트)

from max import max_of

t = (4, 7, 5.6, 2, 1.1, 3)
s = 'string'
a = ['NCT', 'NCT 127', 'NCT DREAM']

print(f'{t}의 최댓값은 {max_of(t)}임')
print(f'{s}의 최댓값은 {max_of(s)}임')
print(f'{a}의 최댓값은 {max_of(a)}임')
