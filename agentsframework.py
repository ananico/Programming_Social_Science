# -*- coding: utf-8 -*-
"""
The following code was developed based on the material taught in 
GEOG5990M Programming for Spatial Analysts: Core Skills, by 
Dr Andy Evans, University of Leeds.

author:Ana Nicoriciu
"""
import random
import math
#create the Agent class which can then be imported similar to a library
"""
For both classes created in this file, the x and y variables are set as private, which is represented by the double underscore (__)
This implies the values cannot be changed outsied the class. However, if they were just protected, they could be changed, due to the 
@property functions set at the end of each class, which is currently set as a comment

"""
class Agent:
    
  #this class can take three argument besides its self 

    def __init__(self, environment, agents, neighbourhood):
        self.environment = environment
        self.__x=(random.randint(0,len(self.environment))) #make it start randomly, 
        #based on the length of the environment 
        self.__y=(random.randint(0,len(self.environment)))
        self.store = 0
        self.agents= agents
        self.neighbourhood=neighbourhood
        self.agentstore=0
   #allows "agents" to move around when called
    """
    diving by 300 creates a Torus effects which brings the points back if the value is above
    the value of the axis when being plottted
    """ 
    def move(self):
            if random.random() < 0.5:

                self.__y = (self.__y + int((self.store)* 0.01)) % 300
            else:
                self.__y = (self.__y - int((self.store)* 0.01)) % 300

            if random.random() < 0.5:
                self.__x = (self.__x + int((self.store)* 0.01)) % 300
            else:
                self.__x = (self.__x - int((self.store)* 0.01)) % 300
   #gives "agents" the posibility to "eat" the environment when called   
           
    def meat(self): 
            if  self.environment[self.__y][self.__x] > 10:
                self.environment[self.__y][self.__x] -= 10
                self.store += 10
            else:
                 self.environment[self.__y][self.__x] -= self.environment[self.__y][self.__x]
                 self.store += self.environment[self.__y][self.__x]
                 
    #when called the function allows "agents" to find how far they are from each other
    #after each move     
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            #agents do not compare to themselves
            if agent==self:
                continue
            dist_agent = self.distance_between(agent) 
            if dist_agent <= neighbourhood:
                sum = self.store + agent.store
                ave = sum /2
                self.store = ave
                agent.store = ave
                #print("sharing " + str(dist_agent) + " " + str(ave))
                #prints max for distance: if wanted remove #
                #print(max(dist_agent))
    #calculates the distance between two agents
    def distance_between(self, agent):
        return math.sqrt(((self.__x - agent.__x)**2) + ((self.__y - agent.__y)**2))

     
    @property 
    def x(self):
        return self.__x
    
    @property 
    def y(self):
        return self.__y
    
    #@x.setter
    #def x(self):
        #return self.__x
        
    #@y.setter
    #def y(self):
        #return self.__y    

#create a new class with similar properties to the agent class above                 
class Wolves:
    #specifies which argumens the class can have
    def __init__(self,agents, neigh_wolves):
        self.__x=(random.randint(0,300))
        self.__y=(random.randint(0,300))
        #creates the "wolves"
        self.store = 0
        self.agents=agents
        self.neigh_wolves=neigh_wolves
        
    #gives wolves the option to move around  
    def move_wolves(self):
                    if random.random() < 0.5:
                        self.__y = (self.__y + 1) % 300
                    else:
                        self.__y = (self.__y- 1) % 300
        
                    if random.random() < 0.5:
                        self.__x = (self.__x + 1) % 300
                    else:
                        self.__x = (self.__x - 1) % 300
    
    """
    The below function removes agents from the list accodring to an if condition, which in this case 
    refers to the distance between a wolf and an agent
    """
    #based on the if condition agents previously created are removed 
    #if the condition is fullfield
    def delete_agent (self):
        for agent in self.agents:
            dist_wolves = self.distance_between(agent) 
            #print(dist_wolves)
            if dist_wolves <= self.neigh_wolves :
               self.agents.remove(agent)
       
    def distance_between(self, agent):
        return math.sqrt(((self.__x - agent._Agent__x)**2) + ((self.__y - agent._Agent__y)**2))
   
    @property 
    def x(self):
        return self.__x
    
    @property 
    def y(self):
        return self.__y
    
   #@x.setter
    #def x(self, value):
         #self.__x=value
        
    #@y.setter
    #def y(self, value):
         #self.__y=value
