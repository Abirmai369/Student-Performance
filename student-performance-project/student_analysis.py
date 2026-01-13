import pandas as pd
import matplotlib.pyplot as plt


# STEP 2: Load the dataset
# NOTE: Dataset is semicolon (;) separated
df = pd.read_csv("student-mat.csv", sep=';')
print("Dataset loaded successfully\n")


# STEP 3: Explore the dataset
print("First 5 records:")
print(df.head(), "\n")


# STEP 4: Inspect dataset shape
print("Dataset Shape (Rows, Columns):")
print(df.shape, "\n")


# STEP 5: Inspect data types
print("Data Types:")
print(df.dtypes, "\n")


# STEP 6: Check missing values
print("Missing Values:")
print(df.isnull().sum(), "\n")


# STEP 7: Remove duplicate rows
print("Duplicate rows before:", df.duplicated().sum())
df = df.drop_duplicates()
print("Duplicate rows after:", df.duplicated().sum(), "\n")


# ================================
# ANALYSIS QUESTIONS
# ================================

# Q1: Average final grade (G3)
average_g3 = df['G3'].mean()
print("Average Final Grade (G3):", average_g3)


# Q2: Number of students scoring above 15
above_15 = df[df['G3'] > 15].shape[0]
print("Students scoring above 15:", above_15)


# Q3: Correlation between study time and performance
correlation = df['studytime'].corr(df['G3'])
print("Study Time vs Performance Correlation:", correlation)


# Q4: Gender-wise average performance
gender_avg = df.groupby('sex')['G3'].mean()
print("\nAverage Grade by Gender:")
print(gender_avg)


# ================================
# VISUALIZATIONS
# ================================

# Histogram of final grades
plt.figure()
plt.hist(df['G3'], bins=10)
plt.xlabel("Final Grade")
plt.ylabel("Number of Students")
plt.title("Histogram of Final Grades")
plt.show()


# Scatter plot: Study time vs grades
plt.figure()
plt.scatter(df['studytime'], df['G3'])
plt.xlabel("Study Time")
plt.ylabel("Final Grade")
plt.title("Study Time vs Grades")
plt.show()


# Bar chart: Male vs Female average score
plt.figure()
gender_avg.plot(kind='bar')
plt.xlabel("Gender")
plt.ylabel("Average Final Grade")
plt.title("Average Grade by Gender")
plt.show()