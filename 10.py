days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def date_to_days(date_str):
    day, month = map(int, date_str.split('.'))
    return sum(days[:month-1]) + day

with open('input.txt', 'r', encoding='utf-8') as f:
    current_date = f.readline().strip()
    n = int(f.readline())
    
    cells = []
    for _ in range(n):
        line = f.readline().strip()
        cell_name, date = line.split()
        cells.append([cell_name, date])

current_day = date_to_days(current_date)

result = []
for cell in cells:
    name = cell[0]
    date = cell[1]
    if current_day - date_to_days(date) > 3:
        result.append(name)

with open('output.txt', 'w', encoding='utf-8') as f:
    for name in result:
        f.write(name + '\n')
