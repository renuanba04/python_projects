def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_around():
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear() and front_is_clear():
        if is_facing_north():
            move()
        else:
            build_wall()
            turn_around()
            move()
    elif wall_on_right() and front_is_clear():
        move()
    elif right_is_clear():
        turn_right()
        move()
    else:
        turn_left()