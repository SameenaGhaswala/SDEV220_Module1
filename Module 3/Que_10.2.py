def get_odds():
    for i in range(11):
        if i % 2 == 1:
            yield i

count = 0
for j in get_odds():
    count += 1
    if count == 3:
        print(j)

