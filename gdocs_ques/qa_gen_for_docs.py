import torch
from .questiongenerator import QuestionGenerator
from .questiongenerator import print_qa

def load_model():
     return QuestionGenerator()

def get_qa(model, text_data, num_questions, answer_style): 
    qa_list = model.generate(
        text_data,
        num_questions=num_questions,
        answer_style=answer_style
    )
    return qa_list
