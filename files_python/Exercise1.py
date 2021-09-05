# %% Exercise

from sys import argv  # Hide

from matplotlib import pyplot as plt


#Some data for X and Y Datasets 
X=[-1,0,1]
Y=[1,0,-1]
#Here we would need to start by using plt.plot(X-array,Y-Array)
#plt.plot(X,Y     )
plt.plot(X,Y,color='red', marker='o',mfc='black' ) # Hide
#plt.savefig(f'{argv[0]}.png', dpi=100) # Hide
#Next we would need to showcase the plot generated.
#plt.   () 

# %% Results

# %% Solution
#X and Y Datasets 
X=[-1,0,1]
Y=[1,0,-1]
#Making the color of the line red and marker black
plt.plot(X,Y,color='red', marker='o',mfc='black' ) 
plt.savefig(f'{argv[0]}.png', dpi=100) # Hide
#Next we would need to showcase the plot generated.
plt.show() 
