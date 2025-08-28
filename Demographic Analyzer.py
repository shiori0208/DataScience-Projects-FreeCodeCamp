# How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
race_count = df.groupby('race')
race_count['race'].count()


# What is the average age of men?
average_age_men = df[df['sex'] == 'Male']['age'].mean()

# What is the percentage of people who have a Bachelor's degree?
percentage_bachelors = df[df['education'] == 'Bachelors'].shape[0] / df.shape[0] * 100

# What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
# What percentage of people without advanced education make more than 50K?

# with and without `Bachelors`, `Masters`, or `Doctorate`
higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

# percentage with salary >50K
higher_education_rich = higher_education[higher_education['salary'] == '>50K']['salary'].count() / higher_education.shape[0] * 100

lower_education_rich = lower_education[lower_education['salary'] == '<50K']['salary'].count() / lower_education.shape[0] * 100

# What is the minimum number of hours a person works per week (hours-per-week feature)?
min_work_hours = df['hours-per-week'].min()

# What percentage of the people who work the minimum number of hours per week have a salary of >50K?
num_min_workers = df[df['hours-per-week'] == 1]['hours-per-week'].count()

rich_percentage = df[(df['hours-per-week'] == 1) & (df['salary'] == '>50K')].shape[0] / num_min_workers

# What country has the highest percentage of people that earn >50K?
highest_earning_country = df[df['salary'] == '>50K'].groupby('native-country')['native-country'].count().max()

highest_earning_country_percentage = (highest_earning_country / df.groupby('native-country')['native-country'].count()).max()

# Identify the most popular occupation for those who earn >50K in India.
top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')].groupby('occupation')['occupation'].count().max()
