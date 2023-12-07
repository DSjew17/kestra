def export_to_excel():
    df = pd.read_csv('/path/to/transformed_data.csv')
    df.to_excel('/path/to/exported_data.xlsx', index=False)
    print("Data exported to Excel.")