# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sky(canvas, scene_width, scene_height)
    draw_cloud(canvas)
    draw_ground(canvas, scene_width, scene_height)
    draw_sun(canvas)
    draw_house(canvas)


    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.
def draw_sky(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, scene_height/3, scene_width, scene_height, width=0, fill="sky blue")

def draw_cloud(canvas):
    draw_oval(canvas, 100, 275, 200, 375, width=0, fill="white")
    draw_oval(canvas, 150, 325, 250, 425, width=0, fill="white")
    draw_oval(canvas, 150, 275, 250, 375, width=0, fill="white")
    draw_oval(canvas, 200, 325, 300, 425, width=0, fill="white")
    draw_oval(canvas, 200, 275, 300, 375, width=0, fill="white")
    draw_oval(canvas, 225, 300, 325, 400, width=0, fill="white")
    
    draw_oval(canvas, 400, 325, 500, 425, width=0, fill="white")
    draw_oval(canvas, 450, 375, 550, 475, width=0, fill="white")
    draw_oval(canvas, 450, 325, 550, 425, width=0, fill="white")
    draw_oval(canvas, 500, 375, 600, 475, width=0, fill="white")
    draw_oval(canvas, 500, 325, 600, 425, width=0, fill="white")
    draw_oval(canvas, 525, 350, 625, 450, width=0, fill="white")


def draw_ground(canvas, scene_width, scene_height):
    """Draw the ground and all the objects on the ground."""
    draw_rectangle(canvas, 0, 0,
        scene_width, scene_height / 3, width=0, fill="tan4")

    # Draw a pine tree.
    tree_center_x = 170
    tree_bottom = 100
    tree_height = 200
    draw_pine_tree(canvas, tree_center_x, tree_bottom, tree_height)

    # Draw another pine tree.
    tree_center_x = 90
    tree_bottom = 70
    tree_height = 220
    draw_pine_tree(canvas, tree_center_x, tree_bottom, tree_height)


def draw_pine_tree(canvas, center_x, bottom, height):
    trunk_width = height / 10
    trunk_height = height / 5
    trunk_left = center_x - trunk_width / 2
    trunk_right = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height

    # Draw the trunk of the pine tree.
    draw_rectangle(canvas, trunk_left, trunk_top, trunk_right, bottom, outline="gray20", width=1, fill="tan3")

    skirt_width = height / 2
    skirt_left = center_x - skirt_width / 2
    skirt_right = center_x + skirt_width / 2
    skirt_top = bottom + height

    # Draw the crown (also called skirt) of the pine tree.
    draw_polygon(canvas, center_x, skirt_top, skirt_right, trunk_top, skirt_left, trunk_top, outline="gray20", width=1, fill="dark green")
    

def draw_sun(canvas):
    draw_oval(canvas, 700, 400, 950, 650, width=0, fill="yellow") # the Sun 
    draw_line(canvas, 750, 400, 700, 350, width=2, fill="yellow")
    draw_line(canvas, 725, 425, 675, 375, width=2, fill="yellow")
    draw_line(canvas, 700, 450, 650, 400, width=2, fill="yellow")


def draw_house(canvas):
    draw_rectangle(canvas, 500, 100, 700, 300, width=0, fill="peach Puff") # the body of the house
    draw_polygon(canvas, 475, 300, 600, 400, 725, 300, width=0, fill="brown" ) # the roof of the house
    draw_rectangle(canvas, 525, 200, 600, 275, width=1, fill="lavender") # the window in the house
    draw_line(canvas, (600 + 525) / 2, 200, (600 + 525) / 2, 275, width=2) # line that is divided window
    draw_line(canvas, (600 + 525) / 2, (200 + 275) / 2, 600, (200 + 275) / 2, width=2) # line that is divided window
    draw_rectangle(canvas, 625, 100, 680, 200, width=0, fill="darkSlateGrey") # door in the house
    draw_oval(canvas, 635, 150, 645, 160, width=0, fill="white") # door knob

 

# Call the main function so that
# this program will start executing.
main()