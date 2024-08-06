def main():

    # Initialize list of items
    items_list = []
    # Initialize dictionary prefix + item
    final_items = {}

    while True:
        try:
            # Prompt user for item and capitalize
            item = input().upper()
            # Append item to items_list
            items_list.append(item)

        # When user inputs ctrl-d
        except EOFError:
            # Sort items_list
            items_list = sorted(items_list)
            print()

            # For each item in sorted items_list
            for item in items_list:
                if item in final_items:
                    # If the item is in the final_items dictionary already,
                    # increment its value
                    final_items[item] += 1
                else:
                    # Else, add the item to the final_items dictionary
                    final_items[item] = 1

            for item in final_items.keys():
                print(f"{final_items[item]} {item}")
            break


main()
