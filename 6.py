def main():
    try:
        with open('input.txt', 'r', encoding='utf-8') as input_file:
            lines = input_file.readlines()

        try:
            n = int(lines[0].strip())
        except ValueError:
            result = "ERROR"
        else:
            actual_lines = len(lines) - 1
            result = "YES" if actual_lines == n else "NO"

        with open('output.txt', 'w', encoding='utf-8') as output_file:
            output_file.write(result)
            
    except FileNotFoundError:
        with open('output.txt', 'w', encoding='utf-8') as output_file:
            output_file.write("ERROR")

if __name__ == "__main__":
    main()
