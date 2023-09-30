donation_records = {}
def add_donation():
    donor_name = input("Enter donor name: ")
    donation_amount = float(input("Enter donation amount: "))
    if donor_name in donation_records:
        donation_records[donor_name] += donation_amount
    else:
        donation_records[donor_name] = donation_amount
    print(f"Donation of ${donation_amount} from {donor_name} recorded successfully!")

def view_donations():
    print("Donation Records:")
    for donor, total_donation in donation_records.items():
        print(f"{donor}: ${total_donation}")

def main():
    while True:
        print("\nDonation Tracker Menu:")
        print("1. Add Donation")
        print("2. View Donations")
        print("3. Exit")

        choice = input("Select an option (1/2/3): ")
        if choice == '1':
            add_donation()
        elif choice == '2':
            view_donations()
        elif choice == '3':
            print("Exiting Donation Tracker.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()