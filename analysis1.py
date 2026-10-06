import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('/mnt/c/Users/joshu/Downloads/Iris.csv')
print(df.head())

print("\nDataset information:")
print(df.info())

print("\nDataset shape:")
print(df.shape)

print("\nMissing values:")
print(df.isnull().sum())

print("\nDataset description:")
print(df.describe())

print("\nSpecies counts:")
print(df['Species'].value_counts())

print("\nMean values by species:")
print(df.groupby('Species').mean(numeric_only=True))

#visualization
# Histogram
plt.hist(df['SepalLengthCm'], bins=18)
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.title('Distribution of Sepal Length')
plt.savefig('histogram.png')
plt.close()


# Scatter plot
plt.scatter(df['PetalLengthCm'], df['PetalWidthCm'])
plt.xlabel('Petal Length (cm)')
plt.ylabel('Petal Width (cm)')
plt.title('Petal Length vs Petal Width')
plt.savefig('scatter_plot.png')
plt.close()

# Line chart
mean_values = df.groupby('Species').mean(numeric_only=True)

mean_values.plot(kind='line', marker='o')

plt.xlabel('Species')
plt.ylabel('Average Measurement (cm)')
plt.title('Average Iris Measurements by Species')
plt.legend()
plt.grid()
plt.savefig('line_chart.png')
plt.close()

# Bar chart
df['Species'].value_counts().plot(kind='bar')
plt.xlabel('Species')
plt.ylabel('Number of Samples')
plt.title('Number of Samples per Species')
plt.savefig('bar_chart.png')
plt.close()