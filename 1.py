def main():
    try:
        with open('input.txt', 'r', encoding='utf-8') as input_file:
            data = input_file.read()
        
        new_data = data.upper()
        
        with open('output.txt', 'w', encoding='utf-8') as output_file:
            output_file.write(new_data)
            
    except FileNotFoundError:
        print("Файл не найден")

if __name__ == "__main__":
    main()
