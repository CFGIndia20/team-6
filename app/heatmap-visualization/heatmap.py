import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv("C:\\Users\\ANJALI\\Desktop\\heat.csv")
#print(df.head(10))
category = ((np.asarray(df['Categories'])).reshape(6,5))
number = ((np.asarray(df['Number'])).reshape(6,5))

#print(category)
#print(number)

result = df.pivot(index='Yrows',columns='Xcols',values='Number')
#print(result)

labels = (np.asarray(["{0} \n {1:.2f}".format(symb,value)
                      for symb,value in zip(category.flatten(),
                                            number.flatten())])
          ).reshape(6,5)

fig, ax =plt.subplots(figsize=(12,7))
title = "Heat Map To Show Number of Complaints received in any Category"
plt.title(title,fontsize=18)
ttl=ax.title
ttl.set_position([0.5,1.05])
ax.set_xticks([])
ax.set_yticks([])
ax.axis('off')

sns.heatmap(result,annot=labels,fmt="",cmap='RdYlGn',linewidth=0.30,ax=ax)
plt.show()
