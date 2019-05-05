from dungeon_generator import Generator
import term_io
from random import randint
from get_a_joke import get_joke


class dungeon:

    def __init__(self,
                 width=64,
                 height=64,
                 max_rooms=15,
                 min_room_xy=5,
                 max_room_xy=10,
                 rooms_overlap=False,
                 random_connections=1,
                 random_spurs=3):
        self.gen = Generator(width, height, max_rooms, min_room_xy, max_room_xy,
                             rooms_overlap, random_connections, random_spurs)
        self.gen.gen_level()
        # translat stone and wall into 1000; floor into 1100
        self.lvl = [[None for _ in range(width)] for _ in range(height)]
        self.width = width
        self.height = height
        for y in range(height):
            for x in range(width):
                cell = self.gen.level[y][x]
                if (cell == 'wall'):
                    self.lvl[y][x] = 1000
                elif (cell == 'stone'):
                    self.lvl[y][x] = 1001
                elif cell == 'floor':
                    self.lvl[y][x] = 1100
        #        print(rownum,colnum,self.lvl[rownum][colnum])
        # for i in self.lvl:
        #    print(i)
        # self.gen.gen_tiles_level()

        x, y = self.find_a_place_in_room()
        self.lvl[y][x] = 1200  # Exit

        self.jokes = [None for _ in range(5)]
        for i in range(5):
            x, y = self.find_normal_wall()
            self.jokes[i] = get_joke()
            self.lvl[y][x] = 1300 + i  # 1300 is joke stone

        x, y = self.find_a_place_in_room()
        self.lvl[y][x] = 1400  # stele

        self.playerX, self.playerY = self.put_player_in_map()

    def put_player_in_map(self):
        x, y = self.find_space()
        return x, y

    def find_space(self):
        while True:
            x = randint(1, self.width) - 1
            y = randint(1, self.height) - 1
            # print(x,y,self.lvl[y][x])
            if self.lvl[y][x] == 1100:
                # if x y is floor
                return x, y

    def find_normal_wall(self):
        while True:
            try:
                x = randint(1, self.width) - 1
                y = randint(1, self.height) - 1
                # print(x,y,self.lvl[y][x])
                if self.lvl[y][x] == 1000:
                    # if x y is wall normal
                    if (self.lvl[y - 1][x] == 1100) or (
                            self.lvl[y][x - 1] == 1100) or (
                                self.lvl[y + 1][x] == 1100) or (
                                    self.lvl[y][x + 1] == 1100):
                        return x, y
            except IndexError:
                do_nothing = None

    def in_a_room(self, x, y):
        for room in self.gen.room_list:
            if (x > room[0] and y > room[1]):
                if (x < room[0] + room[2] - 1) and (y < room[1] + room[3] - 1):
                    return True
        return False

    def find_a_place_in_room(self):
        while True:
            x, y = self.find_space()
            if self.in_a_room(x, y):
                return x, y

    def move_player(self, direction):
        event = []
        nextX = self.playerX
        nextY = self.playerY
        if direction == 'up':
            nextY -= 1
        if direction == 'down':
            nextY += 1
        if direction == 'left':
            nextX -= 1
        if direction == 'right':
            nextX += 1
        next_block = self.lvl[nextY][nextX]
        if next_block == 1100:
            self.playerX = nextX
            self.playerY = nextY
            event += ["moved"]
        elif int(next_block / 100) == 10:
            event += ["blocked"]
        elif int(next_block / 100) == 12:
            event += ["exit"]
        return event, next_block

    def display_string(self, radius=5):
        space = term_io.bgcolor.reset + term_io.fgcolor.default + " " * 3
        player = term_io.bgcolor.white + term_io.fgcolor.green + "0_0"
        wall = term_io.bgcolor.red + term_io.fgcolor.black + " " * 3  # "░" * 3
        floor = term_io.bgcolor.white + term_io.fgcolor.default + " " * 3
        exit = term_io.bgcolor.white + term_io.fgcolor.blue + "_=¯"
        joke = term_io.bgcolor.red + term_io.fgcolor.Yellow + "." * 3  # "░" * 3
        stele = term_io.bgcolor.white + term_io.fgcolor.blue + "[¯]"

        view_width = [6, 8, 10, 10, 10, 12, 12, 12, 10, 10, 10, 8, 6]
        view_height = len(view_width)

        output = ""
        for i in range(view_height):
            front_space = int(8 - int(view_width[i] / 2))
            output = output + space * front_space
            for j in range(view_width[i]):
                y = self.playerY - 6 + i
                x = self.playerX - 6 + front_space + j
                try:
                    cell = self.lvl[y][x]
                except IndexError:
                    cell = 1001  # stone and space are 1001
                if (x == self.playerX) and (y == self.playerY):
                    output = output + player
                elif cell == 1001:
                    output = output + space
                elif cell == 1000:
                    output = output + wall
                elif cell == 1100:
                    output = output + floor
                elif cell == 1200:
                    output = output + exit
                elif int(cell / 100) == 13:
                    output = output + joke
                elif cell == 1400:
                    output = output + stele
            output = output + "\n"
        return output


def text_circle(rad, ch="123"):
    xscale = 1.7
    #Maximum diameter, plus a little padding
    width = 3 + int(0.5 + xscale * rad)

    rad2 = rad**2
    for y in range(-rad, rad + 1):
        #Find width at this height
        x = int(0.5 + xscale * (rad2 - y**2)**0.5)
        s = ch * x
        print(s.center(140))


def main():
    # text_circle(rad=7)
    dun = dungeon()
    while True:
        key = term_io.direction_and_enter()
        if key is not 'enter':
            dun.move_player(key)
            print(term_io.delete.whole_screen)
            print(dun.display_string())


if __name__ == "__main__":
    main()
