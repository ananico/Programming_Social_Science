# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 11:07:05 2018

@author: bn13amn
"""
import random
import math
#create the Agent class which can then be imported similar to a library
class Agent:
  #this class can take three argument besides its self   
    def __init__(self, environment, agents, neighbourhood):
        
        self.x=(random.randint(0,99))
        self.y=(random.randint(0,99))
        self.environment = environment
        self.store = 0
        self.agents= agents
        self.neighbourhood=neighbourhood
        self.agentstore=0
   #allows "agents" to move around when called
    def move(self):
            if random.random() < 0.5:
                self.y = (self.y + int((self.store)* 0.01)) % 100
            else:
                self.y = (self.y - int((self.store)* 0.01)) % 100

            if random.random() < 0.5:
                self.x = (self.x + int((self.store)* 0.01)) % 100
            else:
                self.x = (self.x - int((self.store)* 0.01)) % 100
   #gives "agents" the posibility to "eat" the environment when called   
           
    def meat(self): # can you make it eat what is left?
            if  self.environment[self.y][self.x] > 10:
                self.environment[self.y][self.x] -= 10
                self.store += 10
            else:
                 self.environment[self.y][self.x] -= self.environment[self.y][self.x]
                 self.store += self.environment[self.y][self.x]
                 
    #when called the function allows "agents" to find how far they are from each other
    #after each move     
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            if agent==self:
                continue
            dist = self.distance_between(agent) 
            if dist <= neighbourhood:
                sum = self.store + agent.store
                ave = sum /2
                self.store = ave
                agent.store = ave
                #print("sharing " + str(dist) + " " + str(ave))
                
    #calculates the distance between two agents
    def distance_between(self, agent):
        return math.sqrt(((self.x - agent.x)**2) + ((self.y - agent.y)**2))


   
#create a new class with similar properties to the agent class above                 
class Wolves:
    #specifies which argument the class can have
    def __init__(self,agents, neigh_wolves):
        self.x=(random.randint(0,99))
        self.y=(random.randint(0,99))
        #creates the "wolves"
        self.store = 0
        self.agents=agents
        self.neigh_wolves=neigh_wolves
        
    #gives wolves the option to move around  
    def move_wolves(self):
                    if random.random() < 0.5:
                        self.y = (self.y + 1) % 100
                    else:
                        self.y = (self.y - 1) % 100
        
                    if random.random() < 0.5:
                        self.x = (self.x + 1) % 100
                    else:
                        self.x = (self.x - 1) % 100
    
   
    #based on the if condition agents previously created are removed 
    #if the condition is fullfield
    def delete_agent (self):
        for agent in self.agents:
            dist = self.distance_between(agent) 
            #print(dist)
            if dist <= self.neigh_wolves :
               self.agents.remove(agent)
       
    def distance_between(self, agent):
        return math.sqrt(((self.x - agent.x)**2) + ((self.y - agent.y)**2))

    

      