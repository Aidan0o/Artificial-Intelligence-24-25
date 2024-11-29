def forward_chaining_rule_validation():
    # Configuration for the questions and scoring rules
    rules_config = [
        {
            "question": "What is your age?",
            "key": "age",
            "type": "numeric",
            "points": 0,  # numeric value IS our score modifier
        },
        {
            "question": "Have you been diagnosed with Pneumonia? (yes/no)",
            "key": "pneumonia",
            "type": "boolean",
            "points": 30,
        },
        {
            "question": "Have you been diagnosed with Hypertension? (yes/no)",
            "key": "hypertension",
            "type": "boolean",
            "points": 10,
        },
        {
            "question": "Have you been diagnosed with Diabetes? (yes/no)",
            "key": "diabetes",
            "type": "boolean",
            "points": 10,
        },
        {
            "question": "Have you been classified as Obese? (yes/no)",
            "key": "obesity",
            "type": "boolean",
            "points": 5,
        },
    ]


    # Initialize score
    score = 0


    # Dictionary to store user responses
    responses = {}


    # Process each question
    for rule in rules_config:
        question = rule["question"]
        key = rule["key"]
        answer_type = rule["type"]
        points = rule["points"]


        while True:
            user_input = input(question + " ").strip()
            if answer_type == "numeric":
                try:
                    responses[key] = int(user_input)
                    score += responses[key]
                    break
                except ValueError:
                    print("Please enter a valid number.")
            elif answer_type == "boolean":
                if user_input.lower() in ["yes", "no"]:
                    responses[key] = user_input.lower() == "yes"
                    if responses[key]:  # Add points if the answer is 'yes'
                        score += points
                    break
                else:
                    print("Please answer 'yes' or 'no'.")


    # Final output
    print("\nYour responses:")
    for key, value in responses.items():
        print(f"{key.capitalize()}: {value}")
    print(f"\nFinal Score: {score}")
    # evaluate the final score
    if score > 70:
        print("You are advised to attend the nearest hospital as soon as possible.")
    elif score == 70:
        print("You are advised to ring 111 and discuss further with health professional.")
    else:
        print("We advise you to get rest and plenty of fluids and remain at home.")


# Run the function
if __name__ == "__main__":
    forward_chaining_rule_validation()