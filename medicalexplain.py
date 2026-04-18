# Medical Terms Explainer V2 - with file handling

import json

# Load terms from file 
def load_terms():
    try:
        with open("terms.json","r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("No terms file found,strating freash!")
        return{}
    

# Load when program starts 
medical_terms = load_terms ()

print("Terms loded :",len(medical_terms),"terms found!")

# Save the terms to file 
def save_terms(terms):
    with open("terms.json","w") as file:
        json.dump(terms, file, indent=4 )
    print("Term saved successfully")


# Main Program
def explain_term():
    while True :
        print("\n1.Look up a term")
        print("\n2.Add a new twrm")
        print("\n3.exit")

        choice = input("\nChoose (1/2/3):  ")

        if choice == "1":
            term = input("Enter a medical term: ").lower()
            if term in medical_terms:
                print("=>", medical_terms[term])
            else:
                print("=> Sorry, I don't know that term yet.")

        elif choice == "2":
            term = input("Enter new term: ").lower()
            explanation = input("Enter explanation: ")
            medical_terms[term] = explanation
            save_terms(medical_terms)

        elif choice == "3":
            print("Goodbye! Stay Healthy!")
            break

print(" -- Medical Terms Explainer V2 --")
explain_term()
