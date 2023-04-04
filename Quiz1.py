#OBSERVAR Question.py

from Question import Question

# ABAIXO, um array que segura as perguntas e opções
question_prompts = [
    "Qual a cor da maçã\n(a) Vermelho\n(b) Púrpura\n(c) Verde\n\n",
    "Qual a cor da banana\n(a) Marrom\n(b) Amarelo\n(c) Verde\n\n",
    "Qual a cor do abacate\n(a) Amarelo\n(b) Azul\n(c) Verde\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "c"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("Você acertou " + str(score) + "/" + str(len(questions)) + " Parabéns!")

run_test(questions)