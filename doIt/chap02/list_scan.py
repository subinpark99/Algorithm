print('리스트의 모든 원소 스캔(원소 수 미리 파악)')
x = ['Taeil', 'TaeYong', 'Johnny', 'Yuta']
for i in range(len(x)):
    print(f'x[{i}] = {x[i]}')


print('\n리스트의 모든 원소를 enumerate() 함수로 스캔')
y = ['JaeHyun', 'Jungwoo', 'Doyoung']
for i, name in enumerate(y):
    print(f'y[{i}] = {name}')


print('\n리스트의 모든 원소를 enumerate() 함수로 스캔, 1부터 카운트')
z = ['Mark', 'Haechan']
for i, name in enumerate(z, 1):
    print(f'{i}번째 = {name}')
