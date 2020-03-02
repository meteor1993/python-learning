import akshare as ak

epidemic_history_df = ak.epidemic_history()
epidemic_history_df.to_excel('epidemic_history.xlsx')