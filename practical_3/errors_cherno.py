try:
    number = int('five')
    print(number)
except ValueError:
    print('That is not a valid number')

values = ['10', '5', 'hello', '8', 'three', '2','tuna for lunch','63']

for v in values:
    try:
        transf = int(v)
        print(transf)
    except ValueError:
        print(f"Skipping invalid value: {v}")