import arcade
class EntityClass(arcade.Sprite):
    frame_count = 0
    PLAYER_MOVEMENT_SPEED = 3

    def __init__(self, width, height, pos, name_file, folder_name):

        super().__init__()

        self.width_case = width
        self.height_case = height

        self.cur_texture = 0
        main_path = (f"C:/Users/kylli/OneDrive/Bureau/pacman-main/pacman-main/images/animations/{folder_name}/{name_file}")
        for i in range(3):
            t_entity = arcade.load_texture(f"{main_path}_{i}.png")
            self.textures.append(t_entity)

        self.texture = self.textures[0]
        #self.width = width
        #self.height = height
        self.scale = width/self.width
        self.center_x = pos[0] * width + (width/2)
        self.center_y = pos[1] * height + (height/2)

    def update_animation(self, delta_time: float = 1 / 60):
        self.frame_count += 1
        if self.frame_count % 8 == 0:
            self.cur_texture += 1
            if self.cur_texture > 2:
                self.cur_texture = 0
        self.texture = self.textures[self.cur_texture]



    def move(self, grid):
        # Calcule la nouvelle position en fonction de la direction souhaitée
        next_x, next_y = self.center_x, self.center_y

        if self.desired_direction == arcade.key.RIGHT:
            if self.frame_count % 8 == 0:
                next_x += self.width_case
                self.angle = 180
        elif self.desired_direction == arcade.key.LEFT:
            if self.frame_count % 8 == 0:
                next_x -= self.width_case
                self.angle = 0
        elif self.desired_direction == arcade.key.UP:
            if self.frame_count % 8 == 0:
                next_y += self.height_case
                self.angle = -90
        elif self.desired_direction == arcade.key.DOWN:
            if self.frame_count % 8 == 0:
                next_y -= self.height_case
                self.angle = 90

        # Conversion des coordonnées sprite en coordonnées grille
        grid_x = int(next_x // self.width_case)
        grid_y = int(next_y // self.height_case)

        # Vérifiez si la case est un mur (1 dans la grille)
        if grid[grid_y][grid_x] != 1:
            # Déplace Pac-Man si la case suivante n'est pas un mur
            self.center_x = next_x
            self.center_y = next_y
            self.direction = self.desired_direction
        else:
            # Sinon, arrête le mouvement
            self.desired_direction = None

    def will_collide(self, direction, grid):

        new_x = self.center_x + self.change_x
        new_y = self.center_y + self.change_y

        # Calculer la position sur la grille
        grid_x = int(new_x / self.width_case)
        grid_y = int(new_y / self.height_case)

        # Vérifier si la nouvelle position correspond à un mur (1 dans la grille)
        if grid[grid_y][grid_x] == 1:
            return True
        else:
            # Si c'est un mur, on stoppe le mouvement
            return False
        #if direction == None:
         #   return False

        #match direction:
         #   case arcade.key.UP:
          #      return grid[int(self.center_y // self.height_case) + 1][int(self.center_x // self.width_case)] == 1
           # case arcade.key.DOWN:
            #    return grid[int(self.center_y // self.height_case) - 1][int(self.center_x // self.width_case)] == 1
            #case arcade.key.LEFT:
             #   return grid[int(self.center_y // self.height_case)][(int(self.center_x) // self.width_case) - 1] == 1
            #case arcade.key.RIGHT:
             #   return grid[int(self.center_y // self.height_case)][int(self.center_x // self.width_case) + 1] == 1

        #return False
