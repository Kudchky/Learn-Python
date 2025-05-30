obstacle_position = []

obstacle_definition = """\
    ##      ###   ##  
##  ##      ###   ##
            
             ##
 ##          ##     
###  ###  ###    ###
     
      ###
      #          ###
##    # ## ###   ###
        ###     
        ### ##   ###
###              ###
##  ###      ###    
             ###    \
"""

obstacle_definition = [list(el.ljust(20)) for el in obstacle_definition.split("\n")]

#Funtions----
def add_obstacle_position(list_obstacle_position, list_obstacle_definition):
    for row in range(15):
        for column in range(20):
            if  list_obstacle_definition[row][column]== "#":
                list_obstacle_position.append([row,column])

    return list_obstacle_position
#Fin----

obstacle_position = add_obstacle_position(obstacle_position, obstacle_definition)

print(obstacle_position)