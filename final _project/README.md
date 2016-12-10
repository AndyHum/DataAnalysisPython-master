Project Title:

This is for the final project of Data Analysis in Python. This project is to analyze the earning of citizens in Boston from 2012 to 2015 and the number of incident in Boston from 2012 to 2015
Data Collection:
The data is from Opendata of Boston. Use request API to download the json file and transfer it to dataframe and store it in csv files. There are total 5 csv files download from the Internet.



Analysis One:

The first the analysis of the datasets is to get the Crime Incident Reports.csv file and make an analysis to see the date it begins and the date it ends.  There are 1129 days recorded in the dataset.   And the incidents are divided into 127 different types to be recorded. I break them up and store them with their dates and types in different folders. If someone wants to check the record, it will be easy for him to get in the folder he wants.
 
 
Analysis Two:

Analysis 2 is to analyze the change of Boston citizens from 2012 to 2015. Read all 4 csv files to get all the citizens¡¯ earning and calculate the average earning of them each year. Then use seaborn to draw a barplot to describe the change of Boston citizens¡¯ earning over the years.
 
It seems that there is almost no change between 2012 and 2013, but after that. The earning seems to raise fast. It seems that the earning will go raise in the future.


Analysis Three:

Analysis 3¡¯s goal is same as analysis 2 in some ways. Analysis 3 is to find out the change of numbers of incidents in these 4 years. Read the data from csv file and divide it by their data. Finally, get the barplot of change between years.
 
It seems that the incidents happened between 2013 and 2014 is almost the twice compared with the other 2 years. In 2014, It reaches the highest value 88058. Then rush down quickly to 49760.


Analysis Four:

Because of the high amount of incidents, I want to find whether there is a relation between the earning of citizens and amount of incidents, so I list the earning and incidents in the same barplot to look for the relationship.
 
But just with the number, I cannot find anything that help me to relate them up, so I choose the use rate to find something else. I check out the increasing of earning each year and compare with the amount of incidents.
 
It seems that because of the decreasing of earning in 2013, more incident happened in Boston. Although the earning almost raises back a lot the incidents did not decrease because the problem last year left. Finally in 2015 the earning keep increasing so the incidents finally come down.


Analysis Five:

Analysis 5 is to see the change rate both earning and incidents and I try to make a pre-exploration to find the change in the future
 
It seems that although there are 2 years¡¯ increasing earning. There may be a possibility that the earning decrease a little. In 2016, the average earning may be between 60000 to 77500. And the incidents may be between 20000 to 200000. Because the data is too small. There prediction may be not reliable.

To clone this repo use


git clone
git@github.com:AndyHum/DataAnalysisPython-master.git
