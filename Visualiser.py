import pygame
import random
from Sorting import sortAlgo

COLORS = {
    "background":(35,35,48),
    "regular":(255,248,240),
    "hl1":(239,71,111),
    "hl2":(255,209,102),
    "hl3":(17,138,178),
    "sorted":(6,214,160)
}

class Visualise():

    def __init__(self, width = 600, height = 400,n=50):
        self.width = width
        self.height = height
        #we wait before displaying the screen
        self.screen = None
        #create array to display
        self.array = None
        self.length = n

    def launch(self):
        # initialize pygame and screen
        pygame.init()
        self.screen = pygame.display.set_mode((self.width,self.height))

    def choose_Algo(self,input):
        ...

    def update(self, process,speed = 'n'):
        t = 10 if speed == 'fast' else 100
        #we need to add menu (for update)
        self.launch()

        # animation loop
        anime = True
        while anime:
            #next step is the sorting process
            self.array, hl1, hl2, hl3 = next(process, (None, None, None, None))

            if self.array:
                # display the array
                self.draws_bar(hl1,hl2,hl3)
            else:
                # display sorted array
                self.array = list(range(1,self.length+1))
                self.draws_bar(sorted = True)
            
            #update
            pygame.display.flip()
            #pause
            pygame.time.wait(t)
            # track user interaction
            for event in pygame.event.get():
                #user closes the pygame window to en animation
                if event.type == pygame.QUIT:
                    anime = False

    #function to draw a single bar
    def draw_bar(self, index, color):
        if self.screen:
            #array = random.sample(range(1,n+1),n)
            bar_w = self.width//self.length
            bar_h = self.height//self.length * self.array[index]
            x = index * bar_w
            y = self.height - bar_h
            bar = pygame.Rect(x, y, bar_w, bar_h)
            pygame.draw.rect(self.screen, color, bar)

    # function to visualize an entire array using a bar chart
    def draws_bar(self, hl1 = [], hl2 = [], hl3 = [], sorted=False):
        if self.screen:
            self.screen.fill(COLORS["background"])
            if sorted:
                for h in range(self.length):
                    self.draw_bar(h, COLORS["sorted"])
            else:
                for h in range(self.length):
                    self.draw_bar(h, COLORS["regular"])
                #test hl1[0] instead of for
                for h in hl1:
                    self.draw_bar(h, COLORS["hl1"])
                for h in hl2:
                    self.draw_bar(h, COLORS["hl2"])
                for h in hl3:
                    self.draw_bar(h, COLORS["hl3"])









