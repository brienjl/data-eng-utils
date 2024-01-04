
def compare_column_names(data_frames):
    """
    Compare the column names of multiple data frames.

    Args:
        data_frames (dict): A dictionary of data frames.

    Returns:
        None: This function does not return anything. It prints the comparison results.

    """
    column_names = [df.columns for df in data_frames.values()]
    all_columns_same = all(names.equals(column_names[0]) for names in column_names)

    if all_columns_same:
        print("All data frames have the same column names.")
    else:
        print("Not all data frames have the same column names.")
        for i, names in enumerate(column_names):
            if not names.equals(column_names[0]):
                mismatched_columns = names[~names.isin(column_names[0])]
                print(f"Columns in {list(data_frames.keys())[i]} that do not match:")
                print(mismatched_columns)
                print()