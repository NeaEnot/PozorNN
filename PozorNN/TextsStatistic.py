import os

files = os.listdir('Dataset')

min_n = 100000
max_n = 0
less_64 = 0
total_n = 0

i = 0

for file in files:
    i += 1
    print(i)

    with open(f'Dataset\\{file}', 'r', encoding='utf-8') as file:
        n = 0
        for line in file:
            n += len(line)

        total_n += n

        if n > max_n:
            max_n = n

        if n < min_n:
            min_n = n

        if (n < 64):
            less_64 += 1

print('min_n: ', min_n)
print('max_n: ', max_n)
print('medium_n: ', total_n / len(files))
print('less_64: ', less_64)