"""
 CSC 130 Project 2
 Filename: sort_cards_main.py
 Programmer: Alex Lopez Torres Riega
 Date: October 8, 2018

 Description:
    Program that simulates playing a solitaire card game that
    has a special mathematical feature of being able to find
    the longest increasing or decreasing subsequences of the
    shuffled cards.

    This program uses Stacks, Queues, and Linked Lists.

"""

from cardSorter import CardSorter

def main():
    """
    This class contains the mainline logic to play multiple rounds 
    of the Patience Sorting Card game:
       1. Set the variable to determine the number of rounds to play.
       2. For each round create a new CardSorted object which deals 
          Cards from the Deck onto one of several Piles (Stacks) on 
          the table using the rules of the game.
       3. At the same time a deep copy of the Card is placed on the 
          top of a SubSequence (a LinkedList) such that it is pointing 
          to the top Card of the Pile previous to the Pile on which it 
          is placed. 
       4. Prints each longest decreasing SubSequence for each Card in 
          the last Pile
       5. Reverses the longest decreasing SubSequences and prints the 
          longest increasing SubSequences.    
       6. Uses the Card Piles on the table to return a sorted Deck
    """

    rounds = 5
    
    print("Playing {} games.".format(rounds))

    for run in range(rounds):
    
        print("\n=========== Begin Game " + str(run + 1) + " ==========")
        
        sorter = CardSorter()
        sorter.setup()
        sorter.play()
        
        print("=========== End Game " + str(run + 1) + " ==========")

        print("Simulation complete.")
    
main()
