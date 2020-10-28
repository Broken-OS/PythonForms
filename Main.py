from __future__ import print_function
from PyInquirer import style_from_dict, Token, prompt
import pyfiglet

welcome = pyfiglet.figlet_format("Welcome")
print(welcome)
print("to Python Forms! Just answer the questions and the quiz is created for you!")

style = style_from_dict({
    Token.Separator: '#cc5454',
    Token.QuestionMark: '#0D101E',
    Token.Selected: '#cc5454',  # default
    Token.Pointer: '#673ab7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#f44336 bold',
    Token.Question: '',
})

questions = [
    {
        'type': 'input',
        'message': 'Form Title:',
        'name': 'title',
        'default': 'New Form'
    },
    {
        'type': 'list',
        'message': 'Choose type of first question:',
        'name': 'question1type',
        'choices': ['Multiple Choice', "Text", "True or False"]
    },
    {
        'type': 'input',
        'message': 'Correct answer:',
        'name': 'question1choiceanswer',
        'when': lambda answers: answers['question1type'] == 'Multiple Choice'
    },
    {
        'type': 'input',
        'message': 'Question 1:',
        'name': 'question1'
    },
    {
        'type': 'input',
        'message': 'Choice 1:',
        'name': 'question1choice1',
        'when': lambda answers: answers['question1type'] == 'Multiple Choice'
    },
    {
        'type': 'input',
        'message': 'Answer:',
        'name': 'question1textanswer',
        'when': lambda answers: answers['question1type'] == 'Text'
    },
    {
        'type': 'input',
        'message': 'Choice 2:',
        'name': 'question1choice2',
        'when': lambda answers: answers['question1type'] == 'Multiple Choice'
    },
    {
        'type': 'input',
        'message': 'Choice 3:',
        'name': 'question1choice3',
        'when': lambda answers: answers['question1type'] == 'Multiple Choice'
    },
    {
        'type': 'input',
        'message': 'Choice 4:',
        'name': 'question1choice4',
        'when': lambda answers: answers['question1type'] == 'Multiple Choice'
    },
    {
        'type': 'list',
        'message': 'Is the correct answer true or false?',
        'name': 'question1tfanswer',
        'choices': ['True', 'False'],
        'when': lambda answers: answers['question1type'] == 'True or False'
    },
]

answers = prompt(questions, style=style)
open("answers.txt", "w").write(str(answers))
print(open('answers.txt', 'r').read())
