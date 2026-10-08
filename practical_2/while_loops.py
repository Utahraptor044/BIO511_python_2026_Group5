sequence = 'GATTACAGAACTGATAC'

a_count = 0
i=0
while a_count < 3:
    if sequence[i] == 'A':
        a_count += 1
    i = i+1
print(f"a_count: {a_count}")
print(f"the index of the string where the third 'A' is found {i-1}")

