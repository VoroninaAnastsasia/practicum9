def main():
    with open('input.txt', 'r', encoding='utf-8') as f:
        current_date = f.readline().strip()
        n = int(f.readline().strip())
        cells = [f.readline().strip().split() for _ in range(n)]

    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def to_days(date):
        d, m = map(int, date.split('.'))
        return sum(days_in_month[:m-1]) + d
    
    current_days = to_days(current_date)

    result = [cell for cell, date in cells if current_days - to_days(date) > 3]

    with open('output.txt', 'w', encoding='utf-8') as f:
        f.writelines(f"{cell}\n" for cell in result)

if __name__ == "__main__":
    main()
