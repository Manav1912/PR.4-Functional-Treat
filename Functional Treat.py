print("Welcome to the Data Analyzer and Transformer Program")

array = []

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def statistics(array):
    flat = [num for row in array for num in row]
    return min(flat), max(flat), sum(flat), sum(flat) / len(flat)


while True:
    print("\nMain Menu:")
    print("1. Input Data")
    print("2. Display Data Summary")
    print("3. Calculate Factorial")
    print("4. Filter Data by Threshold")
    print("5. Sort Data")
    print("6. Display Dataset Statistics")
    print("7. Exit Program")

    choice = int(input("Please enter your choice: "))

    match choice:

        case 1:
            array = []
            rows = int(input("Enter number of rows: "))

            for i in range(rows):
                row = list(map(int, input(f"Enter elements for row {i+1}: ").split()))
                array.append(row)

            print("Data stored successfully!")

        case 2:
            if len(array) == 0:
                print("Please enter data first!")
            else:
                flat = [num for row in array for num in row]

                print("\nData Summary:")
                print("Total elements:", len(flat))
                print("Minimum value:", min(flat))
                print("Maximum value:", max(flat))
                print("Sum of all values:", sum(flat))
                print("Average value:", round(sum(flat) / len(flat), 2))

        case 3:
            n = int(input("Enter a number: "))

            if n < 0:
                print("Negative number not allowed!")
            else:
                print("Factorial:", factorial(n))

        case 4:
            if len(array) == 0:
                print("Please enter data first!")
            else:
                threshold = int(input("Enter threshold value: "))

                result = [
                    [x for x in row if x >= threshold]
                    for row in array
                ]

                print("Filtered Data:", result)

        case 5:
            if len(array) == 0:
                print("Please enter data first!")
            else:
                print("1. Ascending")
                print("2. Descending")

                option = int(input("Enter your choice: "))

                flat = [num for row in array for num in row]

                match option:
                    case 1:
                        flat.sort()
                        print("Ascending Order:", flat)

                    case 2:
                        flat.sort(reverse=True)
                        print("Descending Order:", flat)

                    case _:
                        print("Invalid sorting choice!")

        case 6:
            if len(array) == 0:
                print("Please enter data first!")
            else:
                minimum, maximum, total, average = statistics(array)

                print("\nDataset Statistics:")
                print("Minimum value:", minimum)
                print("Maximum value:", maximum)
                print("Sum of all values:", total)
                print("Average value:", round(average, 2))

        case 7:
            print("Thank you for using the Data Analyzer and Transformer Program. Goodbye!")
            break

        case _:
            print("Invalid choice! Please try again.")