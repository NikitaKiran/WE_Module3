import random
class RandomStrategy:
    def apply(diamond_card, remaining_cards, remaining_opponent_cards, remaining_diamond_cards):
        # Implement the logic for the RandomStrategy here
        return random.choice(remaining_cards)

class Strategy1:
    def apply(diamond_card, remaining_cards, remaining_opponent_cards, remaining_diamond_cards):
        if diamond_card > 10:
            return max(remaining_cards)
        elif diamond_card < 5:
            return min(remaining_cards)
        else:
            return random.choice(remaining_cards)

class AdvancedStrategy:
        matching = {}

        def apply(diamond_card, remaining_cards, remaining_opponent_cards, remaining_diamond_cards):
            if diamond_card in AdvancedStrategy.matching.keys():
                    return AdvancedStrategy.matching[diamond_card]
            win_bids = [bid for bid in remaining_cards if bid >= max(remaining_opponent_cards)]
            non_win = [bid for bid in remaining_cards if bid not in win_bids]
            lose_bids = [bid for bid in remaining_cards if bid < min(remaining_opponent_cards)]
            non_lose = [bid for bid in remaining_cards if bid not in lose_bids]
            if len(win_bids) == 0 and len(lose_bids) == 0:
                if diamond_card > 10:
                    return max(remaining_cards)
                elif diamond_card < 5:
                    return min(remaining_cards)
                else:
                    return random.choice(remaining_cards)
            elif len(lose_bids) == 0:
                num = len(win_bids)
                remaining = sorted(remaining_diamond_cards + [diamond_card], reverse=True)
                for i, j in zip(remaining, win_bids):
                    AdvancedStrategy.matching[i] = j
                if diamond_card in AdvancedStrategy.matching.keys():
                    return AdvancedStrategy.matching[diamond_card]
                else:
                    if diamond_card > 10:
                        return max(non_win)
                    elif diamond_card < 5:
                        return min(non_win)
                    else:
                        return random.choice(non_win)
            

                    
