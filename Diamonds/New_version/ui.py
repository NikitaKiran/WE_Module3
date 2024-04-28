import pygame

def display_text(screen, text, position, color, FONT):
    text_surface = FONT.render(text, True, color)
    screen.blit(text_surface, position)


def load_card_image(card, suit):
  card_values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
                    "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
  card_names = {value: key for key, value in card_values.items()}
  image_path = 'cards/' + suit + card_names[card] + '.png'
  if image_path:
    return pygame.image.load(image_path)
  else:
    return None

# Function to draw a card on the screen
def draw_card(screen, card, x, y, suit):
  card_image = load_card_image(card, suit)
  if card_image:
      # Resize the card image to a desired size
      new_width = 80  # Adjust width as needed
      new_height = 105  # Adjust height as needed
      card_image = pygame.transform.scale(card_image, (new_width, new_height))
      screen.blit(card_image, (x, y))
      pygame.display.flip()

def draw_hand(screen, player):
    card_spacing = 82
    for i, card in enumerate(player.cards):
        card_x, card_y = 110 + i * card_spacing, 600
        draw_card(screen, card, card_x, card_y, player.suit)
    pygame.display.flip()

def select_card(player):
    card_spacing = 82
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                # Check if clicked on a card in hand
                for i, card in enumerate(player.cards):
                    card_x, card_y = 110 + i * card_spacing, 600
                    card_rect = pygame.Rect(card_x, card_y, 79, 104)
                    if card_rect.collidepoint(pos):
                        return card
                    



 

