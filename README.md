# US Salary Prediction



1) This is basically a web application used to predict the average annual salary of data scientist in United states.

2) Initially data for this web application was scrapped through glassdoor website by selenium.

I scrapped almost 1000 data scientist jobs.

3) Next step was to clean the data which was scrapped.

Major challenge was to derive new features from existing ones so that they  can have more impact on the results.

4) Then was the step to derive interesting insights from the cleaned data.

see what features have more impact than rest of them.
for this i used some basic histogram, barplots, pivot tables, etc.
Results can be found in edaexploration.py

5) Then assembled all the important features for the model to be prepared.

Model generation can be found in models.py.

6) For making an api i opted for flask framework.

As it is very quick to make and deploy

7) Finally deployed the flask app to heroku.

The link regarding the same can be found below.

https://us-salary-predictor.herokuapp.com/
