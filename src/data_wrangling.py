# Libraries
import pandas as pd

def clients_groups_file():
    '''Function to load and preprocess the clients group data.'''

    # Load the data
    clients_groups = pd.read_csv("data/import/df_final_experiment_clients.txt")

    # Fill NaN values in 'Variation' column
    clients_groups['Variation'] = clients_groups['Variation'].fillna('Non-participant')

    # Export the processed data to CSV
    clients_groups.to_csv("data/export/clients_groups.csv", index=False)
    
    return clients_groups

def clients_demo_file():
    '''Load and preprocess the clients demographic data.'''

    # Load the demographic data
    clients_demo = pd.read_csv("data/import/df_final_demo.txt")

    # Load the clients group data
    clients_groups = clients_groups_file()

    # Merge the demographic data with the clients group data
    clients_demo = clients_demo.merge(clients_groups, on='client_id', how='left')

    # Remove non-participants
    clients_demo = clients_demo[clients_demo['Variation'] != 'Non-participant']

    # Handle missing values in gendr column
    clients_demo['gendr'] = clients_demo['gendr'].fillna('U')

    # Fill missing values in float64 columns with the median
    for col in clients_demo.select_dtypes(include=['float64']).columns:
        clients_demo[col] = clients_demo[col].fillna(clients_demo[col].median())

    # Export the cleaned demographic data to CSV
    clients_demo.to_csv("data/export/clients_demo.csv", index=False)
    
    return clients_demo

def testing_results_file():
    '''
    This function:
    1. Imports and merges the two parts of the web data results file.
    2. Does the necessary data type conversions.
    '''

    # Load the clients group data
    clients_groups = clients_groups_file()

    # Importing the two parts of the web data results files
    results_pt1 = pd.read_csv("data/import/df_final_web_data_pt_1.txt")
    results_pt2 = pd.read_csv("data/import/df_final_web_data_pt_2.txt")

    # Merging the two parts into a single dataframe
    results = pd.concat([results_pt1, results_pt2], ignore_index=True)

    # Merge the results data with the clients group data
    results = results.merge(clients_groups, on='client_id', how='left')
    
    # Remove non-participants
    results = results[results['Variation'] != 'Non-participant']

    # Converting the 'date_time' column to datetime format
    results['date_time'] = pd.to_datetime(results['date_time'])

    # Exporting the cleaned dataframe to a CSV file
    results.to_csv("data/export/testing_results.csv", index=False)

    return results