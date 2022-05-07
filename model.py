"""Agent-Based Model (ABM), where objects/agents can be given individual behaviour and allowed to interact with
each other and their environment. This Model python code sets up the initial model, runs the model iterations and
allows user interaction""" 
import random #imports the random module that generates pseudo-random varaibles within a set range
import operator # imports operator module that allows matermatical operations 
import csv #imports 
import tkinter
import matplotlib
matplotlib.use('TkAgg') 
import matplotlib.pyplot
import matplotlib.animation #imports module that allows data to be plotted into graphs
import agentframework #imports the agentframwork python file 
import requests
import bs4
import os
from sys import argv
import matplotlib.animation
#import time
#start=time.process_time()
# Import modules.
#import sys

'''Step 1: Initialises the starting parameters'''
print("Step 1: Intitialise parameters")
agents=[]
num_of_agents = 50
num_of_iterations = 100
neighbourhood = 20
random_number = 0
agent_store = 90

'''print("Step 1: Initialise parameters")
print("argv", argv)
if len(argv) < 5:
    num_of_agents = 10
    num_of_iterations = 100
    neighbourhood = 20
    random_number = 0
    print("argv does not contain the expected number of arguments")
    print("len(argv)", len(argv))
    print("expected len(argv) 5")
    print("expecting:")
    print("argv[1] as a integer number for num_of_agents")
    print("argv[1] as a integer number for num_of_iterations")
    print("argv[1] as a integer number for neighbourhood")
    print("argv[1] as a integer number for random_number for setting the random seed")
else:
    # set parameters from argv
    num_of_agents = int(argv[1])
    num_of_iterations = int(argv[2])
    neighbourhood = int(argv[3])
    random_number = int(argv[4])
print("num_of_agents", str(num_of_agents))
print("num_of_iterations", str(num_of_iterations))
print("neighbourhood", str(neighbourhood))
print("random_number", str(random_number))
random.seed(random_number)'''


'''Step 2: Get Data from the html link - x,y,z array'''

print("Step 2: Get data from the html link.")
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_xs = soup.find_all(attrs={"class" : "x"})
td_ys = soup.find_all(attrs={"class" : "y"})
#td_zs = soup.find_all(attrs={"class" : "z"}) --- z values are not required for this project
# print(td_ys)
# print(td_xs) 

'''Step 3: Initialises environment, which reads in csv environment data from a text document'''

print("Step 3: Read in Environment Data")
def read_raster(file):
    """
    Desribe what the function does.
    Parameters
    ----------
    file : text
        The path to a file.
    Returns
    -------
    environment : list of lists
        Raster read in.
    """
    f = open(file) #This set of code creates a list of lists. So an empty environment is created and then each row in 
    #the text file an empty list of rows is created. Then each value in a row is appended to the rowlist and then after
    #all the rows are appended in the empty environment list.
    dataset = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    environment = []
    for row in dataset:
        rowlist = []
        for value in row:
            rowlist.append(value)
            #print(value) # Test the value by printing it]
        environment.append(rowlist)
    f.close()
    #print(environment)
    return environment

environment = read_raster('int.txt')
        
'''def distance_between(agents_row_a, agents_row_b): #This function takes in two rows in our agents list and the initialisation of our agents are ran in the agentframwork module
    return (((agents_row_a.x - agents_row_b.x)**2) +
    ((agents_row_a.y - agents_row_b.y)**2))**0.5'''
    

'''Step 4: Initialise the Agents'''
print("Step 4: Initialise agents.")
agents = []
# Make the agents.
for i in range(num_of_agents):
    j = i
    while (i > len(td_ys)): # ensure we don't fall off the end of the array
        j -= len(td_ys)
    y = int(td_ys[i].text)*3
    x = int(td_xs[i].text)*3
    # Add 1 to random seed to get each agent initialised and moving differently
    random_number += 1000
    agents.append(agentframework.Agent(environment, agents, random_number, y, x))

'''Step 5: Initialise the GUI. Defining the variables allows for the final exiting function to run, appending the results upon exiting'''
print("Step 5: Initialising GUI.")
carry_on = True
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])
carry_on = True
init = True
halted = False
rerunid = 0
total_ite = 0;
        
print("Select Run Model from the GUI pop-up window")

'''Step 6 Animation'''

print("Step 6: Animating the agents")
def update(frame_number):
    global carry_on
    global init
    global halted
    global rerunid
    if (init == True):
        print("Start .", end='')
        init = False
    else:
        if (halted):
            rerunid += 1
            print("Continuing", rerunid, end='')
            halted = False
        else:
            print(" .", end='') #Not actually needed as we're not assigning, but clearer
    
    # Clear fig
    fig.clear()

    # The number of iterations once in the for J loop is now controlled in the gen_function
    if (carry_on):
        random.shuffle(agents)
        for i in range(num_of_agents):
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)
        half_full_agent_count = 0
        for i in range(num_of_agents):
            if (agents[i].store > agent_store):
                half_full_agent_count += 1
        if (half_full_agent_count == num_of_agents):
            carry_on = False
            print(" all agent stores are greater than", agent_store, "run ended after ", end='')
    # Plot            
    # Plot environment
    matplotlib.pyplot.xlim(0, len(environment))
    matplotlib.pyplot.ylim(0, len(environment[0]))
    matplotlib.pyplot.imshow(environment)
    
    for i in range(num_of_agents):
        matplotlib.pyplot.title("Agent-Based Modelling")
        matplotlib.pyplot.xlabel("X-Axis")
        matplotlib.pyplot.ylabel("Y-Axis")
        matplotlib.pyplot.scatter(agents[i].getx(),agents[i].gety(), color="red")
       
        
        

def gen_function(b = [0]):
    a = 0
    global carry_on
    global halted
    global total_ite
    while  (a < num_of_iterations) & (carry_on): 
        yield a			
        a = a + 1
        total_ite += 1
    halted = True
    if (a == num_of_iterations):
        print(" run stopped after", total_ite, "iterations.")
    else:
        print(total_ite, "iterations.")
        exiting()

def runanimation():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw()

root = tkinter.Tk()
root.wm_title("Agent-Based Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=runanimation)

'''Step 8: When the model is exited/GUI is killed, the files are outputted to the csv and text files'''
print("Step 8: Write out the environment data to data.csv and the total amount stored to the data.txt)
def exiting():
  
    if halted == False:
        print(" run stopped after", total_ite, "iterations.")

    file = os.path.join('data.csv')
    with open(file, 'w', newline='') as f2:
        writer = csv.writer(f2, delimiter=' ')
        for row in environment:
            writer.writerow(row)
    
    total = 0
    for a in agents:
        total += a.store
        #print(total)
    file = os.path.join('data.txt')
    with open(file, "a") as f3:
        f3.write(str(total) + "\n")
        
        f3.flush  
    f3.close
    print("Step 10: End Program.")
    root.quit()
    root.destroy()


root.protocol('WM_DELETE_WINDOW', exiting) 

tkinter.mainloop() 

print("The model has now ended, the outputs have been appended to the data text and csv files.")


 