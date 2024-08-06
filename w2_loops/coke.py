def main():
    # Initialize coin counter
    count = 0
    print("Amount Due: 50")
    while count < 50:

        coin = int(input("Insert Coin: "))

        # Check if coin is valid (25, 10, 5)
        if coin == 25 or coin == 10 or coin == 5:
            count += coin
            if count < 50:
                print(f"Amount Due: {50 - count}")
            else:
                # Ensure the change is not negative
                print(f"Change Owed: {count - 50}")
        else:
            # Print the remaining amount due if coin is invalid
            print(f"Amount Due: {50 - count}")

main()
