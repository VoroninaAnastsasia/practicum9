def main():
    try:
        with open('input.txt', 'r', encoding='utf-8') as input_file:
            numbers = input_file.read().split()
        
        if len(numbers) != 3:
            raise ValueError

        a, b, c = map(int, numbers)

        result = a / b + c

        with open('output.txt', 'w', encoding='utf-8') as output_file:
            output_file.write(str(result))
            
    except FileNotFoundError:
        print('Файл не найден')
    except ValueError:
        print('data error')
    except ZeroDivisionError:
        print('division by 0')

if __name__ == "__main__":
    main()
