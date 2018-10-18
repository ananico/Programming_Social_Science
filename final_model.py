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




"""if you want to run the file from a command line, the below lines would allow
 the user to just write the file's name and the wnted value for each parameter
 i.e file_name.py 10 100 20 10 5 (random values for each parameter)"""
    #import sys
    #num_of_agents =int(sys.argv[1])
    #num_of_iterations =int(sys.argv[2])
    #neighbourhood = int(sys.argv[3])
    #num_of_wolves=int(sys.argv[4])
    #neigh_wolves=int(sys.argv[5])
    
"""
When you start the program, the program could be set up to ask the user to 
input values for each argument, whihc are them to be used by the program to run. 
This can be achieved by using the following lines (# needs to be removed)   
"""
    #num_of_agents =int(input("Set the numbers of sheeps to be in the environment"))
    #num_of_iterations =int(input("Set how many time you want the 'animals to move'"))
    #num_of_wolves=int(input("Set the number of wolves"))

    
#empty lists for adding sets of coordinates to
agents = [] 
wolves=[]
#set the initial values 
num_of_agents = 50
num_of_iterations = 100
neighbourhood = 20
num_of_wolves=40
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
     
    """creates a condition to make the animation  stop
    in this case, when all the sheeps are eaten the animation stops"""
    if len(agents)==0:
        carry_on=False
        print("Stopping condition ")
    
    """makes agents move, eat and calculate the distance between 
    themselves based on the functions defined in the Agent class"""
    for j in range(num_of_iterations):
        random.shuffle(agents)#shuffles the agents 
        for i in range(len(agents)):
            agents[i].move()
            agents[i].meat()
            agents[i].share_with_neighbours (neighbourhood)
            #print(agents[i].store)
   
    #plots the agents as they move and represented by white dots 
    for i in range(len(agents)):
        matplotlib.pyplot.scatter(agents[i]._Agent__y,agents[i]._Agent__x, color= 'white')   
   
    """makes wolves move and delete agents from the list
    based on the functions defined in the Wolves class"""
    for j in range(num_of_iterations):
        random.shuffle(wolves)#shuffles wolves
        for m in range(len(wolves)):
           wolves[m].move_wolves()
           wolves[m].delete_agent()
    #plots the wolves as they move and represented by black dots 
    for j in range(len(wolves)):
        matplotlib.pyplot.scatter(wolves[j]._Wolves__y,wolves[j]._Wolves__x, color= 'black')    
  
    #makes the agents stop once they have eaten over 800 
    #if all ((agent.store)>8000 for agent in agents):
     #   carry_on=False
      #  print("stopping condition")
       
    
    #sets boundries for the x & y axes
    matplotlib.pyplot.xlim(0, 300)
    matplotlib.pyplot.ylim(0, 300)    
    matplotlib.pyplot.imshow(environment)


def gen_function(b = [0]):
    a = 0
    while (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1
        #print(carry_on)
        #print(a)

animation = matplotlib.animation.FuncAnimation(fig, update, interval=1000, frames= gen_function(), repeat=False)
matplotlib.pyplot.show()     



