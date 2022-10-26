import time
import pygame
from cards import allCards
pygame.init()

dsW = 600
dsH = 600
FPS = 24
cardW = 75
cardH = 90
screen = pygame.display.set_mode((dsW, dsH))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 100)
elixer = 6

#text box variables
base_font = pygame.font.Font(None, 32)
user_text = ''
input_rect = pygame.Rect(200, 400, 140, 32)
color_active = pygame.Color('lightskyblue3')
color_passive = pygame.Color('grey')
elixer_rect = pygame.Rect(505, 50, 65, 380)
color = color_passive
active = False

#in cycle
P1 = [50, 475]
P2 = [200, 475]
P3 = [350, 475]
P4 = [500, 475]

#out of cycle
P5 = [50, 350]
P6 = [50, 250]
P7 = [50, 150]
P8 = [50, 50]


class Card:
    
    def __init__(self, card, code):
        self.imagePath = card["image"]
        self.name = card["name"]
        self.elixer = card["elixer"]
        self.code = code
 
    def getCard(self):
        return pygame. transform. scale(pygame.image.load(self.imagePath), (cardW, cardH))

    def displayCard(self, cycle, px, py):
        return screen.blit(cycle, pygame.Rect( px, py, cardW, cardH))


cards = {
    1 : Card(allCards["temp"], "temp"),
    2 : Card(allCards["temp"], "temp"),         
    3 : Card(allCards["temp"], "temp"), 
    4 : Card(allCards["temp"], "temp"), 
    5 : Card(allCards["temp"], "temp"),      
    6 : Card(allCards["temp"], "temp"),       
    7 : Card(allCards["temp"], "temp"),         
    8 : Card(allCards["temp"], "temp") 
}


inCycle = [cards[1], cards[2], cards[3], cards[4]]
outCycle = [cards[5], cards[6], cards[7], cards[8]]

def updateCycle(position):
    global lastPos
    lastPos = position
    card = inCycle[position]

    outCycle.append(card)
    inCycle.pop(position)

    inCycle.insert(position, outCycle[0])
    outCycle.pop(0)

#moves cycle backwards for undo action
def undo():
    global elixer
    card = outCycle[3]
    elixer += card.elixer
    outCycle.pop(3)
    outCycle.insert(0, inCycle[lastPos])
    inCycle.pop(lastPos)
    inCycle.insert(lastPos, card)

 
cardsPlayed = 8
def addCard():
    global cardsPlayed

    card = allCards[user_text]
    cards[cardsPlayed] = Card(card, user_text)


    if cardsPlayed <= 4:
            updateCycle(cardsPlayed - 1)
            outCycle.pop(3)
    else:
        outCycle.pop(0)

    outCycle.append(cards[cardsPlayed])
    cardsPlayed = cardsPlayed - 1

time1 = time.time()
start = time.time()
eps = 2.8
def checkEps():
    global eps
    current = time.time()
    if (round((current - start), 1) == 5):
        eps = 1.4

def calcElixer(cardPlayed, code):
    global time1
    global elixer
    current = time.time()

    if (round((current - time1), 1) >= eps):
        if elixer != 10:
            elixer += 1
        time1 = time.time()

    if cardPlayed:
        for card in cards.values():
            if (user_text == card.code or code == card.code):
                elixer -= card.elixer

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
            else:
                active = False
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                calcElixer(True, inCycle[0].code)
                updateCycle(0)
                
            if event.key == pygame.K_2:
                calcElixer(True, inCycle[1].code)
                updateCycle(1)
                
            if event.key == pygame.K_3:
                calcElixer(True, inCycle[2].code)
                updateCycle(2)
                
            if event.key == pygame.K_4:
                calcElixer(True, inCycle[3].code)
                updateCycle(3)
                
            if event.key == pygame.K_RETURN:
                for i in allCards:
                    if user_text == i:
                        addCard()
                        calcElixer(True, False)

                user_text = ''
            if event.key == pygame.K_TAB:
                undo()

            elif event.key == pygame.K_BACKSPACE:
  
                # get text input from 0 to -1 i.e. end.
                user_text = user_text[:-1]
  
            # Unicode standard is used for string
            # formation
            elif (event.key != pygame.K_1 and event.key != pygame.K_2 and event.key != pygame.K_3 and event.key != pygame.K_4
            and event.key != pygame.K_RETURN and event.key != pygame.K_TAB):
                user_text += event.unicode

    calcElixer(False, False)
    checkEps()

    screen.fill((0,0,0))

    if active:
        color = color_active
    else:
        color = color_passive

    elixer_rect = pygame.Rect(505, 50, 65, 380)

    for i in range(10):
        ecolor = 'darkgrey'

        if elixer >= i:
            ecolor = 'purple'
        pygame.draw.rect(screen, pygame.Color(ecolor), pygame.Rect(505, 400 - 40*i,65,38))


    pygame.draw.rect(screen, color, input_rect)
    text_surface = base_font.render(user_text, True, (255, 255, 255))
    screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
    input_rect.w = max(220, text_surface.get_width()+10)

    for i in range(4):
        screen.blit(inCycle[i].getCard(), pygame.Rect( globals()[f'P{i+1}'][0], globals()[f'P{i+1}'][1], cardW, cardH))
    for i in range(4):
        screen.blit(outCycle[i].getCard(), pygame.Rect( globals()[f'P{i+5}'][0], globals()[f'P{i+5}'][1], cardW, cardH))


    pygame.display.flip()


