import csv

def read_csv_data(file_path):
    """
    Read csv file
    Args:
        file_path(str): file path
    Returns:
        list: data split row
    """
    result_data = []
    # WRITE YOUR CODE HERE
    data=open('data\weight-height.csv').read()
    result_data=data.split('\n')
    return result_data
file_path='data\weight-height.csv'
read_csv_data(file_path)
    