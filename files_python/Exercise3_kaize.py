# %% Exercise

from sys import argv  # Hide

from matplotlib import pyplot as plt

#Introduction to Subplot to plot on multiple axis

#Some data for X and Y Datasets 
X=[2,3,4,5,6]
Y=[-2,-3,-4,-5,-6]
#Allocating the column and rows for Figure 
##fig, ax = plt.subplots(nrows =  , ncols = , )
fig, ax = plt.subplots(nrows = 1, ncols = 2, figsize = (6,5),constrained_layout = True) #hide

#Building on the same plot 
## Let's start with assigning the plot to different graphs
ax[0].scatter(X,Y,color='b', marker='*' ) # Assign the plot to first graph
ax[1].plot(X,Y,color='b',marker='o') # Assign the plot to second graph

#Add x_labels, y_labels and Title to first plot
ax[0].set_xlabel('x-axis of graph 1') # Hide
ax[0].set_ylabel('y-axis of graph 1') # Hide
ax[0].title.set_text('title 1') # Hide
##.set_xlabel('x-axis of graph 1')
##.set_ylabel('y-axis of graph 1')
##.title.set_text('title 1')

#Add x_labels, y_labels and Title to second plot
ax[1].set_xlabel('x-axis of graph 2') # Hide
ax[1].set_ylabel('y-axis of graph 2') # Hide
ax[1].title.set_text('title 2') # Hide
##.set_xlabel('x-axis of graph 2')
##.set_ylabel('y-axis of graph 2')
##.title.set_text('title 2')
#Next we would need to showcase the plot generated.
plt.savefig(f'{argv[0]}.png', dpi=100) # Hide
plt.show() 

# %% Results

# %% Solution

#Some data for X and Y Datasets 
X=[2,3,4,5,6]
Y=[-2,-3,-4,-5,-6]
#Allocating the column and rows for Figure 
fig, ax = plt.subplots(nrows = 1, ncols = 2, figsize = (6,5),constrained_layout = True) 

#Building on the same plot 
## Let's start with assigning the plot to different graphs
ax[0].scatter(X,Y,color='b', marker='*' ) # Assign the plot to first graph
ax[1].plot(X,Y,color='b',marker='o') # Assign the plot to second graph

#Add x_labels, y_labels and Title to first plot
ax[0].set_xlabel('x-axis of graph 1') 
ax[0].set_ylabel('y-axis of graph 1') 
ax[0].title.set_text('title 1') 



#Add x_labels, y_labels and Title to second plot
ax[1].set_xlabel('x-axis of graph 2')
ax[1].set_ylabel('y-axis of graph 2') 
ax[1].title.set_text('title 2') 
plt.savefig(f'{argv[0]}.png', dpi=100) # Hide
plt.show() 


