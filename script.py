#%%
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import sqlite3 as sql
import seaborn as sns
sns.set(style='darkgrid')


def dataframedb(csvfile, tablename, dbname, querystring):
    df = pd.read_csv(csvfile)
    df.to_sql(tablename, sql.connect(dbname), if_exists="replace")
    con = sql.connect(dbname)
    return pd.read_sql_query(querystring, con)


#%%
# Federal Funds Dataframe, SQL
fftuple = ("FEDFUNDS.csv",
           "ff_table",
           "ff.db",
           'SELECT STRFTIME("%Y-%m", "DATE") AS FDate, FEDFUNDS FROM ff_table'
           )
ff_df = dataframedb(*fftuple)
#ff_df.dtypes

#%%
# GDP Dataframe, SQL
gdptuple = ("A191RL1Q225SBEA.csv",
            "gdp_table",
            "gdp.db",
            'SELECT STRFTIME("%Y-%m", "DATE") AS FDate, GDP FROM gdp_table WHERE FDate >= "1954-07"'
            )
gdp_df = dataframedb(*gdptuple)
#gdp_df

#%%
# SNP 500 Dataframe, SQL
snp_tuple = ("^GSPC.csv",
             "snp_table",
             "snp.db",
             'SELECT STRFTIME("%Y-%m", Date) AS FDate, MAX(Close) AS maxclose FROM snp_table GROUP BY FDate HAVING FDate >= "1954-07"'
             )
snp_df = dataframedb(*snp_tuple)
# SNP 500 % change month over month
snp_pc_df = pd.DataFrame({
    'FDate': snp_df['FDate'],
    'Percent Change': snp_df['maxclose'].pct_change() * 100
})
snp_pc_df.drop(snp_pc_df.index[0], inplace=True)
#snp_pc_df.dtypes
#%%
# Combine Dataframes
gdp_df.drop(gdp_df.index[0], inplace=True)
ff_df.drop(ff_df.index[0], inplace=True)
combined = pd.concat([snp_pc_df, gdp_df, ff_df], sort=False)
combined['FDate'] = pd.to_datetime(combined['FDate'], infer_datetime_format=True)
df_combined = combined.groupby("FDate").mean()
df_combined['GDP'].bfill(limit=2, inplace=True)
df_combined

#%%
gdp_df['FDate'] = pd.to_datetime(gdp_df['FDate'], infer_datetime_format=True)
#gdp_df
#%%
g = sns.relplot(x="FDate", y="GDP", kind="line", data=gdp_df)
g.fig.autofmt_xdate()
#%%
snp_df['FDate'] = pd.to_datetime(snp_df['FDate'], infer_datetime_format=True)
g = sns.relplot(x="FDate", y="maxclose", kind="line", data=snp_df)
g.fig.autofmt_xdate()
#%%
ff_df['FDate'] = pd.to_datetime(ff_df['FDate'], infer_datetime_format=True)
g = sns.relplot(x='FDate', y='FEDFUNDS', kind="line", data=ff_df)
g.fig.autofmt_xdate()
#%%
snp_pc_df['FDate'] = pd.to_datetime(snp_pc_df['FDate'], infer_datetime_format=True)
g = sns.relplot(x='FDate', y='Percent Change', kind='line', data=snp_pc_df)
g.fig.autofmt_xdate()
#%%
sns.regplot(x='GDP', y='FEDFUNDS', data=df_combined)
#sns.regplot(x='GDP', y='Percent Change', data=df_combined)