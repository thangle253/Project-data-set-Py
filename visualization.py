import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('cars.csv')
sns.histplot(data=df, x='buying', kde=True)
plt.show()
