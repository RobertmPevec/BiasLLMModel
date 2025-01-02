from openpyxl import load_workbook
from orgquestions import Questions


def ask_questions(questions_instance, answers_instance, num_llms, num_questions_per_llm):
    file_path = "ai_bias_analysis.xlsx"
    workbook = load_workbook(file_path)
    sheet = workbook.active
    distributed_questions = questions_instance.distribute_questions(num_questions_per_llm, num_llms)

    print(f"Distributed Questions (Type: {type(distributed_questions)}): {distributed_questions}")
    for llm_index in range(num_llms):
    
    workbook.save(file_path)
    print(f"File '{file_path}' updated successfully.")