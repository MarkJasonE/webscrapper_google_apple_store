import re
import pandas as pd
import numpy as np


"""
Table of contents:
Section A: Data Wrangling:
  1 - Functions for columns/rows manipulations
  2 - Functions for string manipulations
  3 - Functions for time manipulations

Section B: Data Visualization:
  1 - Functions for pie charts
"""

#~~~~~~~~# Section A: DATA WRANGLING #~~~~~~~~#

###### A-1 COLUMNS/ROWS MANIPULATION ######

#A-1.1 Dropping columns
def drop_col(df, cols):
  df.drop(cols, axis=1, inplace=True)

###### END A-1 COLUMN/ROWS MANIPULATION ######


###### A-2 STRING MANIPULATION ######

#A-2.1 Clean text from additional white space and line breaks "\n"
def clean_txt(df, col):
  df[col].replace(r"\s+|\\n", " ", regex=True, inplace=True)

#A-2.2 Clean time string from upper/lower case and white spaces before converting
def clean_time(df, col):
  df[col] = df[col].str.replace(r"[a-zA-Z ]|\s+", " ", regex=True)

#A-2.4 Process the text data into tokenz

###### END A-2 STRING MANIPULATION ######


###### A-3 TIME MANIPULATION ######

#A-3.1 Convert time into date time after cleaning
def convert_to_datetime(df, col):
  df[col] = pd.to_datetime(df[col])

###### END A-3 TIME MANIPULATION ######

#~~~~~~~~# End Of Section A: DATA WRANGLING #~~~~~~~~#


#~~~~~~~~# Section B: DATA VISUALIZATION #~~~~~~~~#

###### B-1 PIE CHARTS######

#B-1.1 Show percentage and its total number of N from a specified population
def show_pie_val_pct(pct, total_n):
  absolute = int(np.round(pct/100 * np.sum(total_n)))
  return "{:.1f}%\nN={}".format(pct, absolute)

###### END B-1 PIE CHARTS######

#~~~~~~~~# End Of Section B: DATA VISUALIZATION #~~~~~~~~#
