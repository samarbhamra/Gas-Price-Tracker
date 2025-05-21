from etl.extract_transform import extract_and_transform
from etl.load import load_data
from db.db_utils import get_engine, get_session

if __name__ == "__main__":
    FILE_PATH = "/Users/samardeepbhamra/Desktop/Gas Price Tracker/1810000101-eng (1).csv"

    print("📥 Extracting and transforming...")
    df = extract_and_transform(FILE_PATH)

    print("🔗 Connecting to DB...")
    engine = get_engine()
    session = get_session(engine)

    print("📤 Loading into DB...")
    load_data(df, session)

    print("ETL complete.")
