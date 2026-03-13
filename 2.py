def main():
    try:
        with open('input.txt', 'r', encoding='utf-8') as input_file:
            lines = input_file.readlines()

        new_lines = []
        for line in lines:
            if line != '':
                first_ch = line[0]
                if first_ch == 'A':
                    new_lines.append(line)

        with open('output.txt', 'w', encoding='utf-8') as output_file:
            for result_line in new_lines:
                output_file.write(result_line)
            
    except FileNotFoundError:
        print('Файл не найден')

if __name__ == "__main__":
    main()
