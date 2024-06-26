from players import User, Computer
import ui as ui
from strategies import AdvancedStrategy
import pygame
from random import shuffle
class DiamondsGame:
    
    def __init__(self):
        self.diamonds = [i for i in range(2, 15)]
        shuffle(self.diamonds)
        self.round = 1
        self.player1 = User("Nikita", 'c')
        self.player2 = Computer("Mr. MAC", 'h', AdvancedStrategy)

    def play_round(self, screen, FONT):
        ui.display_text(screen, f"Round: {self.round}", (600, 10), (255, 255, 255), FONT)
        ui.display_text(screen, f"Player 1 ({self.player1.get_displayname()}) Points: {self.player1.get_points()}", (100, 400), (255, 255, 255), FONT)
        ui.display_text(screen, f"Player 2 ({self.player2.get_displayname()}) Points: {self.player2.get_points()}", (100, 430), (255, 255, 255), FONT)
        ui.display_text(screen, "Diamond card", (100, 215), (255, 255, 255), FONT)
        ui.draw_hand(screen, self.player1)
        diamond_card = self.diamonds.pop()
        ui.draw_card(screen, diamond_card, 100, 100, 'd')
        player2_bid = self.player2.bid(diamond_card, self.player1.get_cards(), self.diamonds)
        player1_bid = self.player1.bid(diamond_card, self.player2.get_cards(), self.diamonds)
        ui.display_text(screen, f"{self.player1.get_displayname()}'s bid worth : {player1_bid}", (400, 215), (255, 255, 255), FONT)
        ui.display_text(screen, f"{self.player2.get_displayname()}'s bid worth: {player2_bid}", (800, 215), (255, 255, 255), FONT)
        ui.draw_card(screen, player1_bid, 400, 100, self.player1.get_suit())
        ui.draw_card(screen, player2_bid, 800, 100, self.player2.get_suit())
        
        if player1_bid > player2_bid:
            self.player1.add_points(diamond_card)
            ui.display_text(screen, f"{self.player1.get_displayname()} won {diamond_card} points!", (400, 550), (255, 255, 255), FONT)
        elif player1_bid < player2_bid:
            self.player2.add_points(diamond_card)
            ui.display_text(screen, f"{self.player2.get_displayname()} won {diamond_card} points!", (400, 550), (255, 255, 255), FONT)
        else:
            self.player1.add_points(diamond_card/2)
            self.player2.add_points(diamond_card/2)
            ui.display_text(screen, f"{self.player1.get_displayname()} and {self.player2.get_displayname()} won {diamond_card/2} points each!", (400, 550), (255, 255, 255), FONT)
        pygame.time.wait(500)
        pygame.display.flip()
        self.round += 1
    
    def play(self):
        pygame.init()
        screen = pygame.display.set_mode((1200, 1000))
        pygame.display.set_caption("Diamonds")
        FONT = pygame.font.Font(None, 36)

        game_over = False
        while not game_over:
            screen.fill((0, 80, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    break
            # Play a round
            if self.diamonds:
                self.play_round(screen, FONT)
                pygame.time.wait(2000)
            else:
            # Game Over
                game_over = True
                p1 = self.player1.get_points()
                p2 = self.player2.get_points()  
                ui.display_text(screen, f"GAME OVER", (100, 350), (255, 255, 255), FONT)
                ui.display_text(screen, f"Player 1 ({self.player1.get_displayname()}) Points: {p1}", (100, 400), (255, 255, 255), FONT)
                ui.display_text(screen, f"Player 2 ({self.player2.get_displayname()}) Points: {p2}", (100, 430), (255, 255, 255), FONT) 
                if p1 > p2:
                    ui.display_text(screen, f"{self.player1.get_displayname()} won the game!", (400, 500), (255, 255, 255), FONT)
                elif p2 > p1:
                    ui.display_text(screen, f"{self.player2.get_displayname()} won the game!", (400, 500), (255, 255, 255), FONT)
                else:
                    ui.display_text(screen, f"{self.player1.get_displayname()} and {self.player2.get_displayname()} tied!", (400, 500), (255, 255, 255), FONT)
                pygame.display.flip()
                pygame.time.wait(5000)
        # Quit Pygame
        pygame.quit()

game = DiamondsGame()
game.play()



