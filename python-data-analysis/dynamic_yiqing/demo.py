import akshare as ak
covid_19_history_df = ak.covid_19_history()
covid_19_history_df.to_csv('data.csv')
print(covid_19_history_df)