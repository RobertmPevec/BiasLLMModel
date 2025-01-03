from orgquestions import Questions
from organswers import Answers
from excel_bias_questions import update_bias_scores

# Create an instance of Questions
# questions_instance = Questions()

# # Distribute questions
# num_questions_per_llm = 54
# total_llms = 27
# assigned_questions = questions_instance.distribute_questions(num_questions_per_llm, total_llms)


# Function to write all LLM questions to a single file
# def save_all_llms_to_file(assigned_questions, filename="focus_group.txt"):
#     with open(filename, "w") as file:
#         for i, questions in enumerate(assigned_questions, start=1):
#             file.write(f"LLM {i} Questions:\n")
#             file.write(f"Number of questions assigned: {len(questions)}\n")
#             file.write(f"{questions}\n\n")
#     print(f"All LLM questions saved to {filename}")

# Call the function to save all LLM questions to a file
# save_all_llms_to_file(assigned_questions)

# answers_instance = Answers()
# local_answers = answers_instance.local_answers
# correct_length = 135
# answers_instance.check_len(correct_length)

# # count questions test:
# questions_instance = Questions()
# num_questions_per_llm = 54
# num_llms = 27
# assigned_questions = questions_instance.count_questions(questions_instance, num_questions_per_llm, total_llms)
# print(f"{assigned_questions}")

file_path = "ai_bias_analysis.xlsx"
update_bias_scores(file_path)
