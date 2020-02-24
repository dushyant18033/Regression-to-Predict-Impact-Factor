P&S ASSIGNMENT 2
Date: 26-03-2019
Name: DUSHYANT PANCHAL
Roll No.: 2018033
Section & Group: A7

#THE PROBLEM AND MY APPROACH
->The problem given is to find the regression line for Impact Factors as Y(dependent variable or the output variable) using some of the inputs if not all from the dataset which
 would best fit with the data. In my case I'll be approaching this problem using a brute-force-like method, where-in every possible combination will be checked and compared to
 find the best possible solution for our problem.

->Checking for string based entities like Type(=journal for all entries), SJR Best Quartile, Country, Publisher name, Category or Journal title
 won't be reasonable for such a small training dataset, so I'm leaving them.
 Issn has multiple values for a given journal which are mostly too far. This will also pose a problem with linear regression, so leaving it as well.
 After eliminating all these, I have 11 input parameters and I'll have to select 1 or more of these which give me best possible results.


#ABOUT PYTHON SCRIPT FILES
->FilterData.py takes data from JournalDataFromFound_TXT.xlsx and matches with data available in DownloadedDataAsExcel.xlsx to form a new file called FilteredData.xlsx with only the required columns in it.

->MainScript.py takes the filtered data from file FilteredData.xlsx taking Impact Factors list as Y. Now it forms 2^11-1 combinations which covers all possible combinations
  of the 11 remaining columns as Xi, obviously except for the case when none is selected, finds the regression line for first 80% of the data, then tests it with the remaining 20%
  of data to determine the mean squared error and mean absolute error between Y actual and Y predicted. Then it stores the results in a file called "Regression Analysis.xlsx"
  in the format as was instructed.

->Since lots of calculation is involved, the scripts take a little bit of time to execute. So the user is please requested to be patient.

->Output of the MainScript.py file:-

E:\IIITD works\Sem 2\P&S\2018033_Dushyant_P&S_Assignment2>python MainScript.py
Combination giving least Mean Squared Error:-

SJR, Total Cites (3years), Cites / Doc. (2years), Ref. / Doc.
(Mean Squared Error: 0.07097667431233622)
(Mean Absolute Error: 0.1808821975238447)

Combination giving least Mean Absolute Error:-

SJR, Total Docs. (2017), Total Refs., Total Cites (3years), Citable Docs. (3years), Cites / Doc. (2years), Ref. / Doc., Source ID
(Mean Squared Error: 0.07640856387205447)
(Mean Absolute Error: 0.17489689115901788)
