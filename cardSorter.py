from deck import Deck
from card import Card
from pile import Pile
from subSequence import SubSequence

class CardSorter():
    """
    This class implements the card game simulation using many methods.
    It implements both the sorting card game and the formation and 
    display of the longest subsequences.
    
    The Sort Card Game
    
    1. Initially, there are no piles. 
       The 1st Card dealt forms a new pile consisting of the 1st Card.
    2. As each new Card is dealt from the Deck, a Python list, it must  
       be placed on top of the leftmost (lowest Python list index) 
       Pile, a Stack, whose top Card has a value higher than the 
       new Card's value.
    3. If there are only Piles with top Cards that are lower in value
       than the new Card's value, then use the new Card to start a new 
       Pile (Stack) to the right of all the existing Piles (at end of 
       Python list of Piles)
    4. The game ends when all the cards have been dealt.
    5. After the all Cards have been dealt onto the correct Pile on 
       the table, they are picked back up in sorted order.
    
    Creating and Displaying SubSequences
    
    Dealing the cards in this way provides us a way of retrieving a 
    subset of the longest increasing and decreasing subsequences in 
    the shuffled Deck, where the number of piles is the length of 
    a longest subsequence.
    
    1. As each new Card is placed on the correct Pile (Stack) on the 
       table, this CardSorter's piles, a Python list, it is also 
       placed correctly in a SubSequence (a LinkedList) of Cards 
       forming an ordered subsequence. The ordered subsequence is 
       formed by linked the new Card to the top Card in the previous 
       Pile (the Pile to the left with an index value one lower than 
       the Pile to which the new Card is added). By design, the Pile's
       top Card has a lower value than the value of the new Card.  
    2. The longest decreasing and increasing subsequences for each 
       Card in last Pile (Stack) is displayed. An additional Stack 
       is used to reverse the decreasing SubSequences creating 
       increasing SubSequences
      
    The instances variables of this class include:
    1. self.__deck: the Deck of Cards, using the Deck class; 
                    a Deck is a Python list of Cards
    2. self.__subseqs: a Python list of SubSequences, 
                       each SubSequence is a LinkedList
    3. self.__piles: a Python list of Stacks of Cards, 
                     each Stack is a LinkedList
    4. self.CARDS_IN_DECK: a constant holding the number of Cards 
                           in the Deck
    
    The class methods include: 
    a. __init__: This method creates each instance variable.
    b. setup: This method creates the Deck and shuffles it 5 times
    c. play: This method plays the Card game and forms and displays 
                 the longest SubSequences.  See description below. 
    d. construct_piles_subseqs: This method handles most of this 
                                program's tasks: See description 
                                below.
    e. add_card_to_subseq: This method takes the currently dealt Card 
                       and the top Card from the previous Pile as 
                           parameters and places the currently dealt 
                           Card on the correct position in the list 
                           of SubSequences. See description below.
    f. find_subseq: This method locates the SubSequence on which the 
                    passed in prev_card exists.  It returns the
                    SubSequence or None
    g. display_card_piles: This method displays the Card Piles on the 
                           Python list
    h. display_longest_subseq: This method loops through the 
                               SubSequence Python list and obtains 
                               each SubSequence whose size equals the 
                               number of piles, which is the size of 
                               the longest SubSequences, and displays 
                               the SubSequence.                   
    i. make_sorted_deck: This method makes a sorted Deck by picking 
                         up the smallest Card from the top of the 
                         Piles, one at a time and adding them to end 
                         of the Deck.
    """ 
    
    def __init__(self):
        """
        This method is the constructor for CardSorter. It creates the 
        Deck, a list of Piles and a list of SubSequences and 
        initializes a constant.
        """
        self.__deck = Deck()
        self.__subseqs = list()
        self.__piles = list()
        self.CARDS_IN_DECK = 52
    
    def setup(self):
        """
        This method initializes the Deck and shuffles it 5 times
        then display the shuffled deck..
        """
        self.__deck.initialize()

        for times in range(5):
            self.__deck.shuffle()

        print("\nThe shuffled deck: \n")
        print(self.__deck)

    def play(self):
        """
        This method plays the Card game and forms 
        and displays the SubSequences:
    
        The Algorithm:
    
         1.Construct the Card piles on the table, calling the
           construct_card_piles_subseqs method, which also
           places each dealt Card correctly on the SubSequence list.
         2.Display the Card Piles by calling the 
           display_card_piles method
         3.Display the longest subsequences, calling 
           the Table printLongestSubSeqs method 
         4.Use the piles on the Table to make a sorted Deck,
           calling the Table makeSortedDeck method
         5.Display the sorted Deck directly - no method call
        """
        self.construct_piles_subseqs()
        self.display_card_piles()
        self.display_longest_subseq()
        self.make_sorted_deck()
        print(self.__deck)
        
    def construct_piles_subseqs(self):
        """
        This method handles most of this program's tasks. It creates 
        the Piles of Cards on the table from the Cards dealt from the 
        Deck. It also places the Card in its correct position in the 
        list of SubSequences, linking it to the top Card from the 
        previous Pile.
        
        The Algorithm:
        
        A. Outer Loop for each each Card in the Deck
           1. Retrieve the Card from the Deck: card_from_deck
           2. Set a flag to indicate if we place the 
              card_from_deck in an existing Pile
           3. Inner Loop through each Pile starting from the 
              leftmost Pile - Python list index 0 - to find the
              correct one on which to place the card_from_deck
              a. Obtain a reference to the top Card on the current 
                 Pile(Stack) using peek
              b. If there exists a Pile whose top Card is higher 
                 than the card_from_deck, then
                 i.   Set the flag to say we have found a Pile on 
                      which to place the card_from_deck
                 ii.  Obtain a reference to the top Card on the 
                      previous Pile - the one to the left of where 
                      you just placed the card_from_deck: (one less 
                      index value in Python list) using peek
                 iii. Add the card_from_deck to the list of 
                      SubSequences using the add_card_to_subseq 
                      method
                 iv.  Push the card_from_deck onto the Pile
           4. Check the flag:
              If we haven't found a place for the card_from_deck 
              in an existing Pile, then
              a. Create a new Pile (in Python list of Piles (Stacks)
              b. Obtain a reference to the top Card on the previous 
                 Pile - the one to the left of where you just placed 
                 the card_from_deck: (one less index value in Python 
                 list) using peek - unless this first Card from the 
                 Deck, when the number of Piles are zero, using len 
                 function.
              c. Add the card_from_deck to the list of SubSequences 
                 using the add_card_to_subseq method
              d. Push the card_from_deck onto the Pile
        """
        for card in range(self.CARDS_IN_DECK):
            card_from_deck = self.__deck.deal()
            flag = False
            prev_card = None
            if len(self.__piles) > 0:

                for i in range(len(self.__piles)):
                    top_card = self.__piles[i].get_top_card()
                    if top_card.compare(card_from_deck) > 0:
                        flag = True
                        if i > 0:
                            prev_card = self.__piles[i - 1].get_top_card()
                        self.add_card_to_subseq(card_from_deck, prev_card)
                        self.__piles[i].add_card(card_from_deck)
                        break
            if flag is not True:
                pile = Pile()
                if len(self.__piles) > 0:
                    prev_card = self.__piles[len(self.__piles) - 1].get_top_card()
                self.add_card_to_subseq(card_from_deck, prev_card)
                pile.add_card(card_from_deck)
                self.__piles.append(pile)

    def add_card_to_subseq(self, current_card, prev_card):
        """
        This method adds a copy of the current_card to one of the 
        SubSequences in the SubSequence list. The parameters are
        the current_card and the prev_card. The correct SubSequence
        on which to add the current_card is the one on which the 
        prev_card currently resides.
        
        The Algorithm:
                
        1. Make a copy of the current_card, by passing in the 
           rank and the suit.
        2. Find the SubSequence containing the prev_card by 
           calling the find_subseq method passing in prev_card, 
           which returns a reference to the correct SubSequence.
        3. If there is no SubSequence containing the prev_card, 
           create a new SubSequence and add the copy of the 
           current_card to the new SubSequence and add the new 
           SubSequence to the Python list of SubSequences.
        4. If there was a SubSequence containing the prev_card, 
           then check to see if the prev_card is at the head of  
           the SubSequence by calling first_card method:
           a. If the prev_card is at the head, then just add the 
              copy of the current_card to the front of the 
              SubSequence by calling add_card method linking 
              the two Cards.
           b. If the prev_card is not at the head,then we must
              i.   Copy the SubSequence containing the prev_card 
                   by calling the copy_subseq method
              ii.  Add the copied SubSequence to the Python list 
                   of SubSequences using the append method
              iii. Traverse the copied SubSequence from the head,
                   removing each Card that is not the prev_card
                   by calling the remove_first method.  Be sure to
                   break out of the loop when finding the prev_card.
              iv.  Now, the prev_card is at the front of the copied
                   SubSequence, so we can add the copy of the
                   current_card to the front of the SubSequence by 
                   calling add_card method linking the two Cards.
        
        """
        copied_card = Card(current_card.get_suit(), current_card.get_rank())
        prev_card_subseq = self.find_subseq(prev_card)

        if prev_card_subseq is None:
            new_card_subseq = SubSequence()
            new_card_subseq.add_first(copied_card)
            self.__subseqs.append(new_card_subseq)
        else:
            first_card = prev_card_subseq.first_card()

            if first_card.compare(prev_card) == 0:
                prev_card_subseq.add_first(copied_card)
            else:
                subseq_copy = prev_card_subseq.clone_subseq()
                self.__subseqs.append(subseq_copy)
                for c in range(subseq_copy.get_size()):
                    card = subseq_copy.first_card()
                    if card.compare(prev_card) == 0:
                        break
                    else:
                        subseq_copy.remove_first()
                subseq_copy.add_first(copied_card)
    
    def find_subseq(self, prev_card):
        """
        This method locates the SubSequence on which the passed in 
        prev_card exists. It returns the SubSequence or None. It
        finds the first SubSequence in the Python list of
        SubSequences that contains the prev_card passed in.
        
        The Algorithm:
        
        1. Check that the Card passed in is not null, If so, 
           return null.
        2. Traverse the Python list of SubSequence LinkedLists, 
           checking to see if the SubSequence contains the card 
           passed in
        3. Return the SubSequence when found, or None if not found.
        """
        if prev_card is None:
            return None
        else:
            for sequence in self.__subseqs:
                if sequence.contains_card(prev_card):
                    return sequence
            return None
        
    def display_card_piles(self):
        """
        This method displays the Card Piles on the Python list
        """
        print("The piles:\n")

        for p in self.__piles:
            print(p)

    def display_longest_subseq(self):
        """
        This method traverses the SubSequence Python list twice.  
        The each time through it obtains each SubSequence whose 
        size equals the number of piles, which is the size of the 
        longest SubSequences,  The first time through, it displays 
        each SubSequence, the decreasing ones. The second time 
        through it reverses the SubSequence and then displays the
        increasing ones.
        
        The Algorithm
        1.  Loop through each SubSequence in the Python list
            a. If the length of the SubSequence is equal to the 
               number of Piles, print the SubSequence
        2. Loop through each SubSequence in the Python list
            a. If the length of the SubSequence is equal to the 
               number of Piles:
               i.   Clone the SubSequence
               ii.  Reverse the SubSequence
               iii. Print the SubSequence          
        """
        
        print("\nLongest Decreasing Sub-Sequences: \n")

        for seqs in self.__subseqs:
            if seqs.get_size() == len(self.__piles):
                print(seqs)
        
        print("\nLongest Increasing Sub-Sequences: \n")
        
        for seq in self.__subseqs:
            if seq.get_size() == len(self.__piles):
                cloned_subseq = seq.clone_subseq()
                cloned_subseq.reverse_subseq()
                print(cloned_subseq)
        print()

    def make_sorted_deck(self):
        """
        This method makes a sorted Deck by picking up the smallest
        Card from the top of the Piles, one at a time and adding 
        them to end of the Deck.. At any given round the next 
        smallest Card is one of the Cards at the top of one of the 
        Piles on the table.
        
        The Algorithm:
        
        A. Outer Loop: Loop 52 times, once for each Card in the Deck.
           1. Initialize a low_pile variable to 0 to hold the index 
              of the current Pile contains the lowest Card found 
              so far.
           2. Initialize a low_card variable to the highest Card in 
              the Deck, which is the King of Spades: Card(3, 13), to
              hold the lowest Card found so far.
           3. Inner Loop: Traverse each Pile using the range function
              a. If the Pile is not empty
                 i. Grab the first_card in the Pile
                 ii. Compare that first_card to the current low_card 
                     and if the first_card is lower than the current 
                     low_card, then make the first_card the newest
                     low_card and the Pile index the current low_pile.
           4. Get the lowest card from the top of Piles and add it to 
              the Deck.              
        """
        print("The sorted deck:\n")

        for i in range(52):
            low_pile = 0
            low_card = Card(3, 13)
            for p in range(len(self.__piles) - 1, -1, -1):
                if len(self.__piles[p]) > 0:
                    first_card = self.__piles[p].get_top_card()
                    if first_card.compare(low_card) <= 0:
                        low_card = first_card
                        low_pile = p

            self.__deck.add_card(self.__piles[low_pile].remove_card())
