import pandas as pd

def extract_and_transform(file_path):
    df_raw = pd.read_csv(file_path, skiprows=8)
    df_raw = df_raw.drop(index=0).reset_index(drop=True)
    df_raw.rename(columns={df_raw.columns[0]: "Geography"}, inplace=True)

    df_long = df_raw.melt(id_vars=["Geography"], var_name="Date", value_name="Price")

    df_long["Geography"] = df_long["Geography"].str.replace('"', '')
    df_long["Date"] = df_long["Date"].str.replace('"', '')

    df_long["Price"] = pd.to_numeric(df_long["Price"], errors="coerce")
    df_long["Date"] = pd.to_datetime("1 " + df_long["Date"], format="%d %B %Y")

    geo_split = df_long["Geography"].str.extract(r"^(.*?),\s*(.*?)$")
    df_long["City"] = geo_split[0]
    df_long["Province"] = geo_split[1]

    df_long.dropna(subset=["City", "Province", "Date", "Price"], inplace=True)

    return df_long[["City", "Province", "Date", "Price"]]
