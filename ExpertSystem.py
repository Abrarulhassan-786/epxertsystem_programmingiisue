# Define global variables
facts = {}

# Define the knowledge base
knowledge_base = {
    "Symptom": {
        "Syntax error": {"Cause": ["Incorrect syntax"], "Solution": ["Correct the syntax errors in your code"]},
        "Runtime error": {"Cause": ["Incompatible data types", "Division by zero", "Array out of bounds"], "Solution": ["Check your data types", "Avoid division by zero", "Check array boundaries"]},
        "Logic error": {"Cause": ["Incorrect use of logical operators", "Incorrect conditional statements"], "Solution": ["Review your logic and correct any errors"]},
        "Memory error": {"Cause": ["Excessive memory usage"], "Solution": ["Optimize your code to use less memory"]}
    }
}

# Define the forward chaining function
def forward_chaining(symptom):
    if symptom in knowledge_base["Symptom"]:
        for cause in knowledge_base["Symptom"][symptom]["Cause"]:
            if cause not in facts:
                user_input = input(f"Do you have {cause}? (y/n): ")
                if user_input.lower() == "y":
                    facts[cause] = True
                else:
                    return False
        print("Solution: ", knowledge_base["Symptom"][symptom]["Solution"])
        return True
    else:
        return False

# Define the main function
def main():
    print("=================================ABRAR UL HASSAN=================================")
    print("-----------Welcome to the programming issue diagnosis expert system!----------")
    print("=======================================SID 10970=================================")
    while True:
        user_input = input("Enter a symptom or 'done' to quit: ")
        if user_input == "done":
            break
        else:
            if forward_chaining(user_input):
                print("Issue diagnosed!")
            else:
                print("Not enough information to diagnose the issue.")

# Call the main function
if __name__ == "__main__":
    main()
