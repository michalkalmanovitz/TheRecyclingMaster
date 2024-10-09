import consts

bins_list=[]
def create(center_x, center_y, img):
    return {"img":img,
            "center_x": center_x,
            "center_y": center_y,
            }

def create_new_bin():
    x=0
    for image in consts.BIN_IMAGES_LS:
       bins_list.append(create(x,20,image))
       x+=20

#
# def move_in_direction(bubble, direction):
#     bubble["center_x"] += direction[0]
#     bubble["center_y"] += direction[1]
#
#
# def is_colliding_with_wall(bullet_bubble):
#     return bullet_bubble["center_x"] - consts.BUBBLE_RADIUS <= 0 or \
#            bullet_bubble[
#                "center_x"] + consts.BUBBLE_RADIUS >= consts.WINDOW_WIDTH
#
#
# def calc_direction(angle):
#     # y/x = tan(angle)
#     y_movement = 2
#     x_movement = y_movement / math.tan(math.radians(angle))
#     return x_movement, -y_movement
#
#
# def pop(bubbles_grid, bubble_location):
#     bubble_popped = bubbles_grid[bubble_location[0]][bubble_location[1]].copy()
#     bubbles_grid[bubble_location[0]][bubble_location[1]][
#         "color"] = consts.NO_BUBBLE
#     return bubble_popped
#
#
# def is_isolated(bubbles_grid, bubble_location):
#     return is_isolated_inner(bubbles_grid, bubble_location, [])
#
#
# def is_isolated_inner(bubbles_grid, bubble_location, locations_checked):
#     start_row, start_col = bubble_location
#     locations_checked.append(bubble_location)
#
#     # Bubbles on first row are considered not isolated
#     if start_row == 0:
#         return False
#
#     neighbors_directions = BubblesGrid.get_neighbors_directions(start_row)
#
#     for direction in neighbors_directions:
#         new_row = start_row + direction[0]
#         new_col = start_col + direction[1]
#         new_location = (new_row, new_col)
#
#         if 0 <= new_row < len(bubbles_grid) and \
#                 0 <= new_col < consts.BUBBLE_GRID_COLS and \
#                 new_location not in locations_checked and \
#                 bubbles_grid[new_row][new_col]["color"] != consts.NO_BUBBLE and \
#                 not is_isolated_inner(bubbles_grid, new_location,
#                                       locations_checked):
#             return False
#
#     return True
#
#
# # -----------------------------------------------------------------------------
# # ---------------------------------your code-----------------------------------
# # -----------------------------------------------------------------------------
# def get_bubble_color(bullet_bubble):
#     return bullet_bubble["color"]
#
# def should_stop(bubbles_grid, bullet_bubble):
#     # TODO: implement
#     ceiling = 0
#     if bullet_bubble["center_y"] <= ceiling:
#         return True
#
#     for i in range(len(bubbles_grid)):
#         for j in range(len(bubbles_grid[i])):
#             if bubbles_grid[i][j]["color"] != consts.NO_BUBBLE:
#                 distance = math.dist([bubbles_grid[i][j]["center_x"], bubbles_grid[i][j]["center_y"]], [bullet_bubble["center_x"], bullet_bubble["center_y"]])
#                 sum_of_radius = bubbles_grid[i][j]["radius"]+bullet_bubble["radius"]
#                 if distance <= sum_of_radius:
#                     return True
#     return False
#





