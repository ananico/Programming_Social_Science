# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 14:16:08 2018

@author: n21731an
"""

##First practical Leeds 
#import math
import random 
import matplotlib.pyplot
import agentsframework
import csv
import matplotlib.animation

"""if you would want to run the file from a command line, the below lines would allow
 the user to just write the file's name and the wnted value for each parameter
 i.e file_name.py 10 100 20 10 5 (random values for each parameter)"""
#import sys
#num_of_agents =int(sys.argv[1])
#num_of_iterations =int(sys.argv[2])
#neighbourhood = int(sys.argv[3])
#num_of_wolves=int(sys.argv[4])
#neigh_wolves=int(sys.argv[5])

#set the initial values 
agents = [] 
wolves=[]
num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20
num_of_wolves=10
neigh_wolves=5

#read in the data from a text file
dataset=open("in.txt", newline='')
environment=[]
reader=csv.reader(dataset, quoting=csv.QUOTE_NONNUMERIC)

for row in reader:
    rowlist=[]
    for value in row:
        rowlist.append(value)
    environment.append(rowlist)
dataset.close()  
      
  
"""to the empty lists declared above add agents and wolves 
based on the Agent & Wolves classes on the agentsframework file 
"""
for i in range(num_of_agents):
    agents.append(agentsframework.Agent(environment,agents, neighbourhood))  
for j in range(num_of_wolves):
    wolves.append(agentsframework.Wolves(agents, neigh_wolves))

#set the values for figure size&axes 
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

carry_on = True

#define a function which is then used as an input in the animation command
def update(frame_number):
    
    fig.clear()  
    global carry_on
     
    #creates a condition to make the animation  stop
    #in this case, when all the sheeps are eaten the animation stops
    if len(agents)==0:
        carry_on=False
        print("Stopping condition ")
    
    #makes agents move, eat and calculate the distance between 
    #themselves based on the functions defined in the Agent class
    for j in range(num_of_iterations):
        random.shuffle(agents)#shuffles the agents 
        for i in range(len(agents)):
            agents[i].move()
            agents[i].meat()
            agents[i].share_with_neighbours (neighbourhood)
            print(agents[i].store)
   
    #plots the agents as they move and represented by white dots 
    for i in range(len(agents)):
        matplotlib.pyplot.scatter(agents[i].y,agents[i].x, color= 'white')   
   
    #makes wolves move and delete agents from the list
    #based on the functions defined in the Wolves class
    for j in range(num_of_iterations):
        random.shuffle(wolves)#shuffles wolves
        for m in range(len(wolves)):
           wolves[m].move_wolves()
           wolves[m].delete_agent()
    #plots the wolves as they move and represented by black dots 
    for j in range(len(wolves)):
        matplotlib.pyplot.scatter(wolves[j].y,wolves[j].x, color= 'black')    
  
    #makes the agents stop once they have eaten over 800 
    #if all ((wolf.store)>8000 for wolf in wolves):
     #   carry_on=False
      #  print("stopping condition")
    ##first stopping condition
    #for agent in agents:        
     #   if agent.store > 8000: 
      #       carry_on=False
       #      print("stopping condition")

    #matplotlib.pyplot.scatter(agents[2].y,agents[2].x, color= 'black')
        #print(agents[i].y,agents[i].x)
    
    #sets boundries for the x & y axes
    matplotlib.pyplot.xlim(0, 99)
    matplotlib.pyplot.ylim(0, 99)    
    matplotlib.pyplot.imshow(environment)


def gen_function(b = [0]):
    a = 0
    #global carry_on #Not actually needed as we're not assigning, but clearer
    while (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1
        #print(carry_on)
        #print(a)

animation = matplotlib.animation.FuncAnimation(fig, update, interval=1000, frames= gen_function(), repeat=False)
matplotlib.pyplot.show()     



"""#Practical 1
#creates a radom integer to start
#between 0 and 99
y0=random.randint(0,99)
x0=random.randint(0,99)

random_number=random.random()
if random_number<0.5:
    y0+=1
   
else:
    y0-=1
   

print(y0)

if random_number<0.5:
    
    x0+=1
else:
    
    x0-=1
print(x0)


x1=random.randint(0,99)
y1=random.randint(0,99)
random_number=random.random()
if random_number<0.5:
    y1+=1 
else:
    y1-=1
print(y1)

if random_number<0.5:   
    x1+=1
else:   
    x1-=1
print(x1)

answer=math.sqrt((y0-y1)**2+(x0-x1)**2)

####Practical2 
agents=[]
#creates a radom integer to start
#between 0 and 99
##add agents to the list
agents.append([random.randint(0,99),random.randint(0,99)])

random_number=random.random()
if random_number<0.5:
    agents[0][0]+=1
   
else:
   agents[0][0]-=1
   

if random_number<0.5:
    
    agents[0][1]+=1
else:
    
   agents[0][1]-=1


random_number=random.random()
if random_number<0.5:
    agents[0][0]+=1 
else:
    agents[0][0]-=1


if random_number<0.5:   
    agents[0][1]+=1
else:   
    agents[0][1]-=1

print(agents)
#answer=math.sqrt((agents[0][0]-agents[1][0])**2+(agents[0][1]-agents[1][1])**2)

# find which agents is furthest east(largex)
print(max(agents))
a=max(agents, key=operator.itemgetter(1))

#plot the current agents
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
matplotlib.pyplot.scatter(agents[1][1],agents[1][0])
matplotlib.pyplot.scatter(a[1], a[0], color='red')
matplotlib.pyplot.show()



##Practical Code shrinking 2

#creates a radom integer to start
#between 0 and 99
##add agents to the list
##create function to compute distance
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a[0] - agents_row_b[0])**2) + 
            ((agents_row_a[1] - agents_row_b[1])**2))**0.5     
num_of_agents=10
num_of_iterations=100
agents=[]
#agents.append([random.randint(0,100),random.randint(0,100)])
for i in range(num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])

# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):

        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] - 1) % 100

        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else:
            agents[i][1] = (agents[i][1] - 1) % 10
            


#plot the current agents
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
matplotlib.pyplot.show()

for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)
        print(distance)
        
        
##final part using a class

#read in the data
dataset=open("in.txt", newline='')
#rowlist=[]
environment=[]
reader=csv.reader(dataset, quoting=csv.QUOTE_NONNUMERIC)

for row in reader:
    rowlist=[]
    for value in row:
        rowlist.append(value)
    environment.append(rowlist)
dataset.close()  
    
    
#starting values   

#model.py
num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20
agents = []   
#adds the agents
for i in range(num_of_agents):
    agents.append(agentsframework.Agent(environment,agents, neighbourhood))    

#agents=random.shuffle(agents)
#moves the agents  
#for j in range(num_of_iterations):
 #   random.shuffle(agents)
  #  for i in range(num_of_agents):
   #     agents[i].move()
    #    agents[i].meat()
     #   agents[i].share_with_neighbours (neighbourhood)
#matplotlib.pyplot.xlim(0, 99)
#matplotlib.pyplot.ylim(0, 99)
#matplotlib.pyplot.imshow(environment)
#for i in range(num_of_agents):
#    matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
#matplotlib.pyplot.show()

#for agents_row_a in agents:
 #   for agents_row_b in agents:
  #      distance = distance_between(agents_row_a, agents_row_b)
        #print(distance)
        
   """    