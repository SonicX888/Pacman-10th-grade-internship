import arcade
import time
from src.Characters.PacmanCharacter import PacmanCharacter
from src.Characters.Ghosts import Ghosts
from src.Fruits.Fruits import Fruits
from src.Fruits.Points import Points_sprite

WIDTH = arcade.window_commands.get_display_size()[0]
HEIGHT = arcade.window_commands.get_display_size()[1]
SPRITE_SCALING = 0.5
grid = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 1],
            [1, 2, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 2, 1],
            [1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1],
            [1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 2, 2, 2, 1, 1, 2, 1, 1, 1, 2, 1, 1, 2, 2, 2, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1],
            [1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1],
            [1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1],
            [1, 2, 1, 2, 1, 2, 1, 1, 1, 1, 2, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 2, 1, 1, 1, 1, 2, 1, 2, 1, 2, 1],
            [1, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 1, 0, 0, 0, 0, 0, 1, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1],
            [1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 0, 0, 0, 0, 0, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1],
            [1, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 1, 0, 0, 0, 0, 0, 1, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1],
            [1, 2, 1, 2, 1, 2, 1, 1, 1, 1, 2, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 2, 1, 1, 1, 1, 2, 1, 2, 1, 2, 1],
            [1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1],
            [1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1],
            [1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 2, 2, 2, 1, 1, 2, 1, 1, 1, 2, 1, 1, 2, 2, 2, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1],
            [1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1],
            [1, 2, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 2, 1],
            [1, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

pacman_pos = [19, 17]




class MenuView(arcade.View):


    def on_show_view(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        self.clear()
        arcade.draw_text("PACMAN", WIDTH / 2, HEIGHT / 2,
                         arcade.color.PINK, font_size=50, anchor_x="center", font_name="ARCADECLASSIC")
        arcade.draw_text("Click  to  show  keybinds", WIDTH / 2, HEIGHT / 2 - 75,
                         arcade.color.AMBER, font_size=20, anchor_x="center", font_name="ARCADECLASSIC")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        instructions_view = InstructionView()
        self.window.show_view(instructions_view)


class InstructionView(arcade.View):
    def on_show_view(self):
        arcade.set_background_color(arcade.color.PINK)

    def on_draw(self):
        self.clear()
        arcade.draw_text("USE ARROW KEYS", WIDTH / 2, HEIGHT / 2,
                         arcade.color.BLACK, font_size=50, anchor_x="center", font_name="ARCADECLASSIC")
        arcade.draw_text("You  only  have  3  lives", WIDTH / 2, HEIGHT / 2 - 75,
                         arcade.color.BLACK, font_size=20, anchor_x="center", font_name="ARCADECLASSIC")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = GameView()
        GameView.setup(GameView)
        self.window.show_view(game_view)


class GameView(arcade.View):

    player_sprite = None
    coin_list = None
    wall_list = None
    fruit_sprite = None
    fruit_pos = [19, 12]
    fruit_eaten = True
    points_show = False
    points_time = 180
    time_spent = 0
    ghosts_pos = [19, 6]
    ghost_sprite_red = None
    ghost_sprite_pink = None
    ghost_sprite_blue = None
    ghost_sprite_orange = None
    ghost_red_apparition = False
    ghost_pink_apparition = False
    ghost_blue_apparition = False
    ghost_orange_apparition = False
    ghost_sprites = None
    timer_init = 0
    timer = 0
    timer2 = 0
    died = 0
    coins_count = 0
    touched = False

    def __init__(self):

        self.timer_init = time.time()

        super().__init__()

        self.score = 0

    def setup(self):
        ratio = len(grid[0]) / (len(grid) + 2)
        if ratio / WIDTH > HEIGHT:
            self.case_size = HEIGHT // (len(grid) + 2)
        else:
            self.case_size = WIDTH // len(grid[0])

        self.width_case = self.case_size
        self.height_case = self.case_size
        self.player_sprite = PacmanCharacter(self.width_case, self.height_case, pacman_pos)
        self.ghost_sprites = arcade.SpriteList()
        self.fruit_sprite = Fruits(self.width_case, self.height_case, self.fruit_pos)
        self.points_sprite = Points_sprite(self.width_case, self.height_case, self.fruit_pos)
        self.setup_grid(self)
        self.waka_sound = arcade.load_sound("C:/Users/kylli/OneDrive/Bureau/pacman-main/pacman-main/sounds/Pacman sound2.wav")

    def update_ghosts(self):
        self.timer = time.time() - self.timer_init
        if (self.timer > 0 or self.timer2 > 0) and not self.ghost_red_apparition:
            self.ghost_sprite_red = Ghosts(self.width_case, self.height_case, self.ghosts_pos)
            self.ghost_red_apparition = True
            self.ghost_sprites.append(self.ghost_sprite_red)
        if (self.timer > 5 or self.timer2 > 5) and not self.ghost_pink_apparition:
            self.ghost_sprite_pink = Ghosts(self.width_case, self.height_case, self.ghosts_pos)
            self.ghost_pink_apparition = True
            self.ghost_sprites.append(self.ghost_sprite_pink)
        if (self.timer > 10 or self.timer2 > 10) and not self.ghost_blue_apparition:
            self.ghost_sprite_blue = Ghosts(self.width_case, self.height_case, self.ghosts_pos)
            self.ghost_blue_apparition = True
            self.ghost_sprites.append(self.ghost_sprite_blue)
        if (self.timer > 15 or self.timer2 > 15) and not self.ghost_orange_apparition:
            self.ghost_sprite_orange = Ghosts(self.width_case, self.height_case, self.ghosts_pos)
            self.ghost_orange_apparition = True
            self.ghost_sprites.append(self.ghost_sprite_orange)

        if self.ghost_red_apparition == True:
            self.ghost_sprite_red.update(grid, self.player_sprite)
        if self.ghost_pink_apparition == True:
            self.ghost_sprite_pink.update(grid, self.player_sprite)
        if self.ghost_blue_apparition == True:
            self.ghost_sprite_blue.update(grid, self.player_sprite)
        if self.ghost_orange_apparition == True:
            self.ghost_sprite_orange.update(grid, self.player_sprite)

    def setup_grid(self):
        self.wall_list = arcade.SpriteList(is_static=True, use_spatial_hash=True)
        self.coin_list = arcade.SpriteList(is_static=True, use_spatial_hash=True)
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == 1:
                    wall = arcade.SpriteSolidColor(self.width_case, self.height_case, arcade.color.AMBER)
                    wall.center_x = (column * self.width_case) + self.width_case / 2
                    wall.center_y = (row * self.height_case) + self.height_case / 2
                    self.wall_list.append(wall)
                if grid[row][column] == 2:
                    coin = arcade.SpriteSolidColor(self.width_case, self.height_case, arcade.color.WHITE)
                    coin.center_x = (column * self.width_case) + self.width_case / 2
                    coin.center_y = (row * self.height_case) + self.height_case / 2
                    coin.scale = 0.2
                    self.coin_list.append(coin)


    def on_key_press(self, key, modifiers):
        match key:
            case arcade.key.RIGHT | arcade.key.LEFT | arcade.key.UP | arcade.key.DOWN:
                self.player_sprite.desired_direction = key

    def on_update(self, delta_time: float):
        self.hit_list_coins = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
        for coin in self.hit_list_coins:
            coin.kill()
            # coin.remove_from_sprite_lists()
            self.score += 10
            self.coins_count += 1
            arcade.play_sound(self.waka_sound)
        self.player_sprite.update(grid, delta_time)
        self.update_ghosts()


        self.hit_list_ghosts = arcade.check_for_collision_with_list(self.player_sprite, self.ghost_sprites)
        if len(self.hit_list_ghosts) > 0:
            if self.died < 2:
                self.player_sprite.direction = None
                self.player_sprite.desired_direction = None
                self.player_sprite.center_x = 760.5
                self.player_sprite.center_y = 682.5
                self.ghost_sprite_red.kill()
                self.ghost_sprite_red.center_x = 763.5
                self.ghost_sprite_red.center_y = 253.5
                if self.ghost_pink_apparition == True:
                    self.ghost_sprite_pink.center_x = 760.5
                    self.ghost_sprite_pink.center_y = 253.5
                    self.ghost_sprite_pink.kill()
                    self.ghost_pink_apparition = False
                if self.ghost_blue_apparition == True:
                    self.ghost_sprite_blue.center_x = 760.5
                    self.ghost_sprite_blue.center_y = 253.5
                    self.ghost_sprite_blue.kill()
                    self.ghost_blue_apparition = False
                if self.ghost_orange_apparition == True:
                    self.ghost_sprite_orange.center_x = 760.5
                    self.ghost_sprite_orange.center_y = 253.5
                    self.ghost_sprite_orange.kill()
                    self.ghost_orange_apparition = False
                self.timer2 = 0
                self.died += 1
                self.touched = True
            else:
                game_over = GameOverView()
                self.window.show_view(game_over)


        if len(self.coin_list) == 0:
            self.setup()
            self.timer = 0
        if self.touched == True:
            self.timer2 +=1


    def on_show_view(self):
        arcade.set_background_color(arcade.color.BLACK)

        # Don't show the mouse cursor
        self.window.set_mouse_visible(False)



    def on_draw(self):
        """ Render the screen. """
        self.clear()
        self.wall_list.draw()
        self.coin_list.draw()
        self.player_sprite.draw()
        self.ghost_sprites.draw()

        score_text = f"Score: {self.score}"
        arcade.draw_text(score_text, arcade.window_commands.get_display_size()[0] // len(grid[0]),
                         arcade.window_commands.get_display_size()[1] // 1.1, arcade.csscolor.WHITE,
                         30 / 3 * ((arcade.window_commands.get_display_size()[1] // 39) / 7.5),
                         font_name="ARCADECLASSIC")
        self.fruit_sprite.fruits_draw(coins_count=self.coins_count, player_sprite=self.player_sprite)
        self.points_sprite.points_draw()
        if self.coins_count == 70 or self.coins_count == 140 or self.coins_count == 210 or self.coins_count == 280:
            self.fruit_eaten = False
        if self.fruit_eaten == False:
            hit_fruit = arcade.check_for_collision(sprite1=self.player_sprite, sprite2=self.fruit_sprite)
            if hit_fruit == True:
                self.score += 200
                self.fruit_eaten = True
                self.points_show = True

        if self.points_show == True:
            timer = self.timer - self.timer + time.time()

            while timer < 10:
                self.points_sprite.draw()
                break

            self.points_show = False


    def score(self):
        return self.score


class GameOverView(arcade.View):
    def __init__(self):
        super().__init__()
        self.time_taken = 0

    def on_show_view(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        self.clear()
        """
        Draw "Game over" across the screen.
        """
        arcade.draw_text("Game Over", WIDTH / 2, HEIGHT / 2 - 50, arcade.color.PINK, font_size=54, anchor_x="center", font_name="ARCADECLASSIC")
        arcade.draw_text("Click  to  restart", WIDTH / 2, HEIGHT / 2 - 50, arcade.color.PINK, font_size=24, anchor_x="center", font_name="ARCADECLASSIC")



    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = GameView()
        self.window.show_view(game_view)


def main():
    window = arcade.Window(WIDTH, HEIGHT, "PACMAN STYLE KI", update_rate=1/40)
    window.total_score = 0
    menu_view = MenuView()
    window.show_view(menu_view)
    arcade.run()


if __name__ == "__main__":
    main()