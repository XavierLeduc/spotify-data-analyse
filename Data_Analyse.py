import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# 1. Read the data
df = pd.read_csv('spotify_songs.csv')
print(df.head())
print(df.describe())

