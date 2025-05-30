months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def main():
    while True:
        date = input("Date: ")
        try:
            month, day, year = date.split("/")
            month = int(month)
            day = int(day)
            year = int(year)
            if day > 31 or month > 12:
                continue
            else:
                print(f"{year}-{month:02}-{day:02}")
                break

        except ValueError:
            if "," not in date:
                continue
            date = date.replace(",", "")
            date_parts = date.split(" ")
            if date_parts[0].isdigit() or date_parts[1].isalpha():
                continue
            month, day, year = date_parts
            day = int(day)
            year = int(year)
            if day > 31:
                continue
            elif month in months:
                num_month = months.index(month)
                print(f"{year}-{(num_month + 1):02}-{day:02}")
                break
            else:
                continue


main()
