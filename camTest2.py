import pygame as pg
import time, os, sys

os.system("clear")
print("")
initial_time = time.time()
pg.init()
clock = pg.time.Clock()

class window:
    dimensions = (1000, 800)
    screen = pg.display.set_mode(dimensions)
    fps = 60

class player:
    dimensions = (100, 100)
    surf = pg.Surface(dimensions)
    surf.fill("green")
    rect = surf.get_rect(topleft = (0, 0))
    position = (rect.x, rect.y)
    row = rect.y
    column = rect.y

class bg:
    surf = pg.Surface(window.dimensions)
    surf.fill("lightblue")

class tile:

    class tile:
        surf = pg.Surface((100, 100))
        surf.fill("red")

    tile_map = {
        1: [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
        2: [1, 0, 1, 0, 0, 0, 1, 0, 0, 0],
        3: [1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
        4: [1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
        5: [1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
        6: [1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
        7: [1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
        8: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    }

    def tile_positions(self):
        tile_positions = []
        for x in self.tile_map:
            index = 1
            lst = self.tile_map.get(x)
            for z in range(len(lst)):
                if lst[z] == 1: tile_positions.append((x, index)); index += 1
                else: index += 1
        
        return tile_positions

    # NOTE: NEXT IS TO FIND A WAY TO MAKE THE RENDERING SCALABLE BY A NUMBER
    # COULD USE A FOR LOOP AND ADD/SUBTRACT THE X VALUE BY THE BLITS AND INDEXES.
    def check_proximity_tiles(self, player_row, player_column):
        tile_below_lst = self.tile_map.get(player_row + 1)
        tile_above_lst = self.tile_map.get(player_row - 1)
        tile_lst_lr = self.tile_map.get(player_row)
        upper_tile_lst = self.tile_map.get(player_row - 1)
        lower_tile_lst = self.tile_map.get(player_row + 1)
        try:
            try:
                tile_below = tile_below_lst[player_column - 1]
                tile_above = tile_above_lst[player_column - 1]
                if tile_above > 0:
                    window.screen.blit(self.tile.surf, ((player_column - 1) * 100, (player_row - 2) * 100))
                else:
                    pass
                if tile_below > 0:
                    window.screen.blit(self.tile.surf, ((player_column - 1) * 100, (player_row) * 100))

                # Checking for tiles to the left and right of the player.
                tile_left = tile_lst_lr[player_column - 2]
                tile_right = tile_lst_lr[player_column]
                if tile_left > 0:
                    window.screen.blit(tile.tile.surf, ((player_column - 2) * 100, (player_row - 1) * 100))
                else: 
                    pass
                if tile_right > 0:
                    window.screen.blit(tile.tile.surf, (player_column * 100, (player_row - 1) * 100))
                else:
                    pass

                # Checking for tiles on the row above the player to the left and right.
                tile_upper_left = upper_tile_lst[player_column - 2]
                tile_upper_right = upper_tile_lst[player_column]
                if tile_upper_left > 0:
                    window.screen.blit(tile.tile.surf, ((player_column - 2) * 100, (player_row - 2) * 100))
                if tile_upper_right > 0:
                    window.screen.blit(tile.tile.surf, (player_column * 100, (player_row - 2) * 100))


                #Checking for tiles on the row under the player to the left and right.
                tile_lower_left = lower_tile_lst[player_column - 2]
                tile_lower_right = lower_tile_lst[player_column]
                if tile_lower_left > 0:
                    window.screen.blit(tile.tile.surf, ((player_column - 2) * 100, player_row * 100))
                if tile_lower_right > 0:
                    window.screen.blit(tile.tile.surf, (player_column * 100, player_row * 100))
            except IndexError:
                # Checking bottom bound.
                tile_above = tile_above_lst[player_column - 1]
                if tile_above > 0:
                    window.screen.blit(self.tile.surf, ((player_column - 1) * 100, (player_row - 2) * 100))
                else:
                    return False

                # Checking far right bound.
                tile_left = tile_lst_lr[player_column - 2]
                if tile_left > 0:
                    window.screen.blit(tile.tile.surf, ((player_column - 2) * 100, (player_row - 1) * 100))
                else:
                    return False
        except TypeError:
            return False
    
    # Checks for tiles above and below the player.
    def tile_above_below(self, player_row, player_column):
        tile_below_lst = self.tile_map.get(player_row + 1)
        tile_above_lst = self.tile_map.get(player_row - 1)
        try:
            try:
                tile_below = tile_below_lst[player_column - 1]
                tile_above = tile_above_lst[player_column - 1]
                if tile_above > 0:
                    window.screen.blit(self.tile.surf, ((player_column - 1) * 100, (player_row - 2) * 100))
                if tile_below > 0:
                    window.screen.blit(self.tile.surf, ((player_column - 1) * 100, (player_row) * 100))
            except IndexError:
                return False
        except TypeError:
            return False

    # Checks for tiles to the left and right of the player.
    def tile_left_right(self, player_row, player_column):
        tile_lst_lr = self.tile_map.get(player_row)
        try:
            try:
                tile_left = tile_lst_lr[player_column - 2]
                tile_right = tile_lst_lr[player_column]
                if tile_left > 0:
                    window.screen.blit(tile.tile.surf, ((player_column - 2) * 100, (player_row - 1) * 100))
                else: 
                    pass
                if tile_right > 0:
                    window.screen.blit(tile.tile.surf, (player_column * 100, (player_row - 1) * 100))
                else:
                    pass
            except IndexError:
                return False
        except TypeError:
            return False

    # Checks for tiles on the row above the player to the left and right.
    def tile_upper_left_right(self, player_row, player_column):
        try:
            upper_tile_lst = self.tile_map.get(player_row - 1)
            try:
                tile_upper_left = upper_tile_lst[player_column - 2]
                tile_upper_right = upper_tile_lst[player_column]
                if tile_upper_left > 0:
                    window.screen.blit(tile.tile.surf, ((player_column - 2) * 100, (player_row - 2) * 100))
                if tile_upper_right > 0:
                    window.screen.blit(tile.tile.surf, (player_column * 100, (player_row - 2) * 100))
            except IndexError:
                return False
        except TypeError:
            return False
    
    # Checks for tiles on the row under the player to the left and right.
    def tile_lower_left_right(self, player_row, player_column):
        try:
            lower_tile_lst = self.tile_map.get(player_row + 1)
            try:
                tile_lower_left = lower_tile_lst[player_column - 2]
                tile_lower_right = lower_tile_lst[player_column]
                if tile_lower_left > 0:
                    window.screen.blit(self.tile.surf, ((player_column - 2) * 100, player_row * 100))
                if tile_lower_right > 0:
                    window.screen.blit(self.tile.surf, (player_column * 100, player_row * 100))
            except IndexError:
                return False
        except TypeError:
            return False

    # Checks for tiles below, to the right, and to the bottom right of the player.
    # Ran when player is in the top left corner.
    # Used to circumvents errors that cause tiles to not be rendered in corners or rows/columns.
    def PTR_upper_left(self, player_row, player_column):
        try:
            lower_tile_lst = self.tile_map.get(player_row + 1)
            current_row_tile_lst = self.tile_map.get(player_row)
            try:
                tile_lower_right = lower_tile_lst[player_column]
                tile_below = lower_tile_lst[player_column - 1]
                tile_right = current_row_tile_lst[player_column]

                if tile_below > 0:
                    window.screen.blit(tile.tile.surf, ((player_column - 1) * 100, (player_row) * 100))
                
                if tile_right > 0:
                    window.screen.blit(tile.tile.surf, ((player_column) * 100, (player_row - 1) * 100))
                
                if tile_lower_right > 0:
                    window.screen.blit(tile.tile.surf, ((player_column) * 100, (player_row) * 100))

            except IndexError:
                return False
        except:
            return False

    def PTR_upper_row(self, player_row, player_column):
        try:
            lower_tile_lst = self.tile_map.get(player_row + 1)
            tile_lst_lr = self.tile_map.get(player_row)
            try:
                tile_lower_left = lower_tile_lst[player_column - 2]
                tile_lower_right = lower_tile_lst[player_column]
                tile_below = lower_tile_lst[player_column - 1]
                tile_left = tile_lst_lr[player_column - 2]
                tile_right = tile_lst_lr[player_column]
                if tile_lower_left > 0:
                    window.screen.blit(tile.tile.surf, ((player_column - 2) * 100, player_row * 100))
                if tile_lower_right > 0:
                    window.screen.blit(tile.tile.surf, (player_column * 100, player_row * 100))
                if tile_below > 0:
                    window.screen.blit(self.tile.surf, ((player_column - 1) * 100, player_row * 100))
                if tile_left > 0:
                    window.screen.blit(tile.tile.surf, ((player_column - 2) * 100, (player_row - 1) * 100))
                if tile_right > 0:
                    window.screen.blit(tile.tile.surf, (player_column * 100, (player_row - 1) * 100))
            except IndexError:
                return False
        except TypeError:
            return False

    def PTR_upper_right(self, player_row, player_column):
        try:
            tile_lst_lr = self.tile_map.get(player_row)
            lower_tile_lst = self.tile_map.get(player_row + 1)
            try:
                tile_lower_left = lower_tile_lst[player_column - 2]
                tile_below = lower_tile_lst[player_column - 1]
                tile_left = tile_lst_lr[player_column - 2]
                if tile_lower_left > 0:
                    window.screen.blit(tile.tile.surf, ((player_column - 2) * 100, player_row * 100))
                if tile_below > 0:
                    window.screen.blit(self.tile.surf, ((player_column - 1) * 100, player_row * 100))
                if tile_left > 0:
                    window.screen.blit(tile.tile.surf, ((player_column - 2) * 100, (player_row - 1) * 100))
            except IndexError:
                return False
        except TypeError:
            return False
    
    def PTR_farRight_column(self, player_row, player_column):
        try:
            above_tile_lst = self.tile_map.get(player_row - 1)
            tile_lst_lr = self.tile_map.get(player_row)
            lower_tile_lst = self.tile_map.get(player_row + 1)
            try:
                tile_upper_left = above_tile_lst[player_column - 2]
                tile_lower_left = lower_tile_lst[player_column - 2]
                tile_below = lower_tile_lst[player_column - 1]
                tile_above = above_tile_lst[player_column - 1]
                tile_left = tile_lst_lr[player_column - 2]
                if tile_above > 0:
                    window.screen.blit(self.tile.surf, ((player_column - 1) * 100, (player_row - 2) * 100))
                if tile_below > 0:
                    window.screen.blit(self.tile.surf, ((player_column - 1) * 100, (player_row) * 100))
                if tile_lower_left > 0:
                    window.screen.blit(self.tile.surf, ((player_column - 2) * 100, player_row * 100))
                if tile_upper_left > 0:
                    window.screen.blit(tile.tile.surf, ((player_column - 2) * 100, (player_row - 2) * 100))
                if tile_left > 0:
                    window.screen.blit(tile.tile.surf, ((player_column - 2) * 100, (player_row - 1) * 100))
            except IndexError:
                return False
        except TypeError:
            return False

    def PTR_bottom_right(self, player_row, player_column):
        try:
            current_row_tile_lst = self.tile_map.get(player_row)
            tile_above_lst = self.tile_map.get(player_row - 1)
            try:
                tile_left = current_row_tile_lst[player_column - 2]
                tile_above = tile_above_lst[player_column - 1]
                tile_upper_left = tile_above_lst[player_column - 2]
                if tile_upper_left > 0:
                    window.screen.blit(tile.tile.surf, ((player_column - 2) * 100, (player_row - 2) * 100))
                if tile_above > 0:
                    window.screen.blit(self.tile.surf, ((player_column - 1) * 100, (player_row - 2) * 100))
                if tile_left > 0:
                    window.screen.blit(tile.tile.surf, ((player_column - 2) * 100, (player_row - 1) * 100))
            except IndexError:
                return False
        except TypeError:
            return False
    
    def PTR_bottom_row(self, player_row, player_column):
        try:
            current_row_tile_lst = self.tile_map.get(player_row)
            tile_above_lst = self.tile_map.get(player_row - 1)
            try:
                tile_left = current_row_tile_lst[player_column - 2]
                tile_above = tile_above_lst[player_column - 1]
                tile_upper_right = tile_above_lst[player_column]
                tile_upper_left = tile_above_lst[player_column - 2]
                tile_right = current_row_tile_lst[player_column]
                if tile_right > 0:
                    window.screen.blit(tile.tile.surf, (player_column * 100, (player_row - 1) * 100))
                if tile_upper_right > 0:
                    window.screen.blit(tile.tile.surf, (player_column * 100, (player_row - 2) * 100))
                if tile_upper_left > 0:
                    window.screen.blit(tile.tile.surf, ((player_column - 2) * 100, (player_row - 2) * 100))
                if tile_above > 0:
                    window.screen.blit(self.tile.surf, ((player_column - 1) * 100, (player_row - 2) * 100))
                if tile_left > 0:
                    window.screen.blit(tile.tile.surf, ((player_column - 2) * 100, (player_row - 1) * 100))
            except IndexError:
                return False
        except TypeError:
            return False

tile_func = tile()
# Prints list of tuples with the row number + the index position of the tiles (Tiles are 1).
#print(tile_func.tile_positions())
# Prints value found in the row (first argument) and column (second argument) inputted.
#row_column = (8, 3)

while True:    
    # Combats lag.
    dt = initial_time - time.time()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        # Basic player movement based on key presses, not keys held down.
        # When tile rendering becomes stable and scalable, switch to held keys.
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_d:
                player.rect.x += 100
            if event.key == pg.K_w:
                player.rect.y -= 100
            if event.key == pg.K_s:
                player.rect.y += 100
            if event.key == pg.K_a:
                player.rect.x -= 100
            
        if player.rect.x < 0:
            player.rect.x = 0
        if player.rect.x > window.dimensions[0] - 100:
            player.rect.x = window.dimensions[0] - 100
        if player.rect.y < 0:
            player.rect.y = 0
        if player.rect.y > window.dimensions[1] - 100:
            player.rect.y = window.dimensions[1] - 100
    
    # *** IMPORTANT NOTE: THE ROW THE PLAYER IS ON IS PLAYER.Y, COLUMN IS PLAYER.X ***

    player.column = int(player.rect.x/100) + 1
    player.row = int(player.rect.y/100) + 1

    window.screen.blit(bg.surf, (0, 0))

    # All functions for checking different parts of the tile map.
    #tile_func.tile_lower_left_right(player.row, player.column)
    #tile_func.tile_upper_left_right(player.row, player.column)
    #tile_func.tile_left_right(player.row, player.column)
    #tile_func.tile_above_below(player.row, player.column)
    # Function for checking all tiles at once, rather than 4 separate functions.
    if player.column == 1 and player.row == 1:
        tile_func.PTR_upper_left(player.row, player.column)
    elif player.column == (window.dimensions[0] / 100) and player.row == (window.dimensions[1] / 100):
        tile_func.PTR_bottom_right(player.row, player.column)
    elif player.row == (window.dimensions[1] / 100):
        tile_func.PTR_bottom_row(player.row, player.column)
    elif player.column == (window.dimensions[0] / 100) and player.row == 1:
        tile_func.PTR_upper_right(player.row, player.column)
    elif player.column == (window.dimensions[0] / 100):
        tile_func.PTR_farRight_column(player.row, player.column)
    elif player.row == 1:
        tile_func.PTR_upper_row(player.row, player.column)
    else:
        tile_func.check_proximity_tiles(player.row, player.column)

    player.position = (player.column, player.row)
    
    window.screen.blit(player.surf, player.rect)
    pg.display.update()
    clock.tick(window.fps)