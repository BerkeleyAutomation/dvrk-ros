from robot import *
import math



def dictionary(robotName):
    r=robot(robotName)
    dict = {}
    dict['test'] = [('u'),('d')]
    dict['test2'] = [('r',90,60),('r',180,60),('r',270,60),('r',0,60)]
    dict['a'] = [('r',80,60),('r',280,30),('r',180,10),('r',0,10),('r',280,30)]
    #dict['b'] = [('f',60),('r',100),('f',30),('r',80),('f',20),('r',80),('f',30),('r',200),('f',40),('r',80),('f',23),('r',90),('f',40)]
    #dict['c'] = [('u'),('r',90),('f',35),('r',180),('d'),('f',30),('r',71.57),('f',15.8114),('r',18.43),('f',30),('r',18.43),('f',15.8114),('r',71.57),('f',30)]
    #dict['d'] = [('f',60),('r',110),('f',30),('r',70),('f',40),('r',70),('f',30)]
    #dict['e'] = [('u'),('r',90),('f',40),('r',180),('d'),('f',40),('r',90),('f',30),('r',90),('f',30),('r',180),('f',30),('r',90),('f',30),('r',90),('f',40)]
    #dict['f'] = [('f',30),('r',90),('f',30),('r',180),('f',30),('r',90),('f',30),('r',90),('f',40)]
    #dict['g'] = [('u'),('r',90),('f',40),('r',270),('f',35),('r',270),('f',12),('r',180),('d'),('f',12),('r',90),('f',35),('r',90),('f',40),('r',90),('f',60),('r',90),('f',40)]
    #dict['h'] = [('f',60),('r',180),('f',30),('r',270),('f',40),('r',270),('f',30),('r',180),('f',60)]
    #dict['i'] = [('r',90),('f',40),('r',180),('f',20),('r',90),('f',60),('r',90),('f',20),('r',180),('f',40)]
    #dict['j'] = [('u'),('f',16),('d'),('r',143.14),('f',15),('r',306.87),('f',12),('r',306.87),('f',15),('r',323.14),('f',40),('r',90),('f',12),('r',180),('f',24)]
    #dict['k'] = [('f',60),('r',180),(]
 

    #print dict['a'][0][0]
    r.move_cartesian([0.0,0.0,-0.12])
    letter_number = 0

    while letter_number < 500:  

        cycle_number = 0  
        letter = raw_input('enter the letter you would like typed: ') 
        length_of_list = len(dict[letter])  

        while cycle_number < length_of_list: 
            if dict[letter][cycle_number][0] == 'r':                      # ('r',angle,distance)
                angle = math.radians(dict[letter][cycle_number][1])
                print 'a', angle
                length = (dict[letter][cycle_number][2])/1000.0
                print 'l', length

                x_position = math.cos(angle)*length
                y_position = math.sin(angle)*length

                r.delta_move_cartesian([x_position,y_position,0.0])

            elif dict[letter][cycle_number] == 'u':         #u = pen up
                r.delta_move_cartesian([0.0,0.0,-0.01])
            elif dict[letter][cycle_number] == 'd':         #d = pen down
                r.delta_move_cartesian([0.0,0.0,0.01])
            
            cycle_number += 1

        r.delta_move_cartesian([0.0,0.0,-0.01])
        r.move_cartesian([0.0,0.0,-0.12])
        r.delta_move_cartesian([0.0,0.0,0.01])
        r.close_gripper()
        letter_number +=50

if __name__ == '__main__':
    if (len(sys.argv) != 2):
        print sys.argv[0] + ' requires one argument, i.e. name of dVRK arm'
    else:
        dictionary(sys.argv[1])
