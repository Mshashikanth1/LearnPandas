import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    customers.drop_duplicates(subset='email', keep='first', inplace=True)
    return customers
    




"""
2882. Drop Duplicate Rows
Easy
14
1
Companies
DataFrame customers
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| customer_id | int    |
| name        | object |
| email       | object |
+-------------+--------+
There are some duplicate rows in the DataFrame based on the email column.

Write a solution to remove these duplicate rows and keep only the first occurrence.

The result format is in the following example.

 

Example 1:
Input:
+-------------+---------+---------------------+
| customer_id | name    | email               |
+-------------+---------+---------------------+
| 1           | Ella    | emily@example.com   |
| 2           | David   | michael@example.com |
| 3           | Zachary | sarah@example.com   |
| 4           | Alice   | john@example.com    |
| 5           | Finn    | john@example.com    |
| 6           | Violet  | alice@example.com   |
+-------------+---------+---------------------+
Output:  
+-------------+---------+---------------------+
| customer_id | name    | email               |
+-------------+---------+---------------------+
| 1           | Ella    | emily@example.com   |
| 2           | David   | michael@example.com |
| 3           | Zachary | sarah@example.com   |
| 4           | Alice   | john@example.com    |
| 6           | Violet  | alice@example.com   |
+-------------+---------+---------------------+
Explanation:
Alic (customer_id = 4) and Finn (customer_id = 5) both use john@example.com, so only the first occurrence of this email is retained.
Accepted
1.2K
Submissions
1.5K
Acceptance Rate
83.1%
Seen this question in a real interview before?
1/4
Yes
No


Solution
Overview
In this problem, we have a DataFrame named customers that consists of details like customer_id, name, and email. The goal is to remove duplicate rows based on the email column and only keep the first occurrence of any duplicated email.

Key Concepts:

DataFrame: a 2D table-like structure, similar to a spreadsheet or SQL table. Each row represents an individual record and each column represents a different attribute. It is size-mutable and designed to handle a mix of different types of data.
drop_duplicates Function: The drop_duplicates function is a method of the DataFrame object in the pandas library. Its purpose is to drop duplicate rows, and you can specify the criteria based on which the rows are considered duplicates.
drop_duplicates Function Argument Definition:

subset: This is the column label or sequence of labels to consider for identifying duplicate rows. If not provided, it considers all columns in the DataFrame.

keep: This argument determines which duplicate row to retain.

'first': (default) Drop duplicates except for the first occurrence.
'last': Drop duplicates except for the last occurrence.
False: Drop all duplicates.
inplace: If set to True, the changes are made directly to the object without returning a new object. If set to False (default), a new object with duplicates dropped will be returned.

Intuition
Let’s go step by step through the provided solution:

1. Importing pandas:

import pandas as pd
This imports the pandas library and gives it an alias pd. pandas is a fast, powerful, flexible, and easy-to-use open-source data analysis and data manipulation library built on top of the Python programming language.

2. Defining the function:

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
This line defines a new function named dropDuplicateEmails which takes a DataFrame customers as an input argument and returns a DataFrame.

3. Dropping duplicate rows based on email:

customers.drop_duplicates(subset='email', keep='first', inplace=True)
This line uses the drop_duplicates method on the customers DataFrame.

subset='email': This means that we are considering duplicates based on the email column only.
keep='first': This indicates that we want to keep the first occurrence of any duplicated email and drop the subsequent occurrences.
inplace=True: This means the changes will be made directly to the passed DataFrame (customers) without returning a new one.
4. Returning the modified DataFrame:

return customers
Finally, we return the modified customers DataFrame with the duplicate rows based on email removed.

Using the Solution

By using the provided function, you can clean up the data in your customers DataFrame and ensure that each customer's email is unique, helping maintain data integrity. If two customers have the same email address, only the first one encountered will be kept in the resulting DataFrame.

Visualization of dropDuplicateEmails function

fig

When you pass this DataFrame to the function:

customer_id	name	email
1	Ella	emily@example.com
2	David	michael@example.com
3	Zachary	sarah@example.com
4	Alice	john@example.com
5	Finn	john@example.com
6	Violet	alice@example.com

It will return:

customer_id	name	email
1	Ella	emily@example.com
2	David	michael@example.com
3	Zachary	sarah@example.com
4	Alice	john@example.com
6	Violet	alice@example.com
Implementation

Note: using inplace=True modifies the original DataFrame. To retain the original DataFrame and get a new one with duplicates removed, we should set inplace=False and assign the result to a new variable.

Comments (0)

Sort by:Best
Type comment here... (Markdown supported)
Preview
Comment
💡 Article Commenting Rules
1. This comment section is for questions and comments regarding this LeetCode article. All posts must respect our LeetCode Community Rules.

2. Concerns about errors or bugs in the article, problem description, or test cases should be posted on LeetCode Feedback, so that our team can address them
"""
