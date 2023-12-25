width,height = input().split()
num_of_boxes = input().split()
arrangement = {}
for i in range(int(width)):
    arrangement[i]=int(num_of_boxes[i])
crane_pos = 0
crane_Box = False  
flag = True
''' 
Command Values:
1 : Move left
2 : Move right
3 : Pick up box
4 : Drop box
0 : Quit
'''
while flag:
    x = input().split()
    int_list = [eval(p) for p in x]
    for command in int_list:
        if command == 0:
            flag = False
        elif command ==1 and crane_pos>0:
            crane_pos-=1
            #print("Moved left to:",crane_pos)
        elif command==2 and crane_pos<=(int(width) -2):
            crane_pos+=1
            #print("Moved right to:",crane_pos)
        elif command==3 and crane_Box==False and arrangement[crane_pos]>=0:
            arrangement[crane_pos]-=1
            crane_Box=True
            #print("picked up box at:", crane_pos)
        elif command==4 and crane_Box==True and arrangement[crane_pos]<int(height):
            arrangement[crane_pos]+=1
            crane_Box=False
            #print("Dropped box at:", crane_pos)
print(' '.join(str(value) for value in arrangement.values()))