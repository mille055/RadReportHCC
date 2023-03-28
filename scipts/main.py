## library imports
import re
from openpyxl import load_workbook
import pandas as pd
import numpy as np
import nltk
from nltk.tokenize import sent_tokenize

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, classification_report, recall_score
from sklearn import metrics

## local imports
from config import *
from utils import *

## read in data
df = pd.read_excel(file_name)
column_list = df.columns

processed_df = Process_frame(df)
print(processed_df.head())
print(processed_df.columns)

y_true = processed_df.Adenoma
y_true = y_true.fillna(0)
y_pred = processed_df.Auto_Adenoma
y_pred = y_pred.fillna(0)

compare_single(y_true, y_pred)



