def check_symptoms():
    print("Answer the following questions with 'yes' or 'no':")


    questions = [
        "Are you over the age of 55?",
        "Have you been diagnosed with Pneumonia?",
        "Have you been diagnosed with Hypertension?",
        "Have you been diagnosed with Diabetes?",
        "Are you classified as Obese?"
    ]


    for question in questions:
        answer = input(question + " ").strip().lower()
        if answer == "yes":
            print("Go to the hospital immediately")
            return  # Exit immediately if any question is answered with "yes"