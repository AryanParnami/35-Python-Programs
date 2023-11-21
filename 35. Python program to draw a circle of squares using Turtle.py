import turtle

def draw_square(side_length):
    for _ in range(4):
        turtle.forward(side_length)
        turtle.right(90)

def draw_circle_of_squares(num_squares, side_length):
    for _ in range(num_squares):
        draw_square(side_length)
        turtle.forward(side_length)
        turtle.right(360 / num_squares)

# Example usage
num_squares_input = int(input("Enter the number of squares in the circle: "))
side_length_input = int(input("Enter the side length of each square: "))

draw_circle_of_squares(num_squares_input, side_length_input)
turtle.done()