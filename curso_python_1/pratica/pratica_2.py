import random 

def get_choices()-> dict:

    player_choice = input("Indique a sua opção: (rock, paper, scissors)")
    computer_choice = "papel"

    opcoes = ["rock", "paper", "scissors"]
    computer_choice = random.choice(opcoes)

    choices = {"player": player_choice, "computer": computer_choice}
    return choices 

# Funções são blocos de códigos reutilizáveis 
# executados somente quando chamados. 


# choices = get_choices()
# def greeting():
#     return "Hi"

# print(greeting())


def check_win(dict_result: dict)-> str:

    player_choice = dict_result['player'].lower()
    computer_choice = dict_result['computer'].lower()

    print(f"You chose: {player_choice.capitalize()}")
    print(f"Computer chose: {computer_choice.capitalize()}")


    if player_choice == computer_choice:
        return "tie"

    elif player_choice == "rock":
        if computer_choice == "paper":
            return "computer wins"

        else: 
            return "you won"
        # elif computer_choice == 'scissors':
        #     return "you won"

    elif player_choice == "paper":
        if computer_choice == "rock":
            return "you won"

        else:
            return "computer wins"

    else: 
        if computer_choice == "rock":
            return "computer wins"

        else: 
            return "you won"


    
# food = ["pizza", "arroz", "feijão"]

def main():
    # print(choices)

    choices = get_choices()
    answer = check_win(choices)


    print(answer)

if __name__ == '__main__':
    main()