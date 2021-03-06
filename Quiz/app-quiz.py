from Question import Question

question_prompts = [
    "Whats color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "Whats color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "Whats color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

right_questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(right_questions)