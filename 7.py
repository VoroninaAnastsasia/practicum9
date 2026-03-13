def main():
    try:
        with open('input.txt', 'r', encoding='utf-8') as input_file:
            all_lines = input_file.readlines()
        
        result_lines = []
        
        for line in all_lines:
            clean_line = line.strip()
            
            if clean_line != '100':
                result_lines.append(line)
        
        with open('output.txt', 'w', encoding='utf-8') as output_file:
            for result_line in result_lines:
                output_file.write(result_line)
            
    except FileNotFoundError:
        print('Файл не найден')

if __name__ == "__main__":
    main()
