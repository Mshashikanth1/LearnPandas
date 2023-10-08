import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students.loc[students["student_id"]==101, ["name","age"]]
    




"""
2880. Select Data
Easy
11
1
Companies
DataFrame students
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| student_id  | int    |
| name        | object |
| age         | int    |
+-------------+--------+

Write a solution to select the name and age of the student with student_id = 101.

The result format is in the following example.

 

Example 1:
Input:
+------------+---------+-----+
| student_id | name    | age |
+------------+---------+-----+
| 101        | Ulysses | 13  |
| 53         | William | 10  |
| 128        | Henry   | 6   |
| 3          | Henry   | 11  |
+------------+---------+-----+
Output:
+---------+-----+
| name    | age | 
+---------+-----+
| Ulysses | 13  |
+---------+-----+
Explanation:
Student Ulysses has student_id = 101, we select the name and age.
Accepted
1.5K
Submissions
1.9K
Acceptance Rate
79.8%
Seen this question in a real interview before?
1/4
Yes
No
Discussion (0)

Overview
This problem provides us with a pandas DataFrame and requires us to return data about one of the records in the DataFrame.

Key Concepts:

DataFrame: a 2D table-like structure, similar to a spreadsheet or SQL table. Each row represents an individual record and each column represents a different attribute. It is size-mutable designed to handle a mix of different types of data.
loc attribute: one of the primary ways to select data from a DataFrame. It is label-based, which means you have to specify the name of the rows or columns to select data. loc is label-based. If you are looking to use integer-based location, use iloc instead.
boolean mask: a series of True/False values used to filter or select elements from another data structure, such as a list, array, or DataFrame, based on a certain condition.
Intuition
The students DataFrame has three columns:

student_id (type: int) - a unique identifier for the student.
name (type: object, which is generally a string in pandas) - the student's name.
age (type: int) - the student's age.
In this problem, we must create a function that accepts a DataFrame as an argument and returns a DataFrame with the required information.

Inside our function, we will use the loc function to select the row where student_id is 101 and return the value from the name and age columns.

To do this, we must provide loc with two arguments.

students.loc[students['student_id'] == 101, ['name', 'age']]
Visualization of loc function

fig

When you pass this DataFrame to the function:

student_id	name	age
101	Ulysses	13
53	William	10
128	Henry	6
3	Henry	11

It will return:

name	age
Ulysses	13

Implementation

Comments (1)

Sort by:Best
Type comment here... (Markdown supported)
Preview
Comment
💡 Article Commenting Rules
1. This comment section is for questions and comments regarding this LeetCode article. All posts must respect our LeetCode Community Rules.

2. Concerns about errors or bugs in the article, problem description, or test cases should be posted on LeetCode Feedback, so that our team can address them.


suraj479
Oct 06, 2023
I typed the same thing. But somehow it didn't work for me .
"""
