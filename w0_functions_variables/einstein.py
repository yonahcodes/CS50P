# Define converting function
def formula(n):
    # m times c (300 000 000^2)
    return n * pow(300000000, 2)



# Define main function
def main():
    # Prompt user for mass
    m = int(input("Enter mass: "))
    # Output the equivalent number of Jules
    E = formula(m)
    # Print function(m)
    print(E)


# Call main
main()
