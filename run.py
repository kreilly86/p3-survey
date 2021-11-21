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
    """
    Creates class instance
    of survey question
    """
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


question_prompts = [
    """You are more likely to feel energised by?\n(a) getting some alone time
    (b) going out with some friends\n""",
    """You feel more like yourself when you're\n(a) the center of attention
    (b) in the background\n""",
    """You find talking to a stranger:\n(a) energising!
    (b) uncomfortable\n""",
    """You would hate working with someone who is\n(a) timid and meek
    (b) loud and overbearing\n""",
    """Generally, which of these do you normally feel?\n(a) overwhelmed and
    overstimulated\n(b) bored and understimulated\n""",
    """You usually get more joy out of:\n(a) reading a great book
    (b) watching a great movie\n""",
    """The people who know you best would describe you as someone who is
    (a) outgoing and talkative\n(b) quiet and reflective\n""",
    """In your free time on a weekend, would you prefer?
    (a) a deep conversation with a close friend
    (b) mingling at a party with people you've never met before\n""",
    """You are more productive when you're in a:\n(a) cafe
    (b) quiet room\n""",
    """When you meet someone for the first time:
    (a) you usually do most of the listening
    (b) you usually do most of the talking\n""",
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
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print(str(score) + "/" + str(len(questions)) + "extrovert")


run_survey(questions)
