import time
move_step = int(0)
while True:
    line_move = ['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X']
    line_move[move_step] = '>'
    time.sleep(0.1)
    line_connect = ''.join(line_move)
    print(line_connect, end='\r')
    move_step += 1
    if move_step == len(line_move):
        move_step = 0