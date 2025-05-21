from prophet import Prophet

def make_forecast(df, periods=180):
    df = df.rename(columns={"date": "ds", "price": "y"})
    model = Prophet()
    model.fit(df)
    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)
    return forecast
