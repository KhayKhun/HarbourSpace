"""
Sai Khay Khun Mong
Intro to Programming 1: Python
M2 - BKK - 2024
Final Project
"""

import random
displayStages = [
    """
------------------------
|                      |
|                      |
|                      |
|                      |
|                      |
|                      |
------------------------
    """,
    """
------------------------
|         -----        |
|                      |
|                      |
|                      |
|                      |
|                      |
------------------------
    """,
    """
------------------------
|         -----        |
|         |   |        |
|                      |
|                      |
|                      |
|                      |
------------------------
    """,
    """
------------------------
|        -----         |
|        |   |         |
|        |   O         |
|                      |
|                      |
|                      |
------------------------
    """,
    """
------------------------
|        -----         |
|        |   |         |
|        |   O         |
|        |  /|         |
|                      |
|                      |
------------------------
    """,
    """
------------------------
|        -----         |
|        |   |         |
|        |   O         |
|        |  /|\\        |
|        |  /          |
|                      |
------------------------
    """,
    """
------------------------
|        -----         |
|        |   |         |
|        |   O         |
|        |  /|\\        |
|        |  / \\        |
|                      |
------------------------
    """,
]

data = [
    {"word": "python", "set": set("python"), "hint": "A popular programming language."},
    {"word": "hangman", "set": set("hangman"), "hint": "A classic word-guessing game."},
    {"word": "programming", "set": set("programming"), "hint": "The process of writing computer code."},
    {"word": "challenge", "set": set("challenge"), "hint": "A task or problem that tests someone's abilities."},
    {"word": "development", "set": set("development"), "hint": "The process of developing something."},
    {"word": "algorithm", "set": set("algorithm"), "hint": "A step-by-step procedure for solving a problem."},
    {"word": "function", "set": set("function"), "hint": "A block of code that performs a specific task."},
    {"word": "variable", "set": set("variable"), "hint": "A storage location identified by a name."},
    {"word": "syntax", "set": set("syntax"), "hint": "The set of rules that defines the combinations of symbols."},
    {"word": "exception", "set": set("exception"), "hint": "An error that occurs during program execution."},
    {"word": "iteration", "set": set("iteration"), "hint": "The repetition of a process in programming."},
    {"word": "debugging", "set": set("debugging"), "hint": "The process of finding and fixing errors in code."},
    {"word": "compiler", "set": set("compiler"), "hint": "A program that translates code into machine language."},
    {"word": "library", "set": set("library"), "hint": "A collection of precompiled routines that a program can use."},
    {"word": "framework", "set": set("framework"), "hint": "A platform for developing software applications."},
    {"word": "database",  "set": set("database"),  "hint":"An organized collection of data, generally stored electronically."},
    {"word":"interface",  "set" : set("interface"),  "hint":"A shared boundary across which two or more separate components exchange information."},
    {"word":"object",  "set" : set("object"),  "hint":"An instance of a class in object-oriented programming."},
    {"word":"module",  "set" : set("module"),  "hint":"A file containing Python definitions and statements."},
    {"word":"repository",  "set" : set("repository"),  "hint":"A storage location for software packages or code."}
]

alreadyEntered = set()
currentCorrectGuesses = set()
mistakes = 0
goal = random.choice(data)

def reset():
    global alreadyEntered
    global currentCorrectGuesses
    global mistakes
    global goal

    alreadyEntered = set()
    currentCorrectGuesses = set()
    mistakes = 0
    goal = random.choice(data)

def isCorrectGuess(target, inputCharacter):
    return inputCharacter in target

def generateLatestString(goalSet, goalString, currentCorrectGuesses):
    diff = goalSet - currentCorrectGuesses
    latestString = []

    for char in goalString:
        if char in diff:
            latestString.append('_')
        else:
            latestString.append(char.upper())
    return latestString


def renderStatus(message):
    lts = generateLatestString(goal["set"], goal["word"], currentCorrectGuesses)
    print("----------------------------------------------")
    print("\nHint:", goal["hint"])
    print(displayStages[mistakes])
    print(message)
    print(f"Your chances: {6 - mistakes}/6")
    print(f".{" ".join(lts)}.")
    print("\n")

def getUserInput():
    val = ""
    while True:
        ip = input('>> ')
        if not ip.isalpha() or len(ip) != 1:
            renderStatus(f'{ip.upper()} is an invalid input! Please try again.')

        elif (ip in alreadyEntered):
            renderStatus(f'You already guessed {ip}. Try another one.')

        else:
            val = ip
            break

    return val

def mainGame():
    while True:
        global mistakes
        if mistakes >= 6:
            renderStatus("------ You Died :( ------")
            print(f"------ The correct answer is {goal["word"].upper()} ------ \n")
            return

        ip = getUserInput()
        alreadyEntered.add(ip)

        if isCorrectGuess(goal["set"], ip):
            currentCorrectGuesses.add(ip)

            renderStatus(f"{ip.upper()} is a correct guess :)")

            if goal["set"] == currentCorrectGuesses:
                renderStatus(f"You won with {mistakes} {"mistake" if mistakes <= 1 else "mistakes"}!")
                return
        else:
            mistakes += 1
            renderStatus(f"{ip.upper()} is a wrong guess :(")


def start():
    end = False
    while not end:
        reset()
        print("\n\n\n\t\t------ WELCOME TO HANGMAN GAME! ------")
        print(displayStages[-1])
        print("Try no to die.")
        input("\nPress Enter to start the game >> \n")
        renderStatus("Please enter a character to start guessing (eg. A [or] a) ")
        mainGame()

        i = input("Press (R) to restart [or] Press any key to quit - ")
        if(i.lower() == 'r'):
            continue
        else:
            break
    
    print("\nThanks for playing!\n")

start()