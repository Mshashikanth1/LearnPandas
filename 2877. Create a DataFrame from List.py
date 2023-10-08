import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    columns_names=["student_id", "age"]
    result_dataframe=pd.DataFrame(student_data, columns=columns_names)
    return result_dataframe



"""
2877. Create a DataFrame from List
Easy
20
1
Companies
Write a solution to create a DataFrame from a 2D list called student_data. This 2D list contains the IDs and ages of some students.

The DataFrame should have two columns, student_id and age, and be in the same order as the original 2D list.

The result format is in the following example.

 

Example 1:

Input:
student_data:
[
  [1, 15],
  [2, 11],
  [3, 11],
  [4, 20]
]
Output:
+------------+-----+
| student_id | age |
+------------+-----+
| 1          | 15  |
| 2          | 11  |
| 3          | 11  |
| 4          | 20  |
+------------+-----+
Explanation:
A DataFrame was created on top of student_data, with two columns named student_id and age.
Accepted
2.3K
Submissions
2.9K


Overview
A DataFrame is a powerful and convenient data structure provided by the pandas library. It is a 2D table-like structure, similar to a spreadsheet or SQL table. Each row represents an individual record and each column represents a different attribute.

In this solution, we aim to convert a 2D list into a pandas DataFrame. This is a common application of the pandas library for when we have raw data in list format and want to convert it to a more structured, labeled format for easier analysis.

Key Concepts:

2D List: A list of lists where each inner list represents a row of data.
DataFrame: A 2-dimensional labeled data structure in pandas.
Intuition
Let's explore step by step how to create a DataFrame with the tools provided by the pandas library.

Importing pandas:

import pandas as pd
This line imports the pandas library and gives it an alias name pd. The pandas library provides fast, flexible, and expressive data structures designed to work with structured (tabular, multidimensional, potentially heterogeneous) data.

Function Definition:

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
This line defines a function named createDataframe that takes in a DataFrame student_data as an argument and returns a DataFrame.

Using pd.DataFrame():

pd.DataFrame(student_data) will allow us to transform our 2D list into a DataFrame.

The diagram below offers a visual representation of the pd.DataFrame() function in action:

fig

You can see that the resultant DataFrame has headers labeled as 0 and 1. This is because all DataFrames are labeled and will create headers by default using integers starting from 0.

We can set custom column names using the columns parameter. First, we create a list of our column names in the order that they will be displayed on the DataFrame. Then, we will provide the list as a parameter when we call the pd.DataFrame() function.

column_names = ["student_id", "age"]

pd.DataFrame(student_data, columns=column_names)

The subsequent diagram demonstrates the impact of the columns parameter:

fig

Implementation

Comments (2)

Sort by:Best
Type comment here... (Markdown supported)
Preview
Comment
💡 Article Commenting Rules
1. This comment section is for questions and comments regarding this LeetCode article. All posts must respect our LeetCode Community Rules.

2. Concerns about errors or bugs in the article, problem description, or test cases should be posted on LeetCode Feedback, so that our team can address them.


jmulero2
Oct 06, 2023
I found an error in the Function Definition section of the article: "... a function named createDataframe that takes in a DataFrame student_data as an argument ...". The function createDataframe does not take a DataFrame as an argument. It takes in a 2D List called student_data as an argument.
"""

    
