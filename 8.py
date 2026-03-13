def main():
    try:
        with open('input.txt', 'r', encoding='utf-8') as input_file:
            steps = [int(line.strip()) for line in input_file]

        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        monthly_averages = []
        с = 0
        
        for month_days in days_in_month:
            month_sum = sum(steps[с:с + month_days])
            month_average = month_sum / month_days
            monthly_averages.append(month_average)
            с += month_days
        
        with open('output.txt', 'w', encoding='utf-8') as output_file:
            for average in monthly_averages:
                output_file.write(f"{average}\n")
        
    except FileNotFoundError:
        print('Файл не найден')

if __name__ == "__main__":
    main()
