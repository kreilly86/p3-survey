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

print('-------------------------------------------')
print('----Welcome to the Personality Profiler----')
print("  -----Let's explore your traits!-----\n")


class Question:
    """
    Creates class instance
    of survey question
    """
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


question_prompts = [
    """You are more likely to feel energised by?
    (a) Getting some alone time
    (b) Going out with some friends\n""",
    """You feel more like yourself when you're
    (a) The center of attention
    (b) In the background\n""",
    """You find talking to a stranger:
    (a) Energising!
    (b) Uncomfortable\n""",
    """You would hate working with someone who is
    (a) Timid and meek
    (b) Loud and overbearing\n""",
    """Generally, which of these do you normally feel?
    (a) Overwhelmed and overstimulated
    (b) Bored and understimulated\n""",
    """You usually get more joy out of:
    (a) Reading a great book
    (b) Watching a great movie\n""",
    """The people who know you best would describe you as someone who is
    (a) Outgoing and talkative
    (b) Quiet and reflective\n""",
    """In your free time on a weekend, would you prefer?
    (a) A deep conversation with a close friend
    (b) Mingling at a party with people you've never met before\n""",
    """You are more productive when you're in a:
    (a) Cafe
    (b) Quiet room\n""",
    """When you meet someone for the first time:
    (a) You usually do most of the listening
    (b) You usually do most of the talking\n\n""",
]

# questions with answer equating to extraversion quality

questions = [
    Question(question_prompts[0], "b"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "a"),
    Question(question_prompts[3], "a"),
    Question(question_prompts[4], "a"),
    Question(question_prompts[5], "b"),
    Question(question_prompts[6], "a"),
    Question(question_prompts[7], "b"),
    Question(question_prompts[8], "a"),
    Question(question_prompts[9], "b"),
]


def run_survey(questions):
    """
    Generate 10 questions for user returning
    a score out of 10 for extroversion
    """
    global score
    score = 0
    for question in questions:
        global answer
        answer = input(question.prompt)
        validate_input(answer)
        if answer == question.answer:
            score += 1
    global result
    result = str(score) + "/" + str(len(questions))
    return result


def validate_input(answer):
    """
    Checks if user answer
    is valid, either "a" or "b".
    Prints error message to terminal
    if invalid
    """
    not_valid = True

    while not_valid:
        if answer not in ['a', 'b']:
            print('Invalid input. Please enter either a or b\n')
        not_valid = False
        continue


def calculate_trait(score, result):
    """
    Retrieve result of survey
    and calculate if user is
    an introvert, extrovert
    or ambivert
    """
    if score >= 7:
        print(f'\nYou scored {result} you are an extrovert!')
    elif score <= 4:
        print(f'\nYou scored {result} you are an introvert!')
    else:
        print(f'\nYou scored {result} you are an ambivert!')


run_survey(questions)
calculate_trait(score, result)
