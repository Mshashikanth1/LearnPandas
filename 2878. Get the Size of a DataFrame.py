import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return [players.shape[0], players.shape[1]]
    



"""
2878. Get the Size of a DataFrame
Easy
12
2
Companies
DataFrame players:
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| player_id   | int    |
| name        | object |
| age         | int    |
| position    | object |
| ...         | ...    |
+-------------+--------+
Write a solution to calculate and display the number of rows and columns of players.

Return the result as an array:

[number of rows, number of columns]

The result format is in the following example.

 

Example 1:

Input:
+-----------+----------+-----+-------------+--------------------+
| player_id | name     | age | position    | team               |
+-----------+----------+-----+-------------+--------------------+
| 846       | Mason    | 21  | Forward     | RealMadrid         |
| 749       | Riley    | 30  | Winger      | Barcelona          |
| 155       | Bob      | 28  | Striker     | ManchesterUnited   |
| 583       | Isabella | 32  | Goalkeeper  | Liverpool          |
| 388       | Zachary  | 24  | Midfielder  | BayernMunich       |
| 883       | Ava      | 23  | Defender    | Chelsea            |
| 355       | Violet   | 18  | Striker     | Juventus           |
| 247       | Thomas   | 27  | Striker     | ParisSaint-Germain |
| 761       | Jack     | 33  | Midfielder  | ManchesterCity     |
| 642       | Charlie  | 36  | Center-back | Arsenal            |
+-----------+----------+-----+-------------+--------------------+
Output:
[10, 5]
Explanation:
This DataFrame contains 10 rows and 5 columns.
Accepted
1.8K
Submissions
2.1K
Acceptance Rate


Overview
This problem requires us to return the number of rows and columns present in the players DataFrame.

Key Concepts:

Attribute: In Python's pandas library, an attribute refers to a property or characteristic of an object that helps describe the object's state or its meta-information. Attributes in pandas are used to access various properties of DataFrame or Series objects, allowing users to retrieve meta-information or underlying data without performing a computation or causing side effects.
shape attribute: Returns the dimensions of the DataFrame or Series in the form of a tuple (rows, columns).
Inuition
Here's a step-by-step breakdown of the solution:

1. Importing the Required Library:

import pandas as pd
We first need to import the pandas library, which is a powerful tool in Python for data manipulation and analysis.
2. Defining the function:

def getDataframeSize(players: pd.DataFrame) -> List:
This line defines a new function named getDataframeSize which takes a DataFrame players as an input argument and returns a list that contains the number of rows and columns in the DataFrame players.
3. Using the shape attribute:

Every DataFrame in pandas has a shape attribute. When you call it, it returns a tuple (number of rows, number of columns). In our case, for the given players DataFrame, the shape would be (10, 5) because there are 10 players and 5 attributes for each player.
4. The Function:

return [players.shape[0], players.shape[1]]
players.shape[0] gives the number of rows in the DataFrame players.
players.shape[1] gives the number of columns in the DataFrame players.
This line thus returns a list containing these two values: [players.shape[0], players.shape[1]].
Using the Solution

Visualization of shape attribute

fig

When you pass this DataFrame to the function:

player_id	name	age	position	team
846	Mason	21	Forward	RealMadrid
749	Riley	30	Winger	Barcelona
155	Bob	28	Striker	ManchesterUnited
583	Isabella	32	Goalkeeper	Liverpool
388	Zachary	24	Midfielder	BayernMunich
883	Ava	23	Defender	Chelsea
355	Violet	18	Striker	Juventus
247	Thomas	27	Striker	ParisSaint-Germain
761	Jack	33	Midfielder	ManchesterCity
642	Charlie	36	Center-back	Arsenal

It will return:

[10, 5]
Implementation

Comments (0)



"""
