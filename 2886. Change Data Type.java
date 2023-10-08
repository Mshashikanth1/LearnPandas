import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students=students.astype({'grade':int})
    return students



"""
2886. Change Data Type
Easy
8
2
Companies
DataFrame students
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| student_id  | int    |
| name        | object |
| age         | int    |
| grade       | float  |
+-------------+--------+
Write a solution to correct the errors:

The grade column is stored as floats, convert it to integers.

The result format is in the following example.

 

Example 1:
Input:
DataFrame students:
+------------+------+-----+-------+
| student_id | name | age | grade |
+------------+------+-----+-------+
| 1          | Ava  | 6   | 73.0  |
| 2          | Kate | 15  | 87.0  |
+------------+------+-----+-------+
Output:
+------------+------+-----+-------+
| student_id | name | age | grade |
+------------+------+-----+-------+
| 1          | Ava  | 6   | 73    |
| 2          | Kate | 15  | 87    |
+------------+------+-----+-------+
Explanation: 
The data types of the column grade is converted to int.
Accepted
1.1K
Submissions
1.2K
Acceptance Rate
84.5%
Seen this question in a real interview before?
1/4
Yes
No
Discussion (0)


Solution
Overview
In this problem, we have a DataFrame named students that contains student data. However, the grades are stored as floats instead of integers. The goal is to change the grade type from floats to integers.

Key Concepts:

DataFrame: a 2D table-like structure, similar to a spreadsheet or SQL table. Each row represents an individual record and each column represents a different attribute. It is size-mutable and designed to handle a mix of different types of data.
astype Function: The astype function is used to cast a pandas object to a specified dtype (data type). astype can be used to cast a pandas object to any dtype. The astype function does not modify the original DataFrame in place. Instead, it returns a new DataFrame with the specified data type changes. If you want to reflect changes in the original DataFrame, you need to reassign the result back to it or use the copy parameter accordingly. The function’s syntax is:
DataFrame.astype(dtype, copy=True, errors='raise')
Where:

dtype: It's a data type, or dict of column name -> data type.
copy: By default, astype always returns a newly allocated object. If copy is set to False, a new object will only be created if the old object cannot be casted to the required type.
errors: Controls the raising of exceptions on invalid data for the provided dtype. By default, raise is set which means exceptions will be raised.
So in our case we want to cast the grade column from float to int and we can do so with the following line:

students = students.astype({'grade': int})
Intuition
Visualization of astype function

fig

In the provided solution:

students = students.astype({'grade': int})
This line is casting the grade column from float to int.

Let’s go step by step through the provided solution:

Importing pandas:

import pandas as pd
This line imports the pandas library and gives it an alias name pd. The pandas library provides fast, flexible, and expressive data structures designed to work with structured (tabular, multidimensional, potentially heterogeneous) data.

Function Definition:

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
This line defines a function named changeDatatype that takes in a DataFrame students as an argument and returns a DataFrame.

Changing Data Type of a Column:

students = students.astype({'grade': int})
This line of code is the heart of the solution. It changes the data type of the grade column to integer using the astype function. The {'grade': int} is a dictionary where the key is the column name and the value is the desired data type.

Return Statement:

return students
This line returns the modified DataFrame.

Using the Solution

When you pass this DataFrame to the function:

student_id	name	age	grade
1	Ava	6	73.0
2	Kate	15	87.0

It will return:

student_id	name	age	grade
1	Ava	6	73
2	Kate	15	87

Implementation

Comments (0)

Sort by:Best
Type comment here... (Markdown supported)
Preview
Comment
💡 Article Commenting Rules
1. This comment section is for questions and comments regarding this LeetCode article. All posts must respect our LeetCode Community Rules.

2. Concerns about errors or bugs in the article, problem description, or test cases should be posted on LeetCode Feedback, so that our team can address them.

"""
