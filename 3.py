def main():
    try:
        with open('input.txt', 'r', encoding='utf-8') as input_file:
            # Фильтруем пустые строки и берем первый символ каждой строки
            first_chars = [line[0] for line in input_file if line.strip()]
        
        # Запись результата
        with open('output.txt', 'w', encoding='utf-8') as output_file:
            output_file.write(''.join(first_chars))
            
    except FileNotFoundError:
        print("Ошибка: Файл input.txt не найден")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()
