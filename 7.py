def main():
    try:
        with open('input.txt', 'r', encoding='utf-8') as input_file:
            lines = input_file.readlines()

        filtered_lines = [line for line in lines if line.strip() != '100']

        with open('output.txt', 'w', encoding='utf-8') as output_file:
            output_file.writelines(filtered_lines)
            
    except FileNotFoundError:
        print("Файл не найден")

if __name__ == "__main__":
    main()
