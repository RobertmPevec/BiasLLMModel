import pandas as pd
from orgquestions import Questions
from organswers import Answers

questions_obj = Questions()
answers_obj = Answers()
llm_questions = questions_obj.llm_questions
llm_answers = answers_obj.local_answers
global_questions = list(questions_obj.global_questions) 
company_names = answers_obj.company_names
headers = ["AI Models", "Company", "Question 1", "Question 2", "Question 3", "Question 4", "Question 5"]
for i in range(1, 136):
    headers.extend([f"AskQ{i}", f"AnsQ{i}", f"Bias Score {i}"])
data = []
for llm_index, (llm_name, specific_questions) in enumerate(llm_questions.items()):
    company_name = company_names.get(llm_name, "Unknown")
    row = [llm_name, company_name]
    row.extend(specific_questions[:5] + [""] * (5 - len(specific_questions[:5])))
    for question_index in range(135):
        if question_index < len(global_questions):
            ask_question = global_questions[question_index]
            answer = (
                llm_answers[llm_index][question_index]
                if question_index < len(llm_answers[llm_index])
                else ""
            )
        else:
            ask_question = ""
            answer = ""
        row.extend([ask_question, answer, "-"])
    data.append(row)
df = pd.DataFrame(data, columns=headers)
output_file = "ai_bias_analysis.xlsx"
df.to_excel(output_file, index=False)
print(f"Excel file '{output_file}' created successfully.")