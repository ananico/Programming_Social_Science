# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 18:23:16 2018

@author: n21731an
"""
#Practical 1
import random 
import math
import matplotlib.pyplot
import matplotlib.animation
import operator


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

#makes the agent furthest east red
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
        
        

 
