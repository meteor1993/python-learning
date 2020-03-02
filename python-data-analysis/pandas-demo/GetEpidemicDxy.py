import akshare as ak

epidemic_dxy_df = ak.epidemic_dxy(indicator="global")
epidemic_dxy_df.to_excel('epidemic_dxy.xlsx')