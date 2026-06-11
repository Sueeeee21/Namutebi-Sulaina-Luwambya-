def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a value greater than 0.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a value greater than 0.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def get_tip_percentage():
    print("\nSelect tip percentage:")
    print("  1. 10%")
    print("  2. 15%")
    print("  3. 20%")
    print("  4. Custom")

    while True:
        choice = input("Enter choice (1-4): ").strip()
        if choice == "1":
            return 10.0
        elif choice == "2":
            return 15.0
        elif choice == "3":
            return 20.0
        elif choice == "4":
            return get_positive_float("Enter custom tip percentage: ")
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


def main():
    print("=" * 40)
    print("       BILL SPLIT CALCULATOR")
    print("=" * 40)

    bill_amount = get_positive_float("\nEnter total bill amount ($): ")
    num_people = get_positive_int("Enter number of people: ")
    tip_percent = get_tip_percentage()


    tip_amount = bill_amount * (tip_percent / 100)
    total_bill = bill_amount + tip_amount
    per_person = total_bill / num_people

   
    print("\n" + "=" * 30)
    print("          RECEIPT")
    print("=" * 30)
    print(f"  Original Bill:        ${bill_amount:>10.2f}")
    print(f"  Tip ({tip_percent:.1f}%):           ${tip_amount:>10.2f}")
    print(f"  {'─' * 38}")
    print(f"  Total Bill:           ${total_bill:>10.2f}")
    print(f"  Number of People:     {num_people:>10}")
    print(f"  {'─' * 38}")
    print(f"  Each Person's Share:  ${per_person:>10.2f}")
    print("=" * 40)

    print(f"\n Each of the {num_people} person(s) owes: ${per_person:.2f}")


if __name__ == "__main__":
    main()