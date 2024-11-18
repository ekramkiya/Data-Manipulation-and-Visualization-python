import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("Titanic-Dataset.csv")
# Check for missing values
# print(data.isnull().sum())

# Fill missing 'Age' with median age
data['Age'] = data['Age'].fillna(data['Age'].median())

# Fill missing 'Embarked' with the most common value
data['Embarked'] = data['Embarked'].fillna(data['Embarked'].mode()[0])

# Drop 'Cabin' column due to too many missing values
data = data.drop('Cabin', axis=1)
print(data.isnull().sum())
# Create a new column 'FamilySize' by combining 'SibSp' and 'Parch'
data['FamilySize'] = data['SibSp'] + data['Parch'] + 1

# Create a new column 'IsAlone' to indicate if a passenger is alone
data['IsAlone'] = (data['FamilySize'] == 1).astype(int)

# Filter data to get only passengers who survived
survived = data[data['Survived'] == 1]

# Filter data to get only passengers who did not survive
not_survived = data[data['Survived'] == 0]

# Filter data to get only passengers who survived
survived = data[data['Survived'] == 1]

# Filter data to get only passengers who did not survive
not_survived = data[data['Survived'] == 0]

# Plot the distribution of ages
plt.figure(figsize=(10, 6))
plt.hist(data['Age'], bins=30, color='skyblue', edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Plot survival rate based on passenger class
plt.figure(figsize=(10, 6))
data['Pclass'].value_counts().sort_index().plot(kind='bar', color='orange', edgecolor='black')
plt.title('Number of Passengers in Each Class')
plt.xlabel('Passenger Class')
plt.ylabel('Number of Passengers')
plt.show()

# Plot survival rate based on whether passengers were alone
plt.figure(figsize=(10, 6))
data['IsAlone'].value_counts().plot(kind='bar', color='green', edgecolor='black')
plt.title('Survival Rate Based on Being Alone')
plt.xlabel('Is Alone')
plt.ylabel('Number of Passengers')
plt.xticks(ticks=[0, 1], labels=['With Family', 'Alone'])
plt.show()

# print(data)