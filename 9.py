import os

def main():
    os.makedirs('simple', exist_ok=True)
    
    file_read = open('input.txt', 'r', encoding='utf-8')
    all_lines = file_read.readlines()
    file_read.close()
    
    even_lines = []
    
    i = 1 
    while i < len(all_lines):
        even_lines.append(all_lines[i])
        i = i + 2
    with open('simple/output.txt', 'w', encoding='utf-8') as file_write:
        for line in even_lines:
            file_write.write(line)

if __name__ == "__main__":
    main()
    
