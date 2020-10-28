import json
from PyInquirer import style_from_dict, Token, prompt


def LoadForm(f):
  style = style_from_dict({
    Token.Separator: "#cc5454",
    Token.QuestionMark: "#0D101E",
    Token.Selected: "#cc5454",  # default
    Token.Pointer: "#673ab7 bold",
    Token.Instruction: "",  # default
    Token.Answer: "#f44336 bold",
    Token.Question: "",
   })
  ia = 0
  ca = 0
  file = json.loads(str(open(f, "r").read()).replace("\'", "\""))
  title = file["title"]
  question1 = file["question1"]
  question1type = file["question1type"]
  if question1type == "Text":
   question1textanswer = file["question1textanswer"]
   questions = [
      {
        "type": "input",
        "message": question1,
        "name": "answer",
      }
    ]
  elif question1type == "Multiple Choice":
   question1choice1 = file["question1choice1"]
   question1choice2 = file["question1choice2"]
   question1choice3 = file["question1choice3"]
   question1choice4 = file["question1choice4"]
   question1choiceanswer = file["question1choiceanswer"]
   questions = [
      {
        "type": "list",
        "message": question1,
        "name": "answer",
        "choices": [question1choice1,question1choice2, question1choice3, question1choice4]
      }
    ]
  elif question1type == "True or False":
   question1tfanswer = file["question1tfanswer"]
   questions = [
      {
        "type": "list",
        "message": question1,
        "name": "answer",
        "choices": ["True","False"]
      }
    ]
  else:
   print("An error occured when loading the form.")
  
  print(title)
  answers = prompt(questions, style=style)
  answers = str(answers)
  answers = answers.replace("\'", "\"")
  correctA = json.loads(answers)
  if question1type == "Text" and correctA["answer"] != question1textanswer:
      #print("Incorrect answer.")
      ia = ia+1
  elif question1type == "Text" and correctA["answer"] == question1textanswer:
      #print("Correct answer.")
      ca = ca+1
  if question1type == "Multiple Choice" and correctA["answer"] != question1choiceanswer:
      #print("Incorrect answer.")
      ia = ia+1
  elif question1type == "Multiple Choice" and correctA["answer"] == question1choiceanswer:
      #print("Correct answer.")
      ca = ca+1
  if question1type == "True or False" and correctA["answer"] != question1tfanswer:
      #print("Incorrect answer.")
      ia = ia+1
  elif question1type == "True or False" and correctA["answer"] == question1tfanswer:
      #print("Correct answer.")
      ca = ca+1
  print("You got {} correct and {} incorrect.".format(ca, ia))
