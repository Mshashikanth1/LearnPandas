import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products['quantity'].fillna(0,inplace=True)
    return products
    


"""
2887. Fill Missing Data
Easy
10
1
Companies
DataFrame products
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| name        | object |
| quantity    | int    |
| price       | int    |
+-------------+--------+
Write a solution to fill in the missing value as 0 in the quantity column.

The result format is in the following example.

 

Example 1:
Input:+-----------------+----------+-------+
| name            | quantity | price |
+-----------------+----------+-------+
| Wristwatch      | 32       | 135   |
| WirelessEarbuds | None     | 821   |
| GolfClubs       | None     | 9319  |
| Printer         | 849      | 3051  |
+-----------------+----------+-------+
Output:
+-----------------+----------+-------+
| name            | quantity | price |
+-----------------+----------+-------+
| Wristwatch      | 32       | 135   |
| WirelessEarbuds | 0        | 821   |
| GolfClubs       | 0        | 9319  |
| Printer         | 849      | 3051  |
+-----------------+----------+-------+
Explanation: 
The quantity for Toaster and Headphones are filled by 0.
Accepted
1.2K
Submissions
1.4K
Acceptance Rate
88.8%
Seen this question in a real interview before?
1/4
Yes
No
Discussion (0)


Solution
Overview
In this problem, we have a DataFrame named products that contains product data. However, some of the quantity data is missing. The goal is to fill the missing quantity data with the value of 0.

Key Concepts:

DataFrame: a 2D table-like structure, similar to a spreadsheet or SQL table. Each row represents an individual record and each column represents a different attribute. It is size-mutable designed to handle a mix of different types of data.
fillna Function: fillna is a function in the pandas library, used primarily with pandas Series and DataFrame objects. It allows you to fill NA/NaN values using specified methods. In this context, we are using it to replace the None (or NaN in the usual dataframe representation) values.
fillna Function Argument Definition:

The fillna function has several arguments that you can utilize, but we'll focus on the most commonly used ones:

value: Scalar, dict, Series, or DataFrame. The value to use to fill holes (e.g. 0). This is what we use in our solution.

method: {‘backfill’, ‘bfill’, ‘pad’, ‘ffill’, None}. Method to use for filling holes in reindexed Series. Default is None.

axis: {0 or ‘index’, 1 or ‘columns’}. Axis along which to fill missing values.

inplace: Bool. If True, fills in place. Note: this will modify any other views on this object. Default is False.

Intuition
In our solution, we use:

products['quantity'].fillna(0, inplace=True)
Since we are trying to fill missing data from the quantity column of the products DataFrame, we apply the fillna function to products['quantity'].
Since we want to replace missing values (NaN or None) with 0, we use the value argument as 0.
Finally, we want to return the original DataFrame, so we set inplace=True to modify the original DataFrame directly without returning a new one. Note that if you don't use inplace=True, you would have to capture the result like this: products = products['quantity'].fillna(0)
Visualization of fillna function

fig

When you pass the following DataFrame to this function:

name	quantity	price
Wristwatch	32	135
WirelessEarbuds	None	821
GolfClubs	None	9319
Printer	849	3051

It will return:

name	quantity	price
Wristwatch	32	135
WirelessEarbuds	0	821
GolfClubs	0	9319
Printer	849	3051

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
