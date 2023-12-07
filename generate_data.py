def generate_data():
    num_users = 10000
    fake = Faker()
    data = {
        'User_ID': [f'User_{i}' for i in range(1, num_users + 1)],
        'Name': [fake.name() for _ in range(num_users)],
        'Age': [fake.random_int(min=18, max=65) for _ in range(num_users)],
    }
    df = pd.DataFrame(data)
    df.to_csv('/path/to/generated_data.csv', index=False)
    print(df)
