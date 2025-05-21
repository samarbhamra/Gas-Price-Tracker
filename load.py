from db.models import GasPrice

def load_data(df, session):
    for _, row in df.iterrows():
        record = GasPrice(
            city=row['City'],
            province=row['Province'],
            date=row['Date'],
            price=row['Price']
        )
        session.add(record)
    session.commit()
