from orgquestions import Questions

# Create an instance of Questions
questions_instance = Questions()

# Distribute questions
num_questions_per_llm = 54
total_llms = 27
assigned_questions = questions_instance.distribute_questions(num_questions_per_llm, total_llms)

questions_instance = Questions()
num_questions_per_llm = 54
total_llms = 27
assigned_questions = questions_instance.distribute_questions(num_questions_per_llm, total_llms)

# Function to write all LLM questions to a single file
def save_all_llms_to_file(assigned_questions, filename="llm_questions_output.txt"):
    with open(filename, "w") as file:
        for i, questions in enumerate(assigned_questions, start=1):
            file.write(f"LLM {i} Questions:\n")
            file.write(f"Number of questions assigned: {len(questions)}\n")
            file.write(f"{questions}\n\n")
    print(f"All LLM questions saved to {filename}")

# Call the function to save all LLM questions to a file
save_all_llms_to_file(assigned_questions)