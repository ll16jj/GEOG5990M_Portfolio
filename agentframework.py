# In this python module the agent class is defined with an _init_ method 
import random 

""" Agent code, where an agent is made up of x and y values, and those agents are able to communicate and interact
with each other."""
class Agent():

    #def __init__(self, environment):
    def __init__(self, environment, agents, random_number, x, y):
        self.environment = environment
        self.store = 0
        self.agents = agents
        # Find out the size of environment inside the agents
        self.width = len(environment);
        self.height = len(environment[0])
        
        if (random_number == None):
            random.seed(0) # defaul random seed to 0
        else:
            random.seed(random_number)
        if (x == None):
            self._x = random.randint(0,self.width)
        else:
            self._x = x
        if (y == None):
            self._y = random.randint(0,self.height)
        else:
            self._y = y
        random.randint(0,self.width)
        #print("x", self._x)
        #print("y", self._y)
        
        
        
        '''self._x = random.randint(0,self.width)
        self._y = random.randint(0,self.height)
        #self._x = random.randint(0,99)
        #self._y = random.randint(0,99)'''
#creates get and set methods, where the property decorater turns the x and y into a "getter" for a read only 
#attribute and set the docstring to state this is the x or y values. the setter method stores the new value in another attribute
 
    @property
    def x(self):
        """I'm the x value"""
        return self._x
        
    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value
        
    def delx(self):
        del self._x
    
    @property
    def y(self):
        """I'm the y value"""
        return self._y

    def gety(self):
        return self._y

    def sety(self, value):
        self._y = value        
        
    def dely(self):
        del self._y
   
# This creates an eat method 
    def eat(self):
        # If more than 10 get 10
        '''if self.environment[self._y][self._x] > 10:
            self.environment[self._y][self._x] -= 10
            self.store += 10
        else:
            # Store what is left
            self.store += self.environment[self._y][self._x]
            self.environment[self._y][self._x] = 0
        #print(str(self.store))
        if self.store > 100:
            self.environment[self._y][self._x] = self.environment[self._y][self._x] + 100
            #print(str(self))
            self.store = 0'''
        if self.environment[self._y][self._x] > 10:
            self.environment[self._y][self._x] -= 10
            self.store += 10
        else:
            # Store what is left
            self.store += self.environment[self._y][self._x]
            self.environment[self._y][self._x] = 0
        #print(str(self.store))
        if self.store > 100:
            self.environment[self._y][self._x] = self.environment[self._y][self._x] + 50
            #print(str(self))
            self.store = 50
            #print(str(self))
            #self.__str__.__call__
            #print("Location x =", self._x, "y =", self._y, "store =", str(self.store))
            
            
# When called ,this function changes the x and y coorindates randomly Move the agents.
     
        #if random.random() < 0.5:
            #self._x = (self._x + 1) % 100
        #else:
            #self._x = (self._x - 1) % 100
        #if random.random() < 0.5:
            #self._y = (self._y + 1) % 100
        #else:
            #self._y = (self._y - 1) % 100
        
    def move(self):
        if random.random() < 0.5:
            self._y = (self._y + 1) % self.width
        else:
            self._y = (self._y - 1) % self.width

        if random.random() < 0.5:
            self._x = (self._x + 1) % self.height
        else:
            self._x = (self._x - 1) % self.height
            
            
            
    def share_with_neighbours(self, neighbourhood):
        """
        Agent shares some of store with neighbours.
        
        Postional arguments:
        neighbourhood -- the distance within which agents share an instance of this Agent class
        """
        #print(neighbourhood)
        for agent in self.agents:
            # Don't share with self for speed (not that it matters much)
                dist = self.distance_between(agent) 
                if dist <= neighbourhood:
                    sum = self.store + agent.store
                    ave = sum /2
                    self.store = ave
                    agent.store = ave
                    #print("sharing " + str(dist) + " " + str(ave))
 
    def distance_between(self, agent):
        """
        Calculate and return the distance between self and agent.
        
        Postional arguments:
        agent -- an instance of this Agent class
        
        Returns: Number
        The distance between self and agent.
        """
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5 
            
            
            
            
    def hi(self):
        print("Hello world I am at x =", self._x, "y =", self._y)
        
    def __str__(self):
        return "Location x = " + str(self._x) + ", y = " + str(self._y) + ", store = " + str(self.store)
            
            