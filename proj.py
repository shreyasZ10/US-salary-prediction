import glassdoor_scrapper as gs
import pandas as pd

path = "C:/Users/SHREYAS/Desktop/project/chromedriver"

df = gs.get_jobs('data scientist', 1000, False, path, 15)
df.to_csv('salary.csv')
