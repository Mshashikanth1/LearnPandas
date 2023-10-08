import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)




"""
2879. Display the First Three Rows
Easy
11
5
Companies
DataFrame: employees
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| employee_id | int    |
| name        | object |
| department  | object |
| salary      | int    |
+-------------+--------+
Write a solution to display the first 3 rows of this DataFrame.

 

Example 1:

Input:
DataFrame employees
+-------------+-----------+-----------------------+--------+
| employee_id | name      | department            | salary |
+-------------+-----------+-----------------------+--------+
| 3           | Bob       | Operations            | 48675  |
| 90          | Alice     | Sales                 | 11096  |
| 9           | Tatiana   | Engineering           | 33805  |
| 60          | Annabelle | InformationTechnology | 37678  |
| 49          | Jonathan  | HumanResources        | 23793  |
| 43          | Khaled    | Administration        | 40454  |
+-------------+-----------+-----------------------+--------+
Output:
+-------------+---------+-------------+--------+
| employee_id | name    | department  | salary |
+-------------+---------+-------------+--------+
| 3           | Bob     | Operations  | 48675  |
| 90          | Alice   | Sales       | 11096  |
| 9           | Tatiana | Engineering | 33805  |
+-------------+---------+-------------+--------+
Explanation: 
Only the first 3 rows are displayed.
Accepted
2K
Submissions
2.2K
Acceptance Rate
92.4%
Seen this question in a real interview before?
1/4
Yes


Overview
This problem requires us to return the first 3 rows of the employees DataFrame.

Key Concepts:

DataFrame: a 2D table-like structure, similar to a spreadsheet or SQL table. Each row represents an individual record and each column represents a different attribute. It is size-mutable and designed to handle a mix of different types of data.
head method: a method provided by the pandas library that is used on a DataFrame to return the first n rows. If n is omitted, it defaults to returning the first 5 rows. This is useful to get an overview or quick look at the beginning of large datasets.
Intuition
Let's explore step by step how to return the first 3 rows of a DataFrame.

Importing pandas:

import pandas as pd
This line imports the pandas library and gives it an alias name pd. The pandas library provides fast, flexible, and expressive data structures designed to work with structured (tabular, multidimensional, potentially heterogeneous) data.

Utilizing head:

Let's look at an example to see how we can use head to solve our problem.

Given the employees DataFrame as:

employee_id	name	department	salary
3	Bob	Operations	48675
90	Alice	Sales	11096
9	Tatiana	Engineering	33805
60	Annabelle	InformationTechnology	37678
49	Jonathan	HumanResources	23793
43	Khaled	Administration	40454

We return the employees DataFrame using the the head function with an input of 3, to indicate we want to return the first 3 rows:

return employees.head(3)
The dataframe returned is then:

employee_id	name	department	salary
3	Bob	Operations	48675
90	Alice	Sales	11096
9	Tatiana	Engineering	33805

Visualization of the head function applied to the employees DataFrame:

fig

Implementation

Comments (1)

Sort by:Best
Type comment here... (Markdown supported)
Preview
Comment
💡 Article Commenting Rules
1. This comment section is for questions and comments regarding this LeetCode article. All posts must respect our LeetCode Community Rules.

2. Concerns about errors or bugs in the article, problem description, or test cases should be posted on LeetCode Feedback, so that our team can address them.


Uzmaaly
Oct 06, 2023
Such a good explanation!!

"""
