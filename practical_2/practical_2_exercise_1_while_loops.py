sequence = 'GATTACAGAACTGATAC'

a_count = 0
i=0
while a_count < 3:
    if sequence[i] == 'A':
        a_count += 1
    i = i+1
print("a_count:",a_count)
git reset --hard HEAD~1