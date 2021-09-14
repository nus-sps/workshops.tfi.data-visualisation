# %% Result

# %% Tasks
'''
With your new dataframe:

1. Plot a boxplot of the test scores of `math.score`

2. Separate the boxplot into two groups of students that have taken the test preparation course and those who haven't.

3. Label the axis properly
'''

# %% Solution
import pandas as pd # Hide
from sys import argv  # Hide
import matplotlib.pyplot as plt

link = 'https://raw.githubusercontent.com/nus-sps/workshops.tfi.data-visualisation/darren-branch/files/StudentPerformance2.csv' # Hide
df = pd.read_csv(link) # Hide
df_dropped = df.drop(columns = ['lunch', 'gender']) # Hide

#Plotting boxplot
ax = df.boxplot('math.score', by='test.preparation.course')
ax.grid(alpha = 0.25)

# Don't forget to add the labels for clarity!
plt.suptitle('')
plt.title('Boxplot of Math Scores grouped by Test Prep Course Completion')
plt.ylabel('Math Scores')
plt.xlabel('Test Prep Course Completion status')
plt.tight_layout()
plt.savefig(f'{argv[0]}.png')  # Hide
plt.show()

# %% Interpreting the results
'''
- It seems that completing the test preperatiion course helped only a little bit in increasing math scores.

- You can see this by the differing means. But the difference is very small.

- Maybe the test preparation course might not be working as effectively as we thought!

- More statistical testing needs to be done (a simple t-test might be suitable)

- You can try to familiarise yourself by changing the code so as to plot the different test scores!
'''
