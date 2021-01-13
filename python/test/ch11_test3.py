def add_1(n):
      return n + 1

target = [1, 2, 3, 4, 5]

result = map(add_1, target)

print(list(result))