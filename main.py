import sys
import pygame
import random

pygame.init()

NB_COL = 17
NB_ROW = 17
CELL_SIZE = 40

screen = pygame.display.set_mode(size=(NB_COL * CELL_SIZE, NB_ROW * CELL_SIZE))
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)
timer = pygame.time.Clock()


class Block:
    def __init__(self, x_pos, y_pos):
        self.x = x_pos
        self.y = y_pos


class Score:
    def __init__(self):
        self.points = 0
        self.evilpoints = 0

    def afficher_score(self):
        myfont = pygame.font.SysFont("lato", 20)
        score_display = myfont.render('Score : ' + str(self.points) + " / 10", True, (145, 245, 0))
        screen.blit(score_display, (40, 40))

    def afficher_score_ennemy(self):
        myfont = pygame.font.SysFont("lato", 20)
        score_display = myfont.render('Score : ' + str(self.evilpoints) + " / 6", True, (158, 24, 8))
        screen.blit(score_display, (CELL_SIZE * NB_COL - 120, 40))

    def reset_score(self):
        self.points = 0

    def victory(self):
        if self.points == 10:
            print("Vous avez gagné !!")
            pygame.quit()
            sys.exit()


class Food:

    def __init__(self):
        x = random.randint(0, NB_COL - 1) + 0.5
        y = random.randint(0, NB_ROW - 1) + 0.5
        self.block = Block(x, y)

    def draw_food(self):
        pygame.draw.circle(screen, (0, 92, 235), ((self.block.x * CELL_SIZE), (self.block.y * CELL_SIZE)), 12)


class Snake:
    def __init__(self):
        self.body = [Block(2, 4), Block(3, 4), Block(4, 4)]
        self.direction = "RIGHT"

    def reset_snake(self):
        self.body = [Block(2, 6), Block(3, 6), Block(4, 6)]
        self.direction = "RIGHT"

    def draw_snake(self):
        for block in self.body:
            x_coord = block.x * CELL_SIZE
            y_coord = block.y * CELL_SIZE
            rect = pygame.Rect(x_coord, y_coord, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, (145, 245, 0), rect, border_radius=8)

    def move_snake(self):
        len_snake = len(self.body)
        old_head = self.body[len_snake - 1]
        if self.direction == "RIGHT":
            new_head = Block(old_head.x + 1, old_head.y)
        elif self.direction == "LEFT":
            new_head = Block(old_head.x - 1, old_head.y)
        elif self.direction == "TOP":
            new_head = Block(old_head.x, old_head.y - 1)
        else:
            new_head = Block(old_head.x, old_head.y + 1)
        self.body.append(new_head)


class EvilSnake:
    def __init__(self):
        self.body = [Block(13, 10), Block(12, 10), Block(11, 10), Block(10, 10), Block(9, 10), Block(8, 10)]
        self.direction = "LEFT"

    def draw_evsnake(self):
        for block in self.body:
            x_coord = block.x * CELL_SIZE
            y_coord = block.y * CELL_SIZE
            rect = pygame.Rect(x_coord, y_coord, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, (158, 24, 8), rect, border_radius=8)

    def move_snake(self):
        global new_head_es
        len_snake = len(self.body)
        old_head = self.body[len_snake - 1]

        if self.direction == "RIGHT":
            new_head_es = Block(old_head.x + 1, old_head.y)
        elif self.direction == "LEFT":
            new_head_es = Block(old_head.x - 1, old_head.y)
        elif self.direction == "TOP":
            new_head_es = Block(old_head.x, old_head.y - 1)
        elif self.direction == "DOWN":
            new_head_es = Block(old_head.x, old_head.y + 1)
        self.body.append(new_head_es)

    def condition_bot(self):
        global value
        len_snake = len(self.body)
        head = self.body[len_snake - 1]
        if 1 <= head.x <= NB_COL - 1 and 1 <= head.y <= NB_ROW - 1:
            value = True
        else:
            value = False
        return value

    def in_limit(self):
        len_snake = len(self.body)
        head = self.body[len_snake - 1]
        coord_x = head.x
        coord_y = head.y
        if coord_x > NB_COL - 1:
            game.evilSnake.direction = "LEFT"
        if coord_x < 1:
            game.evilSnake.direction = "RIGHT"
        if coord_y < 1:
            game.evilSnake.direction = "DOWN"
        if coord_y > NB_ROW - 1:
            game.evilSnake.direction = "TOP"

    @staticmethod
    def random_move():
        if game.evilSnake.direction == "RIGHT":
            game.evilSnake.direction = random.choice(movementRight)
        elif game.evilSnake.direction == "LEFT":
            game.evilSnake.direction = random.choice(movementLeft)
        elif game.evilSnake.direction == "DOWN":
            game.evilSnake.direction = random.choice(movementDown)
        elif game.evilSnake.direction == "TOP":
            game.evilSnake.direction = random.choice(movementTop)

    def detection_food_near(self):
        snake_length2 = len(game.evilSnake.body)
        snake_head2 = game.evilSnake.body[snake_length2 - 1]
        food_block = game.food.block
        x_food = food_block.x - 0.5
        y_food = food_block.y - 0.5
        if snake_head2.x == x_food and snake_head2.y == y_food - 1:
            self.direction = "DOWN"
        if snake_head2.x == x_food and snake_head2.y == y_food + 1:
            self.direction = "TOP"
        if snake_head2.x == x_food + 1 and snake_head2.y == y_food:
            self.direction = "LEFT"
        if snake_head2.x == x_food - 1 and snake_head2.y == y_food:
            self.direction = "RIGHT"

    def detection_food_far(self):
        snake_length2 = len(game.evilSnake.body)
        snake_head2 = game.evilSnake.body[snake_length2 - 1]
        food_block = game.food.block
        x_food = food_block.x - 0.5
        y_food = food_block.y - 0.5
        if snake_head2.x == x_food and snake_head2.y == y_food - 2:
            self.direction = "DOWN"
        if snake_head2.x == x_food and snake_head2.y == y_food + 2:
            self.direction = "TOP"
        if snake_head2.x == x_food + 2 and snake_head2.y == y_food:
            self.direction = "LEFT"
        if snake_head2.x == x_food - 2 and snake_head2.y == y_food:
            self.direction = "RIGHT"

    def detection_food_too_far(self):
        snake_length2 = len(game.evilSnake.body)
        snake_head2 = game.evilSnake.body[snake_length2 - 1]
        food_block = game.food.block
        x_food = food_block.x - 0.5
        y_food = food_block.y - 0.5
        if snake_head2.x == x_food and snake_head2.y == y_food - 3:
            self.direction = "DOWN"
        if snake_head2.x == x_food and snake_head2.y == y_food + 3:
            self.direction = "TOP"
        if snake_head2.x == x_food + 3 and snake_head2.y == y_food:
            self.direction = "LEFT"
        if snake_head2.x == x_food - 3 and snake_head2.y == y_food:
            self.direction = "RIGHT"

    def detection_snake_near(self):
        snake_length2 = len(game.evilSnake.body)
        snake_head2 = game.evilSnake.body[snake_length2 - 1]
        for block in game.snake.body:
            if snake_head2.x == block.x + 1 and snake_head2.y == block.y:
                self.direction = "RIGHT"
            if snake_head2.x == block.x - 1 and snake_head2.y == block.y:
                self.direction = "LEFT"
            if snake_head2.x == block.x and snake_head2.y == block.y - 1:
                self.direction = "DOWN"
            if snake_head2.x == block.x and snake_head2.y == block.y + 1:
                self.direction = "TOP"

    def detection_snake_far(self):
        snake_length2 = len(game.evilSnake.body)
        snake_head2 = game.evilSnake.body[snake_length2 - 1]
        for block in game.snake.body:
            if snake_head2.x == block.x + 2 and snake_head2.y == block.y:
                self.direction = "RIGHT"
            if snake_head2.x == block.x - 2 and snake_head2.y == block.y:
                self.direction = "LEFT"
            if snake_head2.x == block.x and snake_head2.y == block.y - 2:
                self.direction = "DOWN"
            if snake_head2.x == block.x and snake_head2.y == block.y + 2:
                self.direction = "TOP"


class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = Food()
        self.evilSnake = EvilSnake()
        self.generate_food()
        self.score = Score()

    def update(self):
        self.snake.move_snake()
        self.evilSnake.move_snake()
        self.check_head_on_food()
        self.check_head_on_food_ennemy()
        self.game_over()
        self.score.victory()

    def draw_game_element(self):
        self.score.afficher_score()
        self.score.afficher_score_ennemy()
        self.food.draw_food()
        self.snake.draw_snake()
        self.evilSnake.draw_evsnake()

    def check_head_on_food(self):
        snake_length = len(self.snake.body)
        snake_head = self.snake.body[snake_length - 1]
        food_block = self.food.block
        x_food = food_block.x - 0.5
        y_food = food_block.y - 0.5
        if snake_head.x == x_food and snake_head.y == y_food:
            self.score.points += 1
            self.generate_food()
        else:
            self.snake.body.pop(0)

    def check_head_on_food_ennemy(self):
        snake_length2 = len(self.evilSnake.body)
        snake_head2 = self.evilSnake.body[snake_length2 - 1]
        food_block = self.food.block
        x_food = food_block.x - 0.5
        y_food = food_block.y - 0.5
        if snake_head2.x == x_food and snake_head2.y == y_food:
            self.score.evilpoints += 1
            self.generate_food()
        else:
            self.evilSnake.body.pop(0)

    def generate_food(self):
        self.food = Food()
        should_generate_food = True
        while should_generate_food:
            count = 0
            for block in self.snake.body:
                if block.x == self.food.block.x and block.y == self.food.block.y:
                    count += 1
            if count == 0:
                should_generate_food = False
            else:
                self.food = Food()

    def game_over(self):
        snake_length = len(self.snake.body)
        snake_head = self.snake.body[snake_length - 1]
        if snake_head.x not in range(0, NB_COL) or snake_head.y not in range(0, NB_ROW):
            self.score.reset_score()
            self.snake.reset_snake()
        for block in self.snake.body[0: snake_length - 1]:
            if snake_head.x == block.x and snake_head.y == block.y:
                self.score.reset_score()
                self.snake.reset_snake()
        for contact in self.snake.body:
            for bad in self.evilSnake.body:
                if contact.x == bad.x and contact.y == bad.y:
                    self.score.reset_score()
                    self.snake.reset_snake()
        if self.score.evilpoints == 6:
            print("Vous avez perdu !!")
            pygame.quit()
            sys.exit()


def show_grid():
    for i in range(0, NB_COL):
        for j in range(0, NB_ROW):
            rect = pygame.Rect(i * CELL_SIZE, j * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, 'black', rect, width=1)


game_on = True

movementRight = ["DOWN", "TOP", "RIGHT", "RIGHT", "RIGHT", "RIGHT", "RIGHT"]
movementLeft = ["DOWN", "TOP", "LEFT", "LEFT", "LEFT", "LEFT", "LEFT", "LEFT"]
movementTop = ["RIGHT", "TOP", "LEFT", "TOP", "TOP", "TOP", "TOP"]
movementDown = ["DOWN", "RIGHT", "LEFT", "DOWN", "DOWN", "DOWN", "DOWN"]
choicebot = [1, 2]
game = Game()


while game_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            game.update()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if game.snake.direction != "DOWN":
                    game.snake.direction = "TOP"
            if event.key == pygame.K_DOWN:
                if game.snake.direction != "TOP":
                    game.snake.direction = "DOWN"
            if event.key == pygame.K_RIGHT:
                if game.snake.direction != "LEFT":
                    game.snake.direction = "RIGHT"
            if event.key == pygame.K_LEFT:
                if game.snake.direction != "RIGHT":
                    game.snake.direction = "LEFT"

        game.evilSnake.condition_bot()
        # noinspection PyUnboundLocalVariable
        if not value:
            game.evilSnake.in_limit()
        else:
            game.evilSnake.detection_food_too_far()
            game.evilSnake.detection_food_far()
            game.evilSnake.detection_food_near()
            game.evilSnake.detection_snake_far()
            game.evilSnake.detection_snake_near()
            game.evilSnake.random_move()

    screen.fill('black')
    # show_grid()
    game.draw_game_element()
    pygame.display.update()
    timer.tick(60)
