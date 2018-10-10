# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 11:07:05 2018

@author: bn13amn
"""
import random

class Agent:
    
    def __init__(self, environment, agents, neighbourhood):
        
        self.x=(random.randint(0,99))
        self.y=(random.randint(0,99))
        self.environment = environment
        self.store = 0
        self.agents= agents
        self.neighbourhood=neighbourhood
        self.agentstore=0
       # self.wolves=wolves
        #self.wolves.x=(random.randint(0,99))
        #self.wolves.y=(random.randint(0,99))
    def move(self):
            if random.random() < 0.5:
                self.y = (self.y + int((self.store)* 0.01)) % 100
            else:
                self.y = (self.y - int((self.store)* 0.01)) % 100

            if random.random() < 0.5:
                self.x = (self.x + int((self.store)* 0.01)) % 100
            else:
                self.x = (self.x - int((self.store)* 0.01)) % 100
                
    def meat(self): # can you make it eat what is left?
            if  self.environment[self.y][self.x] > 10:
                self.environment[self.y][self.x] -= 10
                self.store += 10
      
    #def distance_between(agents_row_a, agents_row_b):
     #       distance_between=(((agents_row_a.x - agents_row_b.x)**2) + ((agents_row_a.y - agents_row_b.y)**2))**0.5
      #  return distance=distance_between(self.agents[], self.agents[])
               
        
                #def distance_between(agents_row_a, agents_row_b):
#    distance_between = (((agents_row_a[0] - agents_row_b[0])**2) + ((agents_row_a[1] - agents_row_a[1])**2))**0.5
    #distance = distance_between(agents_row_a[0], agents_row_b[0])
    #print(distance) 
#    return distance_between
 
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

    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5


   
                
                
                
                
class Wolves:
    
    def __init__(self, agents):
        self.x=(random.randint(0,99))
        self.y=(random.randint(0,99))
        
        #self.store = 0
        #self.agent=agent
        #self.neigh_wolves=neigh_wolves
        #self.agents=agents
        #self.agents= agents
        #self.vecini=vecini
        #self.agentstore=0
        
    def move_wolves(self):
                    if random.random() < 0.5:
                        self.y = (self.y + 1) % 100
                    else:
                        self.y = (self.y - 1) % 100
        
                    if random.random() < 0.5:
                        self.x = (self.x + 1) % 100
                    else:
                        self.x = (self.x - 1) % 100
    
   
    
    def delete_agent (self, agents):
        for agent in agents:
            dist = self.distance_between(agent) 
            #print(dist)
            if dist <= 10 :
               agents.remove(agent)
        
    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5

    

""" 
def share_with_neighbours (self, neighbourhood):
        result = None
        for i in range (len(self.agents)):
            for j in range(len(self.agents)):
                if i ==j:
                    continue 
                distance=distance_between(self.agents[i], 
                                          self.agents[j])
                if result == None:
                    result=distance 
                elif distance < result:
                    result= distance
        return result 
   """       