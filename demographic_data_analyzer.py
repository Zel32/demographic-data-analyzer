import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')
    total_population = len(df)
    
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()
    
    # What is the average age of men?
    male_df = df[df['sex'] == 'Male']
    average_age_men = round(male_df['age'].mean(),1)

    # What is the percentage of people who have a Bachelor's degree?
    count_bachelors = (df['education'] == 'Bachelors').sum()

    percentage_bachelors = count_bachelors/total_population * 100
    percentage_bachelors = round(percentage_bachelors,1)
    
    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education_df = df[((df["education"]=='Bachelors') |
                                      (df["education"]=='Masters') | 
                                      (df["education"]=='Doctorate'))]
    higher_education = len(higher_education_df)

    lower_education_df = df[((df["education"]!='Bachelors') &
                                      (df["education"]!='Masters') &
                                      (df["education"]!='Doctorate'))]
    lower_education = len(lower_education_df)

    # percentage with salary >50K
    higher_education_rich = round(len(higher_education_df[higher_education_df["salary"]=='>50K'])/higher_education * 100,1)
    lower_education_rich = round(len(lower_education_df[lower_education_df["salary"]=='>50K'])/lower_education * 100,1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df["hours-per-week"].min()
    
    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    df_min_workers = df[(df["hours-per-week"]==min_work_hours)]
    num_min_workers = len(df_min_workers)

    rich_min_workers = len(df_min_workers[(df_min_workers["salary"]=='>50K')])
    rich_percentage = round(rich_min_workers/num_min_workers * 100,1)

    # What country has the highest percentage of people that earn >50K?
    population_country = df["native-country"].value_counts()
    df_rich = df[(df["salary"]=='>50K')]
    rich_per_country = df_rich["native-country"].value_counts()

    rich_percentage_country = round(rich_per_country.divide(population_country, fill_value=0) * 100,1)
    highest_earning_country = rich_percentage_country.idxmax()
    highest_earning_country_percentage = round(rich_percentage_country.max(), 1)

    
    # Identify the most popular occupation for those who earn >50K in India.
    df_india_rich = df[(df["native-country"]=='India') & (df["salary"]=='>50K')]

    india_occupation_rich = df_india_rich["occupation"].value_counts()
    top_IN_occupation = india_occupation_rich.idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
