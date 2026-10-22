class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        #Check whether the total number of cards is divisible by groupSiz 
        if len(hand) % groupSize != 0:
            return False 
        
        #Sort the cards in ascending order 
        hand.sort()

        #Create a frequency map to count the number of occurance of each card 
        frequency_map = {}
        for card in hand:
            if card not in frequency_map:
                frequency_map[card] = 1
            else:
                frequency_map[card] += 1
        
        for card in hand:
            #Skip all cards that have been used 
            if frequency_map[card] == 0:
                continue
            #Start a new  group with GroupSize length 
            for i in range(groupSize):
                current_card = card + i 
                #Check if the number's frequency is zero or if it dosent exist 
                if current_card not in frequency_map or frequency_map[current_card] == 0:
                    return False 
                #Consume the card by decrementing its frequency 
                frequency_map[current_card] -= 1
        return True