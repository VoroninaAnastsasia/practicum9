import os

os.makedirs('simple', exist_ok=True)

with open('input.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    
lines2 = [lines[i] for i in range(1, len(lines), 2)]

with open('simple/output.txt', 'w', encoding='utf-8') as f:
    f.writelines(lines2)
