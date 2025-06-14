import pandas as pd

df = pd.read_csv("/content/Data Science Job Salaries.csv")  # Replace with your actual file name

print(df.info())
print(df.head())

print(df.describe())

# salary distribution
import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(10, 6))
sns.histplot(df['salary_in_usd'], bins=30, kde=True,color='blue')
plt.title('Salary Distribution (USD)')
plt.xlabel('Salary in USD')
plt.ylabel('Frequency')
plt.show()

# Salary VS experience level
 # mean salary of employees with different experience levels
mean_s_exp_lv =df.groupby('experience_level')['salary'].mean().sort_values()
mean_s_exp_lv

sns.set_style('whitegrid')
plt.figure(figsize=(14, 7))
sns.set_palette('spring')
plt.subplot(1, 2, 1)
ax = sns.barplot(x=mean_s_exp_lv.index, y=mean_s_exp_lv)
ax.set_title('Mean Salary Vs Experience Level',
fontdict={'fontsize': 16})
plt.subplot(1, 2, 2)
ax = sns.violinplot(data=df, x='experience_level', y='salary')
ax.set_title('Experience Level VS Salary',
fontdict={'fontsize': 16})

#Salary VS Employment Type
 # mean salary of employees with different employment types
mean_s_emp_type =df.groupby('employment_type')['salary'].mean().sort_values()
mean_s_emp_type

plt.figure(figsize=(14, 7))
sns.set_palette('autumn')
plt.subplot(1, 2, 1)
ax = sns.barplot(x=mean_s_emp_type.index, y=mean_s_emp_type)
ax.set_title('Mean Salary Vs Employment Type',
fontdict={'fontsize': 16})
plt.subplot(1, 2, 2)
ax = sns.boxplot(data=df, x='employment_type', y='salary')
ax.set_title('Employment Type VS Salary', fontdict={'fontsize': 16})

# Salary VS Company Size
 # mean salary of employees from different company sizes
mean_s_cmp_size =df.groupby('company_size')['salary'].mean().sort_values()
mean_s_cmp_size

plt.figure(figsize=(14, 7))
sns.set_palette('spring')
plt.subplot(1, 2, 1)
ax = sns.barplot(x=mean_s_cmp_size.index, y=mean_s_cmp_size)
ax.set_title('Mean Salary VS Company Size',
fontdict={'fontsize': 16})
plt.subplot(1, 2, 2)
sns.set_palette('Set2')
ax = sns.boxenplot(data=df, x='company_size', y='salary')
ax.set_title('Company Size VS Salary', fontdict={'fontsize':16})

# Create a job_type column from remote_ratio
df['job_type'] = df['remote_ratio'].map({
    0: 'Onsite',
    50: 'Hybrid',
    100: 'Remote'
})
mean_s_jtype = df.groupby('job_type')['salary'].mean().sort_values()
mean_s_jtype

#Salary VS Job type (remote, hybrid, onsite)
 # mean salary of employees with different job types
mean_s_jtype =df.groupby('job_type')['salary'].mean().sort_values()
mean_s_jtype

plt.figure(figsize=(14, 7))
sns.set_palette('spring')
plt.subplot(1, 2, 1)
ax = sns.barplot(x=mean_s_jtype.index, y=mean_s_jtype)
ax.set_title('Mean Salary VS Job Type', fontdict={'fontsize': 16})
plt.subplot(1, 2, 2)
ax = sns.violinplot(data=df, x='job_type', y='salary')
ax.set_title('Job Type VS Salary', fontdict={'fontsize': 16})

# job type and company size VS salary
plt.figure(figsize=(14, 7))
sns.set_palette('Set2')
ax = sns.boxenplot(data=df, x='job_type', y='salary',hue='company_size')
ax.set_title('Job Type & Company Size VS Salary',
fontdict={'fontsize': 16})

#Job Types and Experience Level distributions (Pie)
plt.figure(figsize=(12, 5))
sns.set_palette('Set2')
# job types
plt.subplot(1,2,1)
ax = df['job_type'].value_counts().plot(kind='pie',
autopct='%1.1f%%')
ax.set_title('Job Type', fontdict={'fontsize': 16})
ax.set_ylabel('')
 # experience levels
plt.subplot(1,2,2)
ax = df['experience_level'].value_counts().plot(kind='pie',autopct='%1.1f%%')
ax.set_title('Experience Level', fontdict={'fontsize': 16})
ax.set_ylabel('')

#Company Size VS Job Types Counts
plt.figure(figsize=(10, 5))
sns.set_palette('Set2')
ax = sns.countplot(data=df, x='company_size', hue='job_type')
ax.set_title('Company Size VS Job Types Counts',
fontdict={'fontsize': 16})

plt.figure(figsize=(10, 8))
numeric_df = df.select_dtypes(include=['number'])  # Keep only numeric columns
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
plt.title('Feature Correlation')
plt.show()

# Boxplot for salaries by experience level
plt.figure(figsize=(12, 6))
sns.boxplot(x='experience_level', y='salary_in_usd', data=df)
plt.title('Salary by Experience Level')
plt.xlabel('Experience Level')
plt.ylabel('Salary in USD')
plt.show()

# Remote ratio vs salary
plt.figure(figsize=(12, 6))
sns.barplot(x='remote_ratio', y='salary_in_usd', data=df)
plt.title('Salary by Remote Ratio')
plt.xlabel('Remote Ratio')
plt.ylabel('Salary in USD')
plt.show()

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Drop unnecessary columns
df_clean = df.drop(['Unnamed: 0', 'salary', 'salary_currency'], axis=1)

# Convert categorical variables to dummy/one-hot variables
df_encoded = pd.get_dummies(df_clean, drop_first=True)

# Split features and target
X = df_encoded.drop('salary_in_usd', axis=1)
y = df_encoded['salary_in_usd']

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict and evaluate
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")
print(f"Mean Absolute Error: {mae}")

print("Data Science Job Salaries")
print(df.describe())
