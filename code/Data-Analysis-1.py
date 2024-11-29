import pandas as pd

def analyze_deaths_with_age(dataframe):
    """
    Analyzes deaths in a given DataFrame and includes average age for each illness.

    Parameters:
    dataframe (pd.DataFrame): DataFrame with the required columns.

    Returns:
    dict: A dictionary containing the number of deaths, most significant illnesses, and average age per illness.
    """
    # Filter rows where DATE_DIED is not 9999-99-99 and PATIENT_TYPE is 1
    filtered_df = dataframe[(dataframe['DATE_DIED'] != '9999-99-99') & (dataframe['PATIENT_TYPE'] == 1)]

    # Count the number of such rows
    death_count = filtered_df.shape[0]

    # List of illness columns to analyze
    illness_columns = ['INTUBED', 'PNEUMONIA', 'PREGNANT', 'DIABETES', 'COPD',
                       'ASTHMA', 'INMSUPR', 'HIPERTENSION', 'OTHER_DISEASE',
                       'CARDIOVASCULAR', 'OBESITY', 'RENAL_CHRONIC', 'TOBACCO']

    # Initialize dictionary to store illness counts and average age
    illness_stats = []

    for illness in illness_columns:
        # Filter patients with the illness
        illness_patients = filtered_df[filtered_df[illness] == 1]

        # Count the number of patients with this illness
        illness_count = illness_patients.shape[0]

        # Calculate the average age of patients with this illness
        avg_age = illness_patients['AGE'].mean() if illness_count > 0 else None

        # Store results
        illness_stats.append({
            "illness": illness, 
            "count": illness_count,
            "average_age": avg_age
        })
        illness_stats.sort(key=lambda x: x["count"], reverse=True)

    # Return the results
    return {
        "death_count": death_count,
        "illness_stats": illness_stats
    }
