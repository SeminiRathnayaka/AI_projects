# Medical terms explainer - AI mini project

# Medical terms explainer - AI mini project

medical_terms = {
    "hemoglobin": "Hemoglobin is a protein in your red blood cells that carries oxygen around your body. Low hemoglobin means you may feel tired or weak.",
    "glucose": "Glucose is your blood sugar level. High glucose can mean diabetes risk.",
    "cholesterol": "Cholesterol is a fatty substance in your blood. Too much can block your arteries and cause heart problems.",
    "diabetes": "A disease where blood sugar levels are too high.",
    "blood pressure": "The force of blood pushing against blood vessel walls.",
}

def explain_term():
    while True:
        term = input(" Enter a medical term : ").lower()

        if term in medical_terms:
            print(" => ", medical_terms[term])
        else:
            print(" => sorry, I don't know that term yet.")

        again = input(" Look up another term? (yes/no): ").lower()

        if again == "no":
            print(" Goodbye! Stay Healthy!")
            break

print(" -- Medical Terms Explainer --")
explain_term()


