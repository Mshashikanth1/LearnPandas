import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    students.dropna(subset=['name'], inplace=True)
    return students
    




"""
2883. Drop Missing Data
Easy
9
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
There are some rows having missing values in the name column.

Write a solution to remove the rows with missing values.

The result format is in the following example.

 

Example 1:

Input:
+------------+-------+-----+
| student_id | name  | age |
+------------+-------+-----+
| 32         | Piper | 5   |
| 217        | Grace | 19  |
| 779        | None  | 20  |
| 849        | None  | 14  |
+------------+-------+-----+
Output:
+------------+-------+-----+
| student_id | name  | age |
+------------+-------+-----+
| 32         | Piper | 5   |
| 217        | Grace | 19  |
+------------+-------+-----+
Explanation: 
Students with ids 779 and 849 have empty values in the name column, so they will be removed.
Accepted
1.2K
Submissions
1.4K
Acceptance Rate
89.4%
Seen this question in a real interview before?
1/4



Overview
The problem pertains to the handling of missing data in a pandas DataFrame representing student information. Specifically, there are some rows in the name column that have missing values (None or NaN). The objective is to remove those rows with missing names from the DataFrame using the dropna function of pandas.

Key Concepts:

dropna Function: The dropna function belongs to the pandas DataFrame and is used to remove missing values. Missing data in pandas is generally represented by the NaN (short for Not a Number) value, though in your example it appears as None which is also considered a missing value by pandas.
Here's the general usage of the dropna function:

DataFrame.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
dropna Function Argument Definition:

axis: It can be {0 or 'index', 1 or 'columns'}. By default it's 0. If axis=0, it drops rows which contain missing values, and if axis=1, it drops columns which contain missing value.
how: Determines if row or column is removed from DataFrame, when we have at least one NA or all NA.
how='any' : If any NA values are present, drop that row or column (default).
how='all' : If all values are NA, drop that row or column.
thresh: Require that many non-NA values. This is an integer argument which requires a minimum number of non-NA values to keep the row/column.
subset: Labels along the other axis to consider, e.g. if you are dropping rows these would be a list of columns to include. This is particularly useful when you only want to consider NA values in certain columns.
inplace: It's a boolean which makes the changes in data frame itself if True. Always remember when using the inplace=True argument, you're modifying the original DataFrame. If you need to retain the original data for any reason, avoid using inplace=True and instead assign the result to a new DataFrame.
Intuition
We need to use the dropna function to remove rows with missing data in the name column. We can do this by setting the required parameters based on the "Function Argument Definition" section mentioned earlier; here is the breakdown:

We are only considering the name column, so we set subset=['name']. This argument tells dropna to consider only the name column when looking for missing values. So, only rows where the name column has missing values will be dropped.
We need to modify the original DataFrame, so set inplace=True. By setting inplace to True, we're modifying the original students DataFrame directly. If you set it to False (or omitted it), then a new DataFrame with the dropped rows would be returned, and the original students DataFrame would remain unchanged.
students.dropna(subset=['name'], inplace=True)
Visualization of dropna function

fig

When you pass this DataFrame to the function:

student_id	name	age
32	Piper	5
217	Grace	19
779	None	20
849	None	14

It will return:

student_id	name	age
32	Piper	5
217	Grace	19

Implementation

Comments (1)

Sort by:Best
Type comment here... (Markdown supported)
Preview
Comment
💡 Article Commenting Rules
1. This comment section is for questions and comments regarding this LeetCode article. All posts must respect our LeetCode Community Rules.

2. Concerns about errors or bugs in the article, problem description, or test cases should be posted on LeetCode Feedback, so that our team can address them.


mohit-k-verma
LeetCode 75
Oct 07, 2023
Can someone explain why below code doesn't work for this problem?

import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students.loc[students['name'] != None, ['student_id', 'name', 'age']]
"""
