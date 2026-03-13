def main():
    try:
        with open('input.txt', 'r', encoding='utf-8') as input_file:
            all_lines = input_file.readlines()
        
        first_ch_list = []
        
        for line in all_lines:
            clean_line = line.strip()
            
            if clean_line != '':
                first_ch = clean_line[0]
                first_ch_list.append(first_ch)
        
        result_word = ''.join(first_ch_list)
        
        with open('output.txt', 'w', encoding='utf-8') as output_file:
            output_file.write(result_word)
            
    except FileNotFoundError:
        print('Файл не найден')

if __name__ == '__main__':
    main()
