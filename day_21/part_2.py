from collections import Counter

from day_21 import *

# Each turn, roll 3-sided die three times
# Outcomes: Counter({3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1})
# 3 --> 1
# 4 --> 3
# 5 --> 6
# 6 --> 7
# 7 --> 6
# 8 --> 3
# 9 --> 1


class DiracGame:
    def __init__(self):
        self.turn = 0
        self.position_1, self.position_2 = get_starting_positions()
        self.player_1_wins = self.player_2_wins = 0
        self.distribution = Counter({(self.position_1, 0, self.position_2, 0): 1})
        self.rolls_distribution = Counter({3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1})

    def record_wins(self, count):
        if self.turn % 2:
            self.player_1_wins += count
        else:
            self.player_2_wins += count

    def take_turn(self):
        self.turn += 1
        new_distribution = Counter()
        for (position_1, score_1, position_2, score_2), count in self.distribution.items():
            for roll, roll_count in self.rolls_distribution.items():
                position, score = (position_1, score_1) if self.turn % 2 else (position_2, score_2)
                outcome_count = count * roll_count
                new_position, new_score = get_new_position_and_score(position, score, roll)
                if new_score >= 21:
                    self.record_wins(outcome_count)
                else:
                    if self.turn % 2:
                        new_state = (new_position, new_score, position_2, score_2)
                    else:
                        new_state = (position_1, score_1, new_position, new_score)
                    new_distribution[new_state] += outcome_count

        self.distribution = new_distribution

    def play_game(self):
        while self.distribution:
            self.take_turn()


if __name__ == "__main__":
    new_game = DiracGame()
    new_game.play_game()
    print(max(new_game.player_1_wins, new_game.player_2_wins))
