def main():
    time = input("What time is it? ").strip()
    mealtime = convert(time)

    if mealtime >= 7 and mealtime <= 8:
        print("breakfast time")
    elif mealtime >= 12 and mealtime <= 13:
        print("Lunch time")
    elif mealtime >= 18 and mealtime <= 19:
        print("Dinner time")
    else:
        return


def convert(time):
    split_time = time.split(":")
    hours = float(split_time[0])
    minutes = float(split_time[1]) / 60
    return hours + minutes



if __name__ == "__main__":
    main()
