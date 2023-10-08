import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    ans= weather.pivot(index='month' , columns='city' , values='temperature')
    return ans





"""
2889. Reshape Data: Pivot
Easy
13
2
Companies
DataFrame weather
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| city        | object |
| month       | object |
| temperature | int    |
+-------------+--------+
Write a solution to pivot the data so that each row represents temperatures for a specific month, and each city is a separate column.

The result format is in the following example.

 

Example 1:
Input:
+--------------+----------+-------------+
| city         | month    | temperature |
+--------------+----------+-------------+
| Jacksonville | January  | 13          |
| Jacksonville | February | 23          |
| Jacksonville | March    | 38          |
| Jacksonville | April    | 5           |
| Jacksonville | May      | 34          |
| ElPaso       | January  | 20          |
| ElPaso       | February | 6           |
| ElPaso       | March    | 26          |
| ElPaso       | April    | 2           |
| ElPaso       | May      | 43          |
+--------------+----------+-------------+
Output:
+----------+--------+--------------+
| month    | ElPaso | Jacksonville |
+----------+--------+--------------+
| April    | 2      | 5            |
| February | 6      | 23           |
| January  | 20     | 13           |
| March    | 26     | 38           |
| May      | 43     | 34           |
+----------+--------+--------------+
Explanation:
The table is pivoted, each column represents a city, and each row represents a specific month.
Accepted
831
Submissions
1K
Acceptance Rate
82.0%
Seen this question in a real interview before?
1/4
Yes
No
Discussion (1)


Solution
Overview
In this solution we focus on how to pivot a DataFrame. Pivoting a table means reshaping it in such a way that you convert a long-format table into a wide-format table. Let's unravel the solution and the usage of the pivot function in detail.

Key Concepts:

pivot Function: The pivot function in pandas is used to reshape data based on column values and get a new DataFrame out of it. pivot takes the following arguments which we will utilize:
index: Determines the rows in the new DataFrame.
columns: Determines the columns in the new DataFrame.
values: Specifies the values to be used when the table is reshaped.
Intuition
Let's break the solution down step by step:

1. Importing pandas:

import pandas as pd
This imports the pandas library and gives it an alias pd. pandas is a fast, powerful, flexible, and easy-to-use open-source data analysis and data manipulation library built on top of the Python programming language.

2. The pivot Function

ans = weather.pivot(index='month', columns='city', values='temperature')
Here's what each argument in the pivot function does:

index: It determines the rows in the new DataFrame. For this example, we use the month column from the original DataFrame as the index, which means our pivoted table will have one row for each unique value in the month column.
columns: It determines the columns in the new DataFrame. Here, we're using the city column, which means our pivoted table will have one column for each unique value in the city column.
values: This argument specifies the values to be used when the table is reshaped. For this example, we use the temperature column from the original DataFrame.
3. Returning the modified DataFrame:

return ans
This line of code returns the pivoted DataFrame.

Using the Solution

Visualization of pivot function

fig

When you pass this DataFrame to the function:

city	month	temperature
Jacksonville	January	13
Jacksonville	February	23
Jacksonville	March	38
Jacksonville	April	5
Jacksonville	May	34
ElPaso	January	20
ElPaso	February	6
ElPaso	March	26
ElPaso	April	2
ElPaso	May	43

It will return:

month	ElPaso	Jacksonville
April	2	5
February	6	23
January	20	13
March	26	38
May	43	34

Notes:

Missing Data: The pivot function does not handle duplicated entries for the same index/column combination. If there are duplicates, you might consider using pivot_table which can aggregate over duplicate entries.
Data Type: As per the table given, the city and month columns are of "object" data type which is equivalent to string type in pandas, while temperature is of integer type.
Order: The output may not necessarily be in the same order as in the example (i.e., January to May). If you want it in a specific order, you'd have to sort it after pivoting.
Complete Sample Solution with Sorting:

import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    ans = weather.pivot(index='month', columns='city', values='temperature')
    month_order = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    ans = ans.reindex(month_order)
    return ans
In this solution, after pivoting, the DataFrame is sorted based on the predefined order of months. The resulting DataFrame would be:

month	ElPaso	Jacksonville
January	20	13
February	6	23
March	26	38
April	2	5
May	43	34

Implementation

Comments (0)

Sort by:Best

"""
