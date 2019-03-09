#%%
import pandas as pd
import sqlite3 as sql
import seaborn as sb


def dataframedb(csvfile, tablename, dbname, querystring):
    df = pd.read_csv(csvfile)
    df.to_sql(tablename, sql.connect(dbname), if_exists="replace")
    con = sql.connect(dbname)
    return pd.read_sql_query(querystring, con)


#%%
ff_file = "FEDFUNDS.csv"
query = 'SELECT STRFTIME("%Y-%m", "DATE") AS FDate, FEDFUNDS FROM ff_table'
fftablename = "ff_table"
ffdbname = "ff.db"
ff_df = dataframedb(ff_file, fftablename, ffdbname, query)
ff_df

#%%
gdp_file = "A191RL1Q225SBEA.csv"
gdp_df = pd.read_csv(gdp_file)
gdp_df.to_sql("gdp_table", sql.connect("gdp.db"), if_exists="replace")
congdp = sql.connect("gdp.db")
gdp_df = pd.read_sql_query('SELECT STRFTIME("%Y-%m", "DATE") AS FDate, GDP FROM gdp_table WHERE FDate >= "1954-07"', congdp)
#gdp_df

#%%
snp_file = "^GSPC.csv"
snp_df = pd.read_csv(snp_file)
snp_df.to_sql("snp_table", sql.connect("snp.db"), if_exists="replace")
consnp = sql.connect("snp.db")
snp_df = pd.read_sql_query('SELECT STRFTIME("%Y-%m", Date) AS FDate, MAX(Close) AS maxclose FROM snp_table GROUP BY FDate HAVING FDate >= "1954-07"', consnp)
#snp_df