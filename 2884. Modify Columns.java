import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary'] = employees['salary'] *2
    return employees
    


"""

2884. Modify Columns
Easy
8
1
Companies
DataFrame employees
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| name        | object |
| salary      | int    |
+-------------+--------+
A company intends to give its employees a pay rise.

Write a solution to modify the salary column by multiplying each salary by 2.

The result format is in the following example.

 

Example 1:

Input:
DataFrame employees
+---------+--------+
| name    | salary |
+---------+--------+
| Jack    | 19666  |
| Piper   | 74754  |
| Mia     | 62509  |
| Ulysses | 54866  |
+---------+--------+
Output:
+---------+--------+
| name    | salary |
+---------+--------+
| Jack    | 39332  |
| Piper   | 149508 |
| Mia     | 125018 |
| Ulysses | 109732 |
+---------+--------+
Explanation:
Every salary has been doubled.
Accepted
1.4K
Submissions
1.5K
Acceptance Rate
89.7%
Seen this question in a real interview before?
1/4
Yes
No

Overview
Our objective is to modify the salary column in the DataFrame employees so that each employee's salary is doubled.

Key Concepts:

column-wise operations: operations that can be performed on each individual element in a DataFrame Series. A few examples of types of column-wise operations are arithmetic operations, aggregate functions, filtering and conditional operations, and string operations.
Intuition
We double the salary for each employee by multiplying the salary column by 2. In pandas, operations can be applied column-wise, affecting each element in the column.

employees['salary'] = employees['salary'] * 2
Visualization of column-wise operations

fig

This line modifies the salary column of the employees DataFrame by doubling each value. Let's break it down piece by piece:

1. employees['salary']:

This is how you access a specific column of a DataFrame in pandas. employees is the DataFrame, and ['salary'] refers to the column named "salary". It will return a pandas Series, which is a one-dimensional labeled array.

So, employees['salary'] will give you all the values in the salary column of the DataFrame employees.

Example:
If you have the following DataFrame:

name	salary
Jack	19666
Piper	74754
Mia	62509
Ulysses	54866

employees['salary'] would give:

index	salary
0	19666
1	74754
2	62509
3	54866

2. employees['salary']

pandas allows for vectorized operations. When you multiply a Series by a scalar (a single number), it multiplies every single element in the Series by that number.

In our case, it's doubling each value in the salary column.

Example:
Using the previous DataFrame, employees['salary'] * 2 would result in:

index	salary
0	39332
1	149508
2	125018
3	109732

3. employees['salary'] = ...:

This line updates the values in an existing column of the DataFrame. If the column salary didn't exist for some reason, pandas would create it.

In the statement employees['salary'] = employees['salary'] * 2, what we're essentially doing is taking each salary value from the salary column, doubling it, and then updating the original salary column with these newly calculated values.

The DataFrame employees retains its salary column, but the values within this column have now been updated to be twice their original amounts.

Implementation

Comments (0)

Sort by:Best


"""
