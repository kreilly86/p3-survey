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
print("  -----Let's explore your trait!-----\n\n")
print('First we would like to ask for some details\n')


def capture_user():
    """
    Get user info such as
    name, age etc
    """
    global name
    name = input("Please enter your name:\n\n")
    print("Hello", name + "!\n")

    global age
    age = input("Please enter your age:\n\n")

    global gender
    gender = input("Please enter your gender. Male, female or non-binary\n\n")

    global location
    location = input("Please enter the city you live in\n\n")

    print("""\nThank you! Now let's dive in and find out more about
    your personality""")


def update_survey_worksheet(values):
    """
    Updates survey spreadsheet with
    user details
    """
    survey_worksheet = SHEET.worksheet("survey")

    survey_worksheet.append_row(values)


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
        while True: 
            global answer
            answer = input(question.prompt)
            if validate_input(answer):
                break

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
    if answer not in ['a', 'b']:
        print('Invalid input. Please enter either a or b\n')
        return False
    return True


def calculate_trait(score, result):
    """
    Retrieve result of survey
    and calculate if user is
    an introvert, extrovert
    or ambivert
    """
    if score >= 7:
        print(f'\nYou scored {result} you are an extrovert!\n\n')
        return 'extrovert'
    elif score <= 4:
        print(f'\nYou scored {result} you are an introvert!\n\n')
        return 'introvert'
    else:
        print(f'\nYou scored {result} you are an ambivert!\n\n')
        return 'ambivert'


pandemic_prompts = [
    """Question 1.What was your reaction to the dramatic change in
    social contact the pandemic brought about?\n
    (a) I was relieved! It gave me time and space to focus
    on myself and not have pressure to socialise all the time
    (b) It was extremely hard. I missed socialising and
    felt something major was missing from my life\n""",
    """Question 2.Did you notice any change in how you relate
    to other people. e.g. if you are introverted did you become
    more extroverted i.e. doing more zoom calls, if you are extroverted
    did you become more introverted i.e. you became less outward
    and focused on your interal world a little more\n
    (a) No,I feel like nothing changed in me and how I naturally relate to
     others
    (b) Yes,I feel like I changed and my personality type became less set\n""",
    """Question 3.During the lockdowns do you feel you learned new skills
    or took time to do a hobby you always wanted to?
    (a) Yes! I learned a new skill or took up a hobby I always wanted to
    (b) No. I wish I used the time to learn new skills or take up a hobby\n""",
    """Question 4. Did you, like many people decide to buy/adopt a pet during the
    stay at home period of the pandemic?
    (a) No! I either had a pet already or didn't get one during the pandemic
    (b) Yes! I adopted/bought a pet during lockdown. \n""",
    """Question 5.Do you feel like you really missed activities we used to take
    for granted e.g. going to a restaurant or meeting friends for drinks?
    (a) Yes! I really missed activities that were disallowed in the pandemic
    (b) No, not really I managed just fine!\n""",
]

pandemic_questions = [
    Question(pandemic_prompts[0], "a"),
    Question(pandemic_prompts[1], "b"),
    Question(pandemic_prompts[2], "a"),
    Question(pandemic_prompts[3], "b"),
    Question(pandemic_prompts[4], "a"),
]


def opinion_data(pandemic_questions):
    """
    Ask a set of 5 questions
    to find out users' opinion
    on how the pandemic has effected
    how they see their personality
    type, and if they notice any changes
    """
    print('Now we have discovered your personality type')
    print(',we would like to ask a few questions')
    print('relating to your experience of the pandemic\n')
    q_a_map = {}
    count = 1
    for question in pandemic_questions:
        global answer
        answer = input(question.prompt)
        validate_input(answer)
        if answer == question.answer:
            print('You answered yes\n')
        q_a_map[count] = answer
        count += 1
    return q_a_map


capture_user()
run_survey(questions)
trait = calculate_trait(score, result)
answer_list = [name, age, gender, location, trait]
key_map = opinion_data(pandemic_questions)

for key, i in key_map.items():
    answer_list.append(i)
    print(answer_list)

update_survey_worksheet(answer_list)
