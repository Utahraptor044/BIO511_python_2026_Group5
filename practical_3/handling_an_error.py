values = ['10', '5', 'hello', '8', 'three', '2']
for value in values:
    try:
        print(int(value))
    except ValueError:
        print(f"Skipping invalid value: {value}")