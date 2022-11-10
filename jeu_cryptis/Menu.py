import pygame

class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = - 100

    def draw_cursor(self):
        self.game.draw_text('|-->', 15, self.cursor_rect.x, self.cursor_rect.y)
        #self.game.window.blit(self.game.BLACK, (self.cursor_rect.x, self.cursor_rect.y))
        self.game.draw_text('<--|', 15, self.cursor_rect.x+215, self.cursor_rect.y)

    def blit_screen(self):
        pygame.display.flip()
        self.game.reset_keys()

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        self.newgamex, self.newgamey = self.mid_w, self.mid_h + 25
        self.arcadex, self.arcadey = self.mid_w, self.mid_h + 35
        self.cursor_rect.midtop = (self.newgamex + self.offset, self.newgamey)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.window.blit(self.game.background, (0, 0))
            self.game.draw_text('Menu', 30, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 160)
            self.game.window.blit(self.game.deco, (self.game.DISPLAY_W / 2 - 65, self.game.DISPLAY_H - 60))
            self.game.draw_text("NEW GAME", 20, self.newgamex, self.newgamey)
            self.game.draw_text("ARCADE", 20, self.arcadex + 4, self.arcadey + 50)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.arcadex + self.offset, self.arcadey+ 50)
                self.state = 'ARCADE'
            elif self.state == 'ARCADE':
                self.cursor_rect.midtop = (self.arcadex + self.offset, self.arcadey)
                self.state = 'Start'
        elif self.game.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.arcadex + self.offset, self.arcadey)
                self.state = 'ARCADE'
            elif self.state == 'ARCADE':
                self.cursor_rect.midtop = (self.newgamex + self.offset, self.newgamey)
                self.state = 'Start'

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.playing = True
            elif self.state == 'ARCADE':
                self.game.curr_menu = self.game.arcade
            self.run_display = False



class ArcadeMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'CREATE KEYS'
        self.crekeysx,self.crekeysy = self.mid_w, self.mid_h - 30
        self.begx, self.begy = self.mid_w, self.mid_h
        self.easyx, self.easyy = self.mid_w, self.mid_h + 30
        self.medx, self.medy = self.mid_w, self.mid_h + 60
        self.hardx, self.hardy = self.mid_w, self.mid_h + 90
        self.expertx, self.experty = self.mid_w, self.mid_h + 120
        self.cursor_rect.midtop = (self.crekeysx + self.offset, self.crekeysy)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.window.blit(self.game.background, (0, 0))
            self.game.window.blit(self.game.deco, (self.game.DISPLAY_W /2 - 65, self.game.DISPLAY_H - 60))
            self.game.draw_text('ARCADE', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 160)
            self.game.draw_text("CREATE KEYS", 15, self.crekeysx, self.crekeysy)
            self.game.draw_text("BEGINNER - 8 BLOCKS", 15, self.begx, self.begy)
            self.game.draw_text("EASY - 10 BLOCKS", 15, self.easyx, self.easyy)
            self.game.draw_text("MEDIUM - 12 BLOCKS", 15, self.medx, self.medy)
            self.game.draw_text("HARD - 14 BLOCKS", 15, self.hardx, self.hardy)
            self.game.draw_text("EXPERT - 16 BLOCKS", 15, self.expertx, self.experty)
            self.draw_cursor()
            self.blit_screen()

    #def move_cursor(self):

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.game.DOWN_KEY:
                if self.state == 'CREATE KEYS':
                    self.state = 'BEGINNER - 8 BLOCKS'
                    self.cursor_rect.midtop = (self.begx + self.offset, self.begy)
                elif self.game == 'BEGINNER - 8 BLOCKS':
                    self.state = 'EASY - 10 BLOCKS'
                    self.cursor_rect.midtop = (self.easyx + self.offset, self.easyy)
                elif self.state == 'EASY - 10 BLOCKS':
                    self.state = 'MEDIUM - 12 BLOCKS'
                    self.cursor_rect.midtop = (self.medx + self.offset, self.medy)
                elif self.state == 'MEDIUM - 12 BLOCKS':
                    self.state = 'HARD - 14 BLOCKS'
                    self.cursor_rect.midtop = (self.hardx + self.offset, self.hardy)
                elif self.state == 'HARD - 14 BLOCKS':
                    self.state = 'EXPERT - 16 BLOCKS'
                    self.cursor_rect.midtop = (self.expertx + self.offset, self.experty)
                elif self.state == 'EXPERT - 16 BLOCKS':
                    self.state = 'CREATE KEYS'
                    self.cursor_rect.midtop = (self.crekeysx + self.offset, self.crekeysy)
            elif self.game.UP_KEY:
                if self.state == 'CREATE KEYS':
                    self.state = 'EXPERT - 16 BLOCKS'
                    self.cursor_rect.midtop = (self.expertx + self.offset, self.experty)
                elif self.state == 'EXPERT - 16 BLOCKS':
                    self.state = 'HARD - 14 BLOCKS'
                    self.cursor_rect.midtop = (self.hardx + self.offset, self.hardy)
                elif self.state == 'HARD - 14 BLOCKS':
                    self.state = 'MEDIUM - 12 BLOCKS'
                    self.cursor_rect.midtop = (self.medx + self.offset, self.medy)
                elif self.state == 'MEDIUM - 12 BLOCKS':
                    self.state = 'EASY - 10 BLOCKS'
                    self.cursor_rect.midtop = (self.easyx + self.offset, self.easyy)
                elif self.state == 'EASY - 10 BLOCKS':
                    self.state = 'BEGINNER - 8 BLOCKS'
                    self.cursor_rect.midtop = (self.begx + self.offset, self.begy)
                elif self.state == 'BEGINNER - 8 BLOCKS':
                    self.state = 'CREATE KEYS'
                    self.cursor_rect.midtop = (self.crekeysx + self.offset, self.crekeysy)

