def main():
    try:
        with open('input.txt', 'r', encoding='utf-8') as input_file:
            content = input_file.read()
        
        transformed_content = content.upper()
        
        with open('output.txt', 'w', encoding='utf-8') as output_file:
            output_file.write(transformed_content)
            
    except FileNotFoundError:
        print("Ошибка: Файл input.txt не найден")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()
