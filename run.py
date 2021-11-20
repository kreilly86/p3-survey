import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('personality_profiler')


print('----Welcome to the Personality Profiler----')
print("  -----Let's explore your traits!-----\n")

class Question: 
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


question_prompts = [
    "You are more likely to feel energised by?\n(a) getting some alone time\n(b) going out with some friends\n\n",
    "You feel more like yourself when you're...\n(a) the center of attention\n(b) in the background\n\n",
    "You find talking to a stranger:\n(a) energising!\n(b) uncomfortable\n\n",
    "You would hate working with someone who is:\n(a) timid and meek\n(b) loud and overbearing\n\n",
    "Generally, which of these do you normally feel?\n(a) overwhelmed and overstimulated\n(b) bored and understimulated\n\n",
    "You usually get more joy out of:\n(a) reading a great book\n(b) watching a great movie\n\n",
    "The people who know you best would describe you as someone who is...\n(a) outgoing and talkative\n(b) quiet and reflective\n\n",
    "In your free time on a weekend, would you prefer?\n(a) a deep conversation with a close friend\n(b) mingling at a party with people you've never met before\n\n",
    "You are more productive when you're in a:\n(a) cafe\n(b) quiet room\n\n",
    "When you meet someone for the first time:\n(a) you usually do most of the listening\n(b) you usually do most of the talking\n",
] 

# question with answers equating to extraversion quality

questions = [
    Question(question_prompts[0], "b"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "a"),
    Question(question_prompts[3], "a"),
    Question(question_prompts[4], "b"),
    Question(question_prompts[5], "b"),
    Question(question_prompts[6], "a"),
    Question(question_prompts[7], "b"),
    Question(question_prompts[8], "a"),
    Question(question_prompts[9], "b"),
]

def run_survey(questions):
    """
    Generate questions for user
    with input fields giving
    a score out of 10 for extroversion
    """
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print(str(score) + "/" + str(len(questions)) + "extrovert")

run_survey(questions)


