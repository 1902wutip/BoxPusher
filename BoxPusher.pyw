import time
import turtle
import numpy as np
from BoxPusherMaps import EMPTY,WALL,TARGET,BOX,PLAYER,maps
turtle.register_shape("box.gif")


def game_to_screen(game,pos):
    """numpy coordinate -> screen coordinate"""
    game_map = game.maps[game.level-1]["game_map"]
    height,width = game_map.shape[0],game_map.shape[1]
    return (pos[1] - width//2) * 40, (height//2 - pos[0]) * 40  ##  centralized visualization


##  draw static element
def draw_statics(game):
    
    ##  wall
    game.drawer.color("#333333")
    for x, y in game.walls:
        sx, sy = game_to_screen(game,(x, y))
        game.drawer.goto(sx-20, sy+20)
        game.drawer.pendown()
        game.drawer.begin_fill()
        for _ in range(4):
            game.drawer.forward(40)
            game.drawer.right(90)
        game.drawer.end_fill()
        game.drawer.penup()
    
    ##  destination
    game.drawer.color("red")
    for x, y in game.goals:
        sx, sy = game_to_screen(game,(x, y))
        game.drawer.goto(sx, sy)
        game.drawer.dot(20)


##  ================= logic flow =================
def update_graphics(game):
    """update graphic interface"""
    ##  update player
    sx, sy = game_to_screen(game,game.player_pos)
    game.player.goto(sx, sy)
    
    ##  update boxes
    for t, (x, y) in zip(game.box_turtles, game.boxes):
        sx, sy = game_to_screen(game,(x, y))
        t.goto(sx, sy)
        t.shape("circle" if (x, y) in game.goals else "box.gif")
        t.color("gold" if (x, y) in game.goals else "brown")
        t.shapesize(1,1)
    
    game.screen.update()

def is_valid(game,new_pos):
    """check whether the movement is feasible"""
    x, y = new_pos
    return (
        0 <= x < game.maps[game.level-1]["game_map"].shape[0] and 
        0 <= y < game.maps[game.level-1]["game_map"].shape[1] and
        (x, y) not in game.walls
    )

def click(game, x, y):
    if game.game_active == False:
        game.levelup(game.level)

def move(game, dx, dy):

    if game.game_active == False:
        return None
    new_pos = (game.player_pos[0] + dx, game.player_pos[1] + dy)
    if not is_valid(game,new_pos):
        return None
    
    ##  check whether there is a box ahead to push
    if new_pos in game.boxes:
        box_idx = game.boxes.index(new_pos)
        box_new_pos = (new_pos[0] + dx, new_pos[1] + dy)
        if is_valid(game,box_new_pos) and box_new_pos not in game.boxes:
            game.boxes = [box_new_pos if i == box_idx else p for i, p in enumerate(game.boxes)]
            game.player_pos = new_pos
    else:
        game.player_pos = new_pos
    
    update_graphics(game)
    
    ##  check whether victory
    if game.game_active == True and all(pos in game.goals for pos in game.boxes):
        game.game_active = False
        game.level += 1
        game.win_text.write("Victory!", align="center", font=("Arial", 32, "bold"))

    ##  check whether failed for maximal steps
    game.steps += 1
    game.stepper.clear()
    game.stepper.write(f"步数: {game.steps} / {game.MOVE_LIMIT}", align="right", font=("Microsoft YaHei", 14, "bold"))
    if game.game_active == True and game.steps >= game.MOVE_LIMIT:
        game.game_active = False
        game.fail_text.write("Failure: Steps Exhausted!", align="center", font=("Arial", 32, "bold"))

def update_timer(game):
    """update current time every second"""
    if game.game_active:
        now = time.time() - game.t0
        game.timer.clear()
        game.timer.write(f"用时: {format_time(now)} / {format_time(game.TIME_LIMIT)}", 
                         align="left", font=("Microsoft YaHei", 14, "bold"))
        ##  check whether failed for time out
        if game.game_active == True and now >= game.TIME_LIMIT:
            game.game_active = False
            game.fail_text.write("Failure: TimeOut!", align="center", font=("Arial", 32, "bold"))
        game.screen.ontimer(lambda: update_timer(game), 1000)  ##  recursive call every second

def format_time(seconds):
    """seconds -> mm:ss"""
    return f"{int(seconds//60):02}:{int(seconds%60):02}"


class Game():

    def __init__(self,maps,EMPTY,WALL,TARGET,BOX,PLAYER):

        ##  initialization
        self.level = 1
        self.game_active = False
        self.t0 = time.time()
        self.steps = 0
        self.maps = maps
        self.encoding = {"EMPTY":EMPTY,"WALL":WALL,"TARGET":TARGET,"BOX":BOX,"PLAYER":PLAYER}

        ##  timer initialization
        self.timer = turtle.Turtle()
        self.timer.hideturtle()
        self.timer.penup()
        self.timer.goto(-360, 360)  ##  upper left

        ##  step counter initialization
        self.stepper = turtle.Turtle()
        self.stepper.hideturtle()
        self.stepper.penup()
        self.stepper.goto(360, 360)  ##  upper right

        self.drawer = turtle.Turtle()
        self.drawer.hideturtle()
        self.drawer.penup()
        self.drawer.color("red")
        self.drawer.write("Welcome to the Game BoxPusher.\nPlease Click the Mouse to Start.",
                          align="center",font=("Microsoft YaHei",20,"bold"))
        self.win_text = turtle.Turtle()
        self.win_text.hideturtle()
        self.win_text.color("green")
        self.fail_text = turtle.Turtle()
        self.fail_text.hideturtle()
        self.fail_text.color("red")
        
        self.ui()

    def ui(self):

        ##  graphical interface
        self.screen = turtle.Screen()
        self.screen.setup(800, 800)
        self.screen.title("手术SB推箱子小游戏")
        self.screen.tracer(0)
        
        ##  keyboard monitoring
        self.screen.listen()
        self.screen.onkey(lambda: move(self, -1, 0), "Up")
        self.screen.onkey(lambda: move(self, 1, 0), "Down")
        self.screen.onkey(lambda: move(self, 0, -1), "Left")
        self.screen.onkey(lambda: move(self, 0, 1), "Right")
        self.screen.onclick(lambda x,y: click(self,x,y))

    def levelup(self,level):

        ##  screen initialization
        self.drawer.goto(0,0)
        self.timer.clear()
        self.stepper.clear()
        self.drawer.clear()
        self.win_text.clear()
        self.fail_text.clear()
        if hasattr(self,"player"):
            self.player.hideturtle()
            del self.player
        if hasattr(self,"box_turtles"):
            for box_turtle in self.box_turtles:
                box_turtle.hideturtle()
                del box_turtle
        self.screen.update()

        ##  level initialization
        self.level = level
        if self.level > len(self.maps):
            self.drawer.write(f"You Win the Game!!!",align="center",font=("Microsoft YaHei",30,"bold"))
            return
        self.drawer.write(f"Level {level}",align="center",font=("Microsoft YaHei",36,"bold"))
        time.sleep(3)
        self.drawer.clear()

        ##  map initialization
        self.TIME_LIMIT = self.maps[self.level-1]["TIME_LIMIT"]
        self.MOVE_LIMIT = self.maps[self.level-1]["MOVE_LIMIT"]
        game_map = self.maps[self.level-1]["game_map"]
        self.walls = set(tuple(pos) for pos in np.argwhere(game_map == WALL))
        self.goals = set(tuple(pos) for pos in np.argwhere(game_map == TARGET))
        self.boxes = [tuple(pos) for pos in np.argwhere(game_map == BOX)]
        self.player_pos = tuple(np.argwhere(game_map == PLAYER)[0])

        ##  player initialization
        self.player = turtle.Turtle()
        self.player.shape("turtle")
        self.player.color("blue")
        self.player.penup()

        ##  box initialization
        self.box_turtles = []
        for _ in self.boxes:
            t = turtle.Turtle()
            t.shape("box.gif")
            t.penup()
            self.box_turtles.append(t)

        ##  timer & stepper initialization
        self.t0 = time.time()
        self.steps = 0
        self.timer.write(f"用时: {format_time(0)} / {format_time(self.TIME_LIMIT)}",
                         align="left",font=("Microsoft YaHei",14,"bold"))
        self.stepper.write(f"步数: 0 / {self.MOVE_LIMIT}",align="right",font=("Microsoft YaHei",14,"bold"))

        ##  game activation
        self.game_active = True
        update_timer(self)
        draw_statics(self)
        update_graphics(self)


if __name__ == "__main__":
    ##  game running
    game = Game(maps,EMPTY,WALL,TARGET,BOX,PLAYER)
    turtle.done()