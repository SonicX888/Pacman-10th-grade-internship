import arcade

class Fruits(arcade.Sprite):

    fruit_textures = []
    fruit_eaten = False
    cur_texture = 1
    timer = 0

    def __init__(self, width, height, pos):

        super().__init__()

        self.scale = 0.5 / 3 * ((arcade.window_commands.get_display_size()[1] // 39) / 5.4)

        fruit_points = arcade.load_texture("C:/Users/kylli/OneDrive/Bureau/pacman-main/pacman-main/images/fruits/200.png")
        self.fruit_textures.append(fruit_points)
        main_path_fruit = "C:/Users/kylli/OneDrive/Bureau/pacman-main/pacman-main/images/fruits/logo"
        for i in range(4):
            t_fruit = arcade.load_texture(f"{main_path_fruit}_{i}.png")
            self.fruit_textures.append(t_fruit)
        self.center_x = pos[0] * width + (width/2)
        self.center_y = pos[1] * height + (height/2)

    def fruits_draw(self, coins_count, player_sprite):

        if (coins_count >= 70) and self.fruit_eaten == False:
            if self.cur_texture > 4:
                self.cur_texture = 1
            self.texture = self.fruit_textures[self.cur_texture]
            self.draw()
            self.timer += 1
            hit_fruit = arcade.check_for_collision(sprite1=player_sprite, sprite2=self)
            if hit_fruit == True:
                self.cur_texture += 1
                self.timer = 0
                self.fruit_eaten = True
            if self.timer == 600:
                self.timer = 0
                self.cur_texture += 1
                self.fruit_eaten = True

        if coins_count == 140 or coins_count == 210 or coins_count == 280:
            self.fruit_eaten = False