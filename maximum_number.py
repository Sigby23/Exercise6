num = int(input())
max_value = 0

while num >= 0:
    if num > max_value:
       max_value = num
    num = int(input())
print(max_value)
