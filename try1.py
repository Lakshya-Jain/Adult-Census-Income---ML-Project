import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dataset = pd.read_csv("adult.csv")
dataset.head()
dataset.info()
dataset.describe()
dataset['income'].value_counts()

#checking the dataset
sns.heatmap(dataset.isnull(), yticklabels=False, cbar=False, cmap="Blues" )
dataset.isnull().sum()
'''nothing is missing that`s good'''

#preprocessing step
db = datset.drop['fnlwgt']

