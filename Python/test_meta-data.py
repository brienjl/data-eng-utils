import pandas as pd

def test_compare_column_names():
    # Test case 1: All data frames have the same column names
    df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    df2 = pd.DataFrame({'A': [7, 8, 9], 'B': [10, 11, 12]})
    df3 = pd.DataFrame({'A': [13, 14, 15], 'B': [16, 17, 18]})
    data_frames = {'df1': df1, 'df2': df2, 'df3': df3}
    compare_column_names(data_frames)  # Expected output: "All data frames have the same column names."

    # Test case 2: Not all data frames have the same column names
    df4 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    df5 = pd.DataFrame({'A': [7, 8, 9], 'C': [10, 11, 12]})
    df6 = pd.DataFrame({'A': [13, 14, 15], 'B': [16, 17, 18]})
    data_frames = {'df4': df4, 'df5': df5, 'df6': df6}
    compare_column_names(data_frames)  # Expected output: "Not all data frames have the same column names."

    # Test case 3: Mismatched columns in one data frame
    df7 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    df8 = pd.DataFrame({'A': [7, 8, 9], 'B': [10, 11, 12]})
    df9 = pd.DataFrame({'A': [13, 14, 15], 'C': [16, 17, 18]})
    data_frames = {'df7': df7, 'df8': df8, 'df9': df9}
    compare_column_names(data_frames)  # Expected output: "Columns in df9 that do not match:\nIndex(['C'], dtype='object')"

test_compare_column_names()import pandas as pd

def test_compare_column_names():
    # Test case 1: All data frames have the same column names
    df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    df2 = pd.DataFrame({'A': [7, 8, 9], 'B': [10, 11, 12]})
    df3 = pd.DataFrame({'A': [13, 14, 15], 'B': [16, 17, 18]})
    data_frames = {'df1': df1, 'df2': df2, 'df3': df3}
    compare_column_names(data_frames)  # Expected output: "All data frames have the same column names."

    # Test case 2: Not all data frames have the same column names
    df4 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    df5 = pd.DataFrame({'A': [7, 8, 9], 'C': [10, 11, 12]})
    df6 = pd.DataFrame({'A': [13, 14, 15], 'B': [16, 17, 18]})
    data_frames = {'df4': df4, 'df5': df5, 'df6': df6}
    compare_column_names(data_frames)  # Expected output: "Not all data frames have the same column names."

    # Test case 3: Mismatched columns in one data frame
    df7 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    df8 = pd.DataFrame({'A': [7, 8, 9], 'B': [10, 11, 12]})
    df9 = pd.DataFrame({'A': [13, 14, 15], 'C': [16, 17, 18]})
    data_frames = {'df7': df7, 'df8': df8, 'df9': df9}
    compare_column_names(data_frames)  # Expected output: "Columns in df9 that do not match:\nIndex(['C'], dtype='object')"

test_compare_column_names()