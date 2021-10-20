
from random import randint

from termcolor import colored

color=['yellow','green','red','cyan','blue','mangenda','white','grey']

print(
"""Choose your difficulty:
>Easy
>Medium
>Hard"""
)
difficulty=input()
gameOver=False

def GameIsNotOver():
  if gameOver==True:
    return False
  spaces=height*width-bombs
  for i in range(0,height):
    for j in range(0,width):
      if board[i][j]>=10:
        spaces-=1
  if spaces==0:
    return False
  return True
        
def ShowBoard():
  print('     ',end='')
  for i in range(0,width):
    print(str(i+1).center(3),end=' ')
  print('')
  print('    ╔',end='')
  for i in range(0,width-1):
    print('═══╦',end='')
  print('═══╗') 
  for i in range(0,height):
    print(str(i+1).rjust(3),end=' ')
    print('║',end='')
    for j in range(0,width):
      print(' ',end='')
      if board[i][j]==20 or board[i][j]==10:
        print(' ',end='')
      elif board[i][j]>10:
        print(colored(board[i][j]-10,color[board[i][j]-11]),end='')
      else:
        print('x',end='')
      print(' ║',end='')
    print('')
    if(i<height-1):
      print('    ╠',end='')
      for i in range(0,width-1):
        print('═══╬',end='')
      print('═══╣')
  print('    ╚',end='')
  for i in range(0,width-1):
    print('═══╩',end='')
  print('═══╝')

def discover(x,y):
  if board[x][y]==-1:
    gameOver=True
  else:
    if board[x][y]<10:
      board[x][y]+=10
    if board[x][y]==10:
      board[x][y]=20
      if(x>0):
        discover(x-1,y)
      if(x<height-1):
        discover(x+1,y)
      if(y>0):
        discover(x,y-1)
      if(y<width-1):
        discover(x,y+1)
      if(x>0 and y>0):
        discover(x-1,y-1)
      if(x<height-1 and y>0):
        discover(x+1,y-1)
      if(x>0 and y<width-1):
        discover(x-1,y+1)
      if(x<height-1 and y<width-1):
        discover(x+1,y+1)



board=list()
#0-8 bombs around(undiscovered),-1 bomb,10-18 bomb around(discovered),20 no bombs
height=0
width=0
bombs=0

if(difficulty=="Easy"):
  height=9
  width=9
  bombs=10
if(difficulty=="Medium"):
  height=16
  width=16
  bombs=40
if(difficulty=="Hard"):
  height=30
  width=16
  bombs=99
for x in range(0,height):
  line=list()
  for y in range(0,width):
    line.append(0)
  board.append(line)

print("Where do you want to start?")
StartX=int(input())-1
StartY=int(input())-1

for k in range(0,bombs):
  x=randint(0,height-1)
  y=randint(0,width-1)
  while((x==StartX and y==StartY) or board[x][y]==-1):
    x=randint(0,height-1)
    y=randint(0,width-1)
  board[x][y]=-1
  if(x!=0 and y!=0):
    if(board[x-1][y-1]>=0):
      board[x-1][y-1]+=1
  if(x!=0):
    if(board[x-1][y]>=0):
      board[x-1][y]+=1
  if(y!=0):
    if(board[x][y-1]>=0):
      board[x][y-1]+=1
  if(x!=height-1 and y!=width-1):
    if(board[x+1][y+1]>=0):
      board[x+1][y+1]+=1
  if(x!=height-1):
    if(board[x+1][y]>=0):
      board[x+1][y]+=1
  if(y!=width-1):
    if(board[x][y+1]>=0):
      board[x][y+1]+=1
  if(x!=height-1 and y!=0):
    if(board[x+1][y-1]>=0):
      board[x+1][y-1]+=1
  if(x!=0 and y!=width-1):
    if(board[x-1][y+1]>=0):
      board[x-1][y+1]+=1

discover(StartX,StartY)
print('\n'*100)
ShowBoard()
while GameIsNotOver():
  print("Where do you want to search?")
  PosX=int(input())-1
  PosY=int(input())-1
  discover(PosX,PosY)
  print('\n'*100)
  ShowBoard()
  

print('\n'*100)
if gameOver:
  print("You lost!")
else:
  print("You won!")
