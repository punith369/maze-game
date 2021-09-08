def turn_right():
    turn_left()
    turn_left()
    turn_left()
   
    
def move_up():
    turn_left()
    move()
    
def turn_back():
    turn_left()
    turn_left()

    
def turn_down():
    turn_left()
    turn_left()
    move()
  
while at_goal() != True:
    if right_is_clear():
        turn_right()
    if front_is_clear():
        move()
    elif wall_in_front() : 
        turn_back()
    elif wall_in_front() and right_is_clear():
        turn_right()
    elif wall_in_front() and wall_on_right():
        turn_left()
    elif wall_on_right():
        turn_down()
    else:
        move()
        
   
        

 


    
    
    




