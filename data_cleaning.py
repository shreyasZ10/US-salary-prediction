import pandas as pd

df = pd.read_csv('salary.csv')

## Salary Parsing
df['Hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df.Hourly.value_counts()

df['Employer Provided Salary'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary:' in x.lower() else 0)
df['Employer Provided Salary'].value_counts()

df = df[df['Salary Estimate'] != '-1']
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
minusk_d = salary.apply(lambda x: x.replace('K','').replace('$',''))
minus_hr = minusk_d.apply(lambda x: x.lower().replace('per hour','').replace('employer provided salary:',''))

df['min_salary'] = minus_hr.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = minus_hr.apply(lambda x: int(x.split('-')[1]))
df['avg_salary'] = (df.min_salary + df.max_salary)/2

## Company Name
df['Company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating'] < 0 else x['Company Name'][:-3], axis = 1)

## Specify State
df['job_state'] = df['Location'].apply(lambda x: x.split(',')[1])
df.job_state.value_counts()
df['same_state'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis = 1)
df.same_state.value_counts()

## Age of Company
df['age'] = df['Founded'].apply(lambda x: x if x < 0 else 2020 - x)

#python
df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
 
#r studio 
df['R_yn'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() or 'r-studio' in x.lower() else 0)
df.R_yn.value_counts()

#spark 
df['spark'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
df.spark.value_counts()

#aws 
df['aws'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
df.aws.value_counts()

#excel
df['excel'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)
df.excel.value_counts()

#Tableau
df['tableau'] = df['Job Description'].apply(lambda x: 1 if 'tableau' in x.lower() else 0)
df.tableau.value_counts()

#power bi
df['power bi'] = df['Job Description'].apply(lambda x: 1 if 'power bi' in x.lower() else 0)
df['power bi'].value_counts()

#ml
df['ml'] = df['Job Description'].apply(lambda x: 1 if 'machine learning' in x.lower() else 0)
df['ml'].value_counts()

#deep learning
df['dl'] = df['Job Description'].apply(lambda x: 1 if 'deep learning' in x.lower() else 0)
df.dl.value_counts()

def title_simplifier(title):
    if 'data scientist' in title.lower():
        return 'data scientist'
    elif 'data engineer' in title.lower():
        return 'data engineer'
    elif 'analyst' in title.lower():
        return 'analyst'
    elif 'machine learning' in title.lower():
        return 'mle'
    elif 'manager' in title.lower():
        return 'manager'
    elif 'director' in title.lower():
        return 'director'
    else:
        return 'na'
    
def seniority(title):
    if 'sr' in title.lower() or 'senior' in title.lower() or 'sr' in title.lower() or 'lead' in title.lower() or 'principal' in title.lower():
            return 'senior'
    elif 'jr' in title.lower() or 'jr.' in title.lower():
        return 'jr'
    else:
        return 'na'

df['job_sim'] = df['Job Title'].apply(title_simplifier)
df.job_sim.value_counts()

df['seniority'] = df['Job Title'].apply(seniority)
df.seniority.value_counts()

df['min_salary'] = df.apply(lambda x: x.min_salary*2 if x.Hourly ==1 else x.min_salary, axis =1)
df['max_salary'] = df.apply(lambda x: x.max_salary*2 if x.Hourly ==1 else x.max_salary, axis =1)

df_out = df

df_out.to_csv('dataset.csv', index = False)
