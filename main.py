import time
import pygame
import copy
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

#used for calculating elixer
time1 = time.time()
start = time.time()
eps = 2.8

#text box variables
base_font = pygame.font.Font(None, 32)
user_text = ''
input_rect = pygame.Rect(200, 400, 140, 32)
color_active = pygame.Color('lightskyblue3')
color_passive = pygame.Color('grey')
elixer_rect = pygame.Rect(505, 50, 65, 380)
color = color_passive
active = False

# postions of the cards on the screen
positions = [
# in cycle
[50, 475],
[200, 475],
[350, 475],
[500, 475],

# out of cycle
[50, 350],
[50, 250],
[50, 150],
[50, 50]
]


# creates a card object
class Card:
 
    def __init__(self, code):
        self.imagePath = allCards[code]["image"]
        self.name = allCards[code]["name"]
        self.elixer = allCards[code]["elixer"]
        self.code = code


    
    def getCard(self):
        return pygame. transform. scale(pygame.image.load(self.imagePath), (cardW, cardH))

    # adds a new card to the cycle
    def addToCycle(self):

        # logs cycle before it has changed when new card is added
        Move(self, elixer, cycle).logHistory() 

        # checks to see which index the next card that will be in cycle should be pushed to
        index = -1
        for i in cycle[0]:
            if i.code == "temp":
                index += 1

        # rotates the cycle then sets then last card to what was added
        rotateCycle(index)           
        cycle[1][3] = self
        
    # gets the elixer price of a card played and passes it to update the total elixer
    def updateElixer(self):
        if self.code != "temp":
            calcElixer(self.elixer)


class Move:
 
    def __init__(self, card, elixer, cycle):
        self.card = card
        self.elixer = elixer
        self.cycle = cycle

    # adds all current game data to history array
    def logHistory(self):
        history.insert(0, copy.deepcopy(self))

    # goes back to last game data save
    def undo(self):
        global cycle    
        global elixer
        cycle = self.cycle
        elixer = self.elixer
        history.pop(0)


# cycle array
cycle = [

# incycle
[Card( "temp"), Card( "temp"), Card( "temp"), Card( "temp")], 

# outcycle
[Card( "temp"), Card( "temp"), Card( "temp"), Card( "temp")]]

history = []

# function to show the two cycle arrays for debuging
def printCycle():
    print("In cycle:")
    for card in cycle[0]:
        print(card.name)
    print("")
    print("Out of cycle:")
    for card in cycle[1]:
        print(card.name)
    print("")

def rotateCycle(position = 3):

    card = cycle[0][position]
    
    cycle[1].append(card)
    cycle[0].pop(position)

    cycle[0].insert(position, cycle[1][0])
    cycle[1].pop(0)

    printCycle()

# checks for double elixer
def checkEps():
    global eps
    current = time.time()
    if (round((current - start), 1) == 120):
        eps = 1.4

# adds 1 elixer ever 2.8 in single elixer and every 1.4s in double elixer
def calcElixer(cost):
    global time1
    global elixer
    current = time.time()

    # if a cost is passed to the function it will subtract it from the total elixer
    if cost:
        elixer -= cost
        time1 += 0.5

    if (round((current - time1), 1) >= eps):
        if elixer != 10:
            elixer += 1
        time1 = time.time()

# handels display
def dispaly():

    screen.fill((0,0,0))

    if active:
        color = color_active
    else:
        color = color_passive

    for i in range(10):
        ecolor = 'darkgrey'

        if elixer >= i:
            ecolor = 'purple'
        pygame.draw.rect(screen, pygame.Color(ecolor), pygame.Rect(505, 400 - 40*i,65,38))


    pygame.draw.rect(screen, color, input_rect)
    text_surface = base_font.render(user_text, True, (255, 255, 255))
    screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
    input_rect.w = max(220, text_surface.get_width()+10)

    # loops through postions to show cards at correct spots
    for x in range(2):
        for i in range(4):
            screen.blit(cycle[x][i].getCard(), pygame.Rect( positions[i+(4*x)][0], positions[i+(4*x)][1], cardW, cardH))

    pygame.display.flip()


# used to update the game on 1,2,3,4 key presses
def updateGame(index):
    Move(cycle[0][index], elixer, cycle).logHistory()
    cycle[0][index].updateElixer()
    rotateCycle(index)


run = True
while run:

    # runs the function every frame to keep elixer updated
    calcElixer(0)
    
    # checks for double elixer every frame
    checkEps()

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
                updateGame(0)
                
            if event.key == pygame.K_2:
                updateGame(1)
                
            if event.key == pygame.K_3:
                updateGame(2)
                
            if event.key == pygame.K_4:
                updateGame(3)
                
            if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                for i in allCards:
                    if user_text == i:
                        #addCard()
                        Card(user_text).addToCycle()
                        Card(user_text).updateElixer()

                user_text = ''
            if event.key == pygame.K_TAB:
              
                history[0].undo()

            elif event.key == pygame.K_BACKSPACE:
  
                # get text input from 0 to -1 i.e. end.
                user_text = user_text[:-1]
  
            # Unicode standard is used for string
            # formation
            elif (event.key != pygame.K_1 and event.key != pygame.K_2 and event.key != pygame.K_3 and event.key != pygame.K_4
            and event.key != pygame.K_RETURN and event.key != pygame.K_TAB and event.key != pygame.K_SPACE):
                user_text += event.unicode

    dispaly()

    
