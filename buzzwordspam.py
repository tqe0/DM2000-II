import keyboard as kb
import random as r
import time as t
import pyautogui


pro_ai = [
    "Synthetic agency accelerates ontological convergence between probabilistic reasoning and socio-technical legitimacy.",
    "Post-symbolic cognition renders anthropocentric intelligence metrics fundamentally obsolete.",
    "Hypernormalization emerges from stochastic governance embedded within predictive computational infrastructures.",
    "Decentralized alignment paradoxically amplifies systemic value incoherence across autonomous agent ecologies.",
]

anti_ai = [
    "Opaque decision-making in large-scale models undermines meaningful accountability for downstream harms.",
    "Automation of cognitive labor risks concentrating economic power among a narrow set of infrastructure owners.",
    "Statistical pattern-matching lacks the grounded understanding required for robust generalization beyond training distribution.",
    "Widespread deployment outpaces the development of adequate governance and safety verification frameworks.",
    "Synthetic content proliferation erodes epistemic trust in shared informational ecosystems.",
]

pro_communism = [
    "Collective ownership of production abolishes the structural exploitation inherent to wage labor.",
    "Class stratification dissolves when capital is subordinated to communal planning.",
    "Historical materialism reveals capitalism as a transitional, not terminal, economic stage.",
    "Surplus value redistribution under common ownership eliminates systemic worker alienation.",
    "Centralized planning enables resource allocation oriented toward need rather than profit extraction.",
]

pro_capitalism = [
    "Centralized planning historically struggles to replicate the price signaling efficiency of markets.",
    "Concentration of economic control in state apparatus creates significant opportunity for authoritarian drift.",
    "Absence of private incentive structures correlates with reduced innovation velocity in empirical case studies.",
    "Information asymmetries make comprehensive central planning computationally and administratively intractable at scale.",
    "Historical implementations have frequently coincided with suppression of political pluralism and civil liberties.",
]


def print_options():
    choiceslist = {"1": "communism",
                   "BLANK": "",
                   "2": "ai",
                   "BLANK1": "",
                   "3": "full name",
                   "BLANK2": "",
                   "q": "to quit",}

    for k, v in choiceslist.items():
        if "BLANK" not in k:
            print(f"{k}: {v}")
        else:
            print()

def countdown():
    print("tab into game")
    pause = 0.5
    for i in range(5, 0, -1):
        print(i)
        t.sleep(pause)


def send_arguments(arguments):
    delay = 0.25
    chat_key = '/'
    send_key = 'enter'
    typespeed = 0.01
    message_count = 5

    for _ in range(message_count):
        if kb.is_pressed('esc'):
            print("aborted")
            break
        response = r.choice(arguments)
        kb.press_and_release(chat_key)
        t.sleep(delay)
        pyautogui.typewrite(response, interval=typespeed)
        t.sleep(delay)
        kb.press_and_release(send_key)


def main():
    print_options()
    while True:
        choice = input(">>> ")

        match choice:
            case "1":
                side = input("select Y for pro communism N for pro capitalism ").upper()
                if side == "Y":
                    countdown()
                    send_arguments(pro_communism)
                elif side == "N":
                    countdown()
                    send_arguments(pro_capitalism)
                else:
                    print("select Y/N")
            case "2":
                side = input("Y for pro ai N for anti-ai ").upper()
                if side == "Y":
                    countdown()
                    send_arguments(pro_ai)
                elif side == "N":
                    countdown()
                    send_arguments(anti_ai)
                else:
                    print("select Y/N")
            case "q":
                break
            case _:
                print("typo probably")


if __name__ == "__main__":
    main()