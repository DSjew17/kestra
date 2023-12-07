def transform_data():
    df = pd.read_csv('/path/to/generated_data.csv')
    df['Age'] = df['Age'] + 1  # Simple transformation, adding 1 to Age
    df.to_csv('/path/to/transformed_data.csv', index=False)
    print("Data transformed and saved.")