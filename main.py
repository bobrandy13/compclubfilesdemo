import pygame

pygame.init()

X = 600
Y = 600

(width, height) = (X, Y)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('File IO')
screen.fill("WHITE")

pygame.display.flip()

font = pygame.font.SysFont('Arial', 32)

running = True

screen = pygame.display.set_mode((640, 480))
font = pygame.font.Font(None, 32)
clock = pygame.time.Clock()
input_box = pygame.Rect(100, 100, 140, 32)
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive
active = False
text = ''
done = False

# Load the text
savedTextFile = open("demo.txt", "r+")
savedTextFile.seek(0)
contents = savedTextFile.read()

savedText = font.render(contents, True, "BLUE")
textRect = savedText.get_rect()
textRect.center = (X // 2, Y // 2)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if input_box.collidepoint(event.pos):
                # Toggle the active variable.
                active = not active
            else:
                active = False
            # Change the current color of the input box.
            color = color_active if active else color_inactive
        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    savedTextFile.seek(0)
                    savedTextFile.truncate(0)
                    savedTextFile.write(text)
                    text = ''
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

    screen.fill("WHITE")
    # Render the current text.
    txt_surface = font.render(text, True, color)
    # Resize the box if the text is too long.
    width = max(200, txt_surface.get_width()+10)
    input_box.w = width
    # Blit the text.
    screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
    # Blit the input_box rect.
    pygame.draw.rect(screen, color, input_box, 2)

    # render the text 
    screen.blit(savedText, textRect)

    pygame.display.flip()
    clock.tick(30)

savedTextFile.close()