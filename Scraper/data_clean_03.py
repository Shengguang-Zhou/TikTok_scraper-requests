import pandas as pd


# csv to list
def csv_to_list(filename):
    # Read the CSV file
    df = pd.read_csv(filename)
    # Extract the first column and convert it to a list
    user_list = df.iloc[:, 0].tolist()
    return user_list



