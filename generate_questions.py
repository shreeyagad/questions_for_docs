import torch
from questiongenerator import QuestionGenerator
from questiongenerator import print_qa

def generate_questions(payload): 
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    if not torch.cuda.is_available():
        print("Not using CUDA. Set: Runtime > Change runtime type > Hardware Accelerator: GPU for faster performance.")
    qg = QuestionGenerator()
    qa_list = qg.generate(
        payload['input_text'] or '', 
        num_questions=payload['user_num_questions'] or 10,
        answer_style=payload['user_answer_style'] or 'all'
    )
    print_qa(qa_list)
    return qa_list

with open('indian_matchmaking.txt', 'r') as a:
    indian_matchmaking = a.read()

payload = {
    'input_text': indian_matchmaking,
    'user_num_questions': 10,
    'user_answer_style': 'all'
}

generate_questions(payload)