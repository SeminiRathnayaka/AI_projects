# Medical Terms Explainer - with file handling and exceptions

import json

# Load terms from file
def load_terms():
    try:
        with open("terms.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("No terms file found, starting fresh!")
        return {}

# Load when program starts
medical_terms = load_terms()
print("Terms loaded:", len(medical_terms), "terms found!")

# Save terms to file
def save_terms(terms):
    with open("terms.json", "w") as file:
        json.dump(terms, file, indent=4)
    print("Term saved successfully!")

# Main program
def explain_term():
    while True:
        print("\n1. Look up a term")
        print("2. Add a new term")
        print("3. Exit")

        choice = input("\nChoose (1/2/3): ")

        if choice == "1":
            term = input("Enter a medical term: ").lower()
            try:
                if not term:
                    raise ValueError("Please enter a term!")
                if term in medical_terms:
                    print("=>", medical_terms[term])
                else:
                    print("=> Sorry, I don't know that term yet.")
            except ValueError as e:
                print("ERROR:", e)

        elif choice == "2":
            term = input("Enter new term: ").lower()
            try:
                if not term:
                    raise ValueError("Term cannot be empty!")
                explanation = input("Enter explanation: ")
                if not explanation:
                    raise ValueError("Explanation cannot be empty!")
                medical_terms[term] = explanation
                save_terms(medical_terms)
            except ValueError as e:
                print("ERROR:", e)

        elif choice == "3":
            print("Goodbye! Stay Healthy!")
            break

        else:
            print("Invalid choice! Please enter 1, 2 or 3 only.")

print(" -- Medical Terms Explainer V2 --")
explain_term()