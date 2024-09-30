import random
import time
#Deck of 108 UNO Cards
deck = [
    # Red cards
    ['Red', 0], ['Red', 1], ['Red', 1], ['Red', 2], ['Red', 2], ['Red', 3], ['Red', 3], ['Red', 4], ['Red', 4],
    ['Red', 5], ['Red', 5], ['Red', 6], ['Red', 6], ['Red', 7], ['Red', 7], ['Red', 8], ['Red', 8], ['Red', 9], ['Red', 9],
    ['Red', 'Skip'], ['Red', 'Skip'], ['Red', 'Reverse'], ['Red', 'Reverse'], ['Red', 'Draw 2'], ['Red', 'Draw 2'],
    
    # Yellow cards
    ['Yellow', 0], ['Yellow', 1], ['Yellow', 1], ['Yellow', 2], ['Yellow', 2], ['Yellow', 3], ['Yellow', 3],
    ['Yellow', 4], ['Yellow', 4], ['Yellow', 5], ['Yellow', 5], ['Yellow', 6], ['Yellow', 6], ['Yellow', 7], ['Yellow', 7],
    ['Yellow', 8], ['Yellow', 8], ['Yellow', 9], ['Yellow', 9],
    ['Yellow', 'Skip'], ['Yellow', 'Skip'], ['Yellow', 'Reverse'], ['Yellow', 'Reverse'], ['Yellow', 'Draw 2'], ['Yellow', 'Draw 2'],
    
    # Green cards
    ['Green', 0], ['Green', 1], ['Green', 1], ['Green', 2], ['Green', 2], ['Green', 3], ['Green', 3], ['Green', 4], 
    ['Green', 4], ['Green', 5], ['Green', 5], ['Green', 6], ['Green', 6], ['Green', 7], ['Green', 7], ['Green', 8], 
    ['Green', 8], ['Green', 9], ['Green', 9],
    ['Green', 'Skip'], ['Green', 'Skip'], ['Green', 'Reverse'], ['Green', 'Reverse'], ['Green', 'Draw 2'], ['Green', 'Draw 2'],
    
    # Blue cards
    ['Blue', 0], ['Blue', 1], ['Blue', 1], ['Blue', 2], ['Blue', 2], ['Blue', 3], ['Blue', 3], ['Blue', 4], ['Blue', 4], 
    ['Blue', 5], ['Blue', 5], ['Blue', 6], ['Blue', 6], ['Blue', 7], ['Blue', 7], ['Blue', 8], ['Blue', 8], ['Blue', 9], ['Blue', 9],
    ['Blue', 'Skip'], ['Blue', 'Skip'], ['Blue', 'Reverse'], ['Blue', 'Reverse'], ['Blue', 'Draw 2'], ['Blue', 'Draw 2'],

    # Wild cards
    ['Wild', ''], ['Wild', ''], ['Wild', ''], ['Wild', ''],
    ['Wild', 'Draw 4'], ['Wild', 'Draw 4'], ['Wild', 'Draw 4'], ['Wild', 'Draw 4']
]

discard_pile=[]
draw_pile=deck

mycolors = { "Red" : "\x1b[31m"  , "Yellow": "\x1b[33m" , "Blue": "\x1b[34m" , "Green": "\x1b[32m" ,"Wild": ""}

#fuction randomly distributes 7 cards and removes those cards from the draw pile
def distribute_cards():
    player_cards=[]
    for i in range(7):
        card=random.choice(deck)
        player_cards.append(card)
        draw_pile.remove(card)
    return player_cards


#lay the first card, NOT SPECIAL/WILD cards
def first_card():
    first_card=(random.choice(draw_pile))
    for i in draw_pile:
        if first_card[0] in ["Red",'Yellow','Green','Blue'] and 0<=(first_card[1])<=9:
            break
        else:
            first_card=(random.choice(draw_pile))
    discard_pile.append(first_card)  
    return first_card

def draw_pile_checker(draw_pile):
    counter=0
    for card in draw_pile:
        counter+=1
    if counter<5:
            draw_pile=deck
    


#computer decision 
def next_move(top_card,player_cards,human):
    for card in player_cards:
        if card[0]==top_card[0] or  card[0] == 'Wild' or card[1]==top_card[1]:
            if card[0] == 'Wild':
                card[0]=random.choice(["Red","Blue",'Green',"Yellow"])
                discard_pile.append(card)
                player_cards.remove(card)
                if card[1]=='Draw 4':
                    for i in range(4):
                        remove_c=random.choice(draw_pile)
                        human.append(remove_c)
                        draw_pile.remove(remove_c)
                    return "Human Draw 4"
                else:
                    return "Computer played a card"
            
            elif card[1]=='Draw 2':
                for i in range(2):
                        remove_c=random.choice(draw_pile)
                        human.append(remove_c)
                        draw_pile.remove(remove_c)
                return "Human Draw 2"
            elif card[1]=="Skip":
                discard_pile.append(card)
                player_cards.remove(card)
                next_move(discard_pile[-1],player_cards,human)
                return "Computer skipped you"
            else:
                discard_pile.append(card)
                player_cards.remove(card)
                return "Computer played a card"
        else:
            continue
    pick_up_card=random.choice(deck)
    player_cards.append(pick_up_card)
    draw_pile.remove(pick_up_card)
    return "No playerable cards"

#to choose colour
def get_color_choice():
    while True:
        try:
            color = int(input(f"You're playing a wild card, select the number associated with color: {mycolors['Red']}\n1. Red {mycolors['Blue']}\n2. Blue {mycolors['Green']}\n3. Green {mycolors['Yellow']}\n4. Yellow \nYour choice: "))
            if 1 <= color <= 4:
                return ["Red", "Blue", "Green", "Yellow"][color - 1]
            else:
                print("Please select a valid number (1-4).")
        except ValueError:
            print("Invalid input. Please enter a number.")
 
 #compares top card and user's selected card,checks if its playerble and returns any penalties(special cards)   
def move_analyse(top_card,human_card,human_deck,computer):
    if (top_card[1]==human_card[1]) or top_card[0]==human_card[0] or human_card[0]=='Wild':
        if human_card[0] == 'Wild':
            print("choose clolour")
            chosen_color = get_color_choice()
            print(chosen_color)
            human_card[0] = chosen_color
            print(human_card)
            discard_pile.append(human_card)
            human_deck.remove(human_card)
            if human_card[1]=='Draw 4':
                for i in range(4):
                    remove_card=random.choice(draw_pile)
                    computer.append(remove_card)
                    draw_pile.remove(remove_card)
            print("Computer Picked up 4 cards")
            return human_deck
        elif human_card[1]=="Skip":
            print("Computer got skipped")
            print()
            print(f"\033[35mTop card: {mycolors[discard_pile[-1][0]]} {discard_pile[-1][0]} {discard_pile[-1][1]}")
            print()
            print(f"\033[39mYour cards:")
            print()
            x=1
            human_deck.remove(human_card)
            top_card.append(human_card)
            for i in human_deck:
                print ("\x1b[37m " + str(x) + ".", end = " " )
                print (f'{mycolors[i[0]]} {i[0]} {i[1]}')
                x+=1
            print()
            print(f"\033[31mComputer's cards: ({len(computer)} Hidden cards)")
            print()
            while True:
                try:
                    choice = int(input(f"\033[39mChoose a card to play (1-{len(human_deck)}) or type 0 to draw a card: ")) - 1
                    if choice>(len(human_deck)-1) or choice<-1:
                        print(f"Input must be between 1 and {len(human_deck)}")

                    else:
                        break
                    
                except ValueError:
                    print("Input must be number")
            if choice == -1:
                pick_up_card = random.choice(draw_pile)
                human_deck.append(pick_up_card)
                draw_pile.remove(pick_up_card)
                print(f"\033[30mYou drew: {pick_up_card}")
                return human_deck
            else:
                human_card = human_deck[choice]
                human_deck = move_analyse(discard_pile[-1], human_card, human_deck,computer)
                return human_deck
        elif human_card[1]=="Draw 2":
            human_deck.remove(human_card)
            for i in range(2):
                    remove_card=random.choice(draw_pile)
                    computer.append(remove_card)
                    draw_pile.remove(remove_card)
            print("Computer Picked up 2 cards")
            return human_deck
        else:
            #othercolour special cards
            discard_pile.append(human_card)
            human_deck.remove(human_card)
            return human_deck
    pick_up_card=random.choice(deck)
    human_deck.append(pick_up_card)
    draw_pile.remove(pick_up_card)
    return human_deck


def main():
    print("Welcome to UNO Comsole,😉😉 a developer's game😉😉")
    
    while True:
        try:
            start=int(input("Would you like to start?(CHOOSE NUMBER ASSOCIATED WITH ANSWER) \n1. Y\n2. N\nAnswer?: \n"))
            if start==1:
                break
            else:
                print("Come on mate, you run me to cancel. Make the right decision. I promise I'm fun")
        except:    # Blue cardsef draw_pile_checker(draw_pile):
            print("Don't make me mad blud, follow the instructions")
    human=distribute_cards()
    computer=distribute_cards()
    first_card()
  
    
    while len(human) > 0 and len(computer) > 0:
        if len(human)==1:
            print("\n\033[32mHuman: UNO\n")
        if len(computer)==1:
            print("\n\033[31mComputer: UNO\n")
        print()
        print(f"\033[35mTop card: {mycolors[discard_pile[-1][0]]} {discard_pile[-1][0]} {discard_pile[-1][1]}")
        print()
        print(f"\033[39mYour cards:")
        print()
        x=1
        for i in human:
            print ("\x1b[37m " + str(x) + ".", end = " " )
            print (f'{mycolors[i[0]]}{i[0]} {i[1]}')
            x+=1
        print()
        print(f"\033[31mComputer's cards: ({len(computer)} Hidden cards)")
        print()
        while True:
            try:
                choice = int(input(f"\033[39mChoose a card to play (1-{len(human)}) or type 0 to draw a card: ")) - 1
                if choice>(len(human)-1) or choice<-1:
                    print(f"Input must be between 0 and {len(human)}")
                else:
                    break
                
            except ValueError:
                print("Input must be number")
        if choice == -1:
            pick_up_card = random.choice(draw_pile)
            human.append(pick_up_card)
            draw_pile.remove(pick_up_card)
            print(f"\033[30mYou drew: {pick_up_card}")
        else:
            human_card = human[choice]
            human = move_analyse(discard_pile[-1], human_card, human,computer)
        if not human:
            print("\033[32m🎉🎉congratulations, you have won🎉🎉")
            break
        
        print("\033[31mComputer's turn...\n")
        result = next_move(discard_pile[-1], computer,human)
        if not computer:
            print("\033[31mGame over,😞😞You lose😞😞")
            break
        draw_pile_checker(draw_pile)
        time.sleep(2)
        print(result)
        time.sleep(1) 
if __name__=="__main__":
    main()




      
    
    
    
    
