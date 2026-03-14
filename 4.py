def main():
    """The function adds to the output.txt file only
    those files that are longer than 20"""
    
    try:
        with open('input.txt', 'r', encoding='utf-8') as input_file:
            all_lines = input_file.readlines()
        
        long_lines = []
        
        for line in all_lines:
            new_line = line.rstrip('\n')
            
            line_length = len(new_line)
            
            if line_length > 20:
                long_lines.append(line)
        
        with open('output.txt', 'w', encoding='utf-8') as output_file:
            for long_line in long_lines:
                output_file.write(long_line)
            
    except FileNotFoundError:
        print('Файл не найден')

if __name__ == "__main__":
    main()
