import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:

    employees["bonus"] = employees["salary"]*2
    return employees
    






"""
2881. Create a New Column
Easy
10
2
Companies
DataFrame employees
+-------------+--------+
| Column Name | Type.  |
+-------------+--------+
| name        | object |
| salary      | int.   |
+-------------+--------+
A company plans to provide its employees with a bonus.

Write a solution to create a new column name bonus that contains the doubled values of the salary column.

The result format is in the following example.

 

Example 1:

Input:
DataFrame employees
+---------+--------+
| name    | salary |
+---------+--------+
| Piper   | 4548   |
| Grace   | 28150  |
| Georgia | 1103   |
| Willow  | 6593   |
| Finn    | 74576  |
| Thomas  | 24433  |
+---------+--------+
Output:
+---------+--------+--------+
| name    | salary | bonus  |
+---------+--------+--------+
| Piper   | 4548   | 9096   |
| Grace   | 28150  | 56300  |
| Georgia | 1103   | 2206   |
| Willow  |  593   | 13186  |
| Finn    | 74576  | 149152 |
| Thomas  | 24433  | 48866  |
+---------+--------+--------+
Explanation: 
A new column bonus is created by doubling the value in the column salary.
Accepted
1.6K
Submissions
1.7K
Acceptance Rate



4.5
(2 votes)

Solution
Overview
This problem requires us to create a new column 'bonus' in the DataFrame employees. The new column should contain double the value of each employee's salary.

Key Concepts:

pandas Series: a one dimensional data structure provided by the pandas library. A Series can be thought of as a column of data in a pandas DataFrame. A Series can contain of a wide-range of data types, however they are homogenous, meaning that all elements within one pandas Series must be of the same data type. Like DataFrames, Series are indexed and can be labeled for easy data retrieval.
pandas DataFrame: similar to a SQL table, a DataFrame is a collection of Series displayed as columns. They are size-mutable, meaning we can add, delete, and alter values, rows, and columns in a DataFrame.
column-wise operations: operations that can be performed on each individual element in a DataFrame Series. A few examples of types of column-wise operations are arithmetic operations, aggregate functions, filtering and conditional operations, and string operations.
Intuition
To solve this problem, we can create a new column and calculate the bonus using the column-wise operation * to multiply the salary column by 2.

The simplest way to create a new column will be to assign the new column to the employees DataFrame using the column name. Then, we will set it equal to the value of the salary column multiplied by two.

Visualization of column-wise operations

fig

Example:
If you have the following DataFrame:

name	salary
Piper	4548
Grace	28150

employees['salary'] would give:

index	salary
0	4548
1	28150

pandas allows for vectorized operations. When you multiply a Series by a scalar (a single number), it multiplies every single element in the Series by that number. In our case, we want to use this to double each value in the salary column.

Using the previous DataFrame, employees['salary'] * 2 would result in:

index	bonus
0	9096
1	56300

We can assign these values to a new (or existing) column in the DataFrame. If the column bonus doesn't already exist, pandas will create it.

When we do employees['bonus'] = employees['salary'] * 2, we're creating a new column called bonus in the DataFrame employees, and populating it with the doubled values of the salary column.

Implementation

Comments (0)

Sort by:Best



"""
