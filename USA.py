import arcade

import random

def main():
    data_file = open('USA_data.txt', 'r')
    our_colors = [arcade.color.AIR_FORCE_BLUE, arcade.color.WHITE, arcade.color.ALABAMA_CRIMSON, arcade.color.ALICE_BLUE,
                  arcade.color.AUBURN, arcade.color.BABY_BLUE, arcade.color.BABY_POWDER,arcade.color.BARN_RED,
                  arcade.color.FLORAL_WHITE,arcade.color.CAROLINA_BLUE]
    #colors for bar

    arcade.open_window(650, 650, "Population of USA")
    arcade.set_background_color(arcade.color.BLACK)
    #USA window opens

    all_lines = data_file.readlines()
    title1 = all_lines[0]
    x_axis_title1 = all_lines[1]
    y_axis_title1 = all_lines[2]
    arcade.start_render()
    #positons of titles

    arcade.draw_text(title1,160,520,arcade.color.WHITE,25)
    arcade.draw_text(x_axis_title1, 160, 90, arcade.color.WHITE, 25)
    arcade.draw_text(y_axis_title1, 50, 250, arcade.color.WHITE, 25, rotation=90)
    #titles of x and y axis

    graph_info = all_lines[3:]
    center_y1 = 160

    for line in graph_info:
        chart_label1, chart_num1, = line.split(":")
        color1 = arcade.color.WHITE
        center_x = 70
        center_y1+= 30
        arcade.draw_text(chart_label1,center_x,center_y1,color1)
    #location of age groups


    rest_of_the_lines = all_lines[3:]
    x_loc = 350
    y_loc = 150
    #location of bars

    for line in rest_of_the_lines:
        rec_data,rec_data2 = line.split(":")
        size = int(rec_data2)
        y_loc = int(y_loc+29)
        this_color = random.choice(our_colors)
        rectangle = arcade.create_rectangle_filled(x_loc, y_loc, size, 29, this_color)
        rectangle.draw()
        print(rec_data2)
    #sctual bar graphs

    arcade.finish_render()
    arcade.run()

main()