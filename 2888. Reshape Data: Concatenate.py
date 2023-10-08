import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return pd.concat([df1,df2], axis=0)






"""

2888. Reshape Data: Concatenate
Easy
8
1
Companies
DataFrame df1
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| student_id  | int    |
| name        | object |
| age         | int    |
+-------------+--------+

DataFrame df2
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| student_id  | int    |
| name        | object |
| age         | int    |
+-------------+--------+

Write a solution to concatenate these two DataFrames vertically into one DataFrame.

The result format is in the following example.

 

Example 1:

Input:
df1
+------------+---------+-----+
| student_id | name    | age |
+------------+---------+-----+
| 1          | Mason   | 8   |
| 2          | Ava     | 6   |
| 3          | Taylor  | 15  |
| 4          | Georgia | 17  |
+------------+---------+-----+
df2
+------------+------+-----+
| student_id | name | age |
+------------+------+-----+
| 5          | Leo  | 7   |
| 6          | Alex | 7   |
+------------+------+-----+
Output:
+------------+---------+-----+
| student_id | name    | age |
+------------+---------+-----+
| 1          | Mason   | 8   |
| 2          | Ava     | 6   |
| 3          | Taylor  | 15  |
| 4          | Georgia | 17  |
| 5          | Leo     | 7   |
| 6          | Alex    | 7   |
+------------+---------+-----+
Explanation:
The two DataFramess are stacked vertically, and their rows are combined.
Accepted
1K
Submissions
1.2K
Acceptance Rate



Solution
Overview
In the task presented, the goal is to concatenate two DataFrames, df1 and df2, vertically. The DataFrames have the same structure with columns student_id, name, and age.

Key Concepts:

pd.concat(): A convenient function within pandas used to concatenate DataFrames either vertically (by rows) or horizontally (by columns).
The objs parameter is a sequence or mapping of Series or DataFrame objects to be concatenated.
The axis parameter determines the direction of concatenation:
axis=0 is set as the default value, which means it will concatenate DataFrames vertically (by rows).
axis=1 will concatenate DataFrames horizontally (by columns).
Intuition
The process of concatenating DataFrames vertically involves stacking one DataFrame on top of the other, ensuring the order of columns is consistent.

Inside the concatenateTables function, we utilize the pd.concat() function to concatenate the DataFrames. Since we are concatenated df1 and df2 we pass the list [df1, df2] as the first argument for objs; and since we are concatenating vertically, we set axis=0.

Visualization of the pd.concat() function applied to the df1 and df2 DataFrames:

fig

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
    
