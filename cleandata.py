import pandas as pd
import numpy as np

file_path = "C:\\Users\\Kirbs\\Desktop\\BSIT_3A\\LAURENTE_DASHB\\PHL_GATS_2021_Public_use_16NOV2023.csv"
df = pd.read_csv(file_path, low_memory=False)


df.columns = df.columns.str.strip().str.upper()


df_cessation = df[df['D01'] == 1].copy()


df_cessation['Gender'] = df_cessation['A01'].map({1: 'Male', 2: 'Female'})
df_cessation['Residence'] = df_cessation['RESIDENCE'].map({1: 'Urban', 2: 'Rural'})


duration_map = {1: 'Months', 2: 'Weeks', 3: 'Days', 4: 'Less than 24 hrs'}
df_cessation['Success_Unit'] = df_cessation['D02A'].map(duration_map)


method_map = {1: 'Yes', 2: 'No'}
df_cessation['Counseling'] = df_cessation['D03A'].map(method_map)
df_cessation['NRT_Usage'] = df_cessation['D03B'].map(method_map)
df_cessation['Quit_Alone'] = df_cessation['D03K'].map(method_map)


df_cessation['Age'] = pd.to_numeric(df_cessation['AGE'], errors='coerce')


final_cols = ['Gender', 'Residence', 'Age', 'Success_Unit', 'Counseling', 'NRT_Usage', 'Quit_Alone']
cleaned_df = df_cessation[final_cols].dropna(subset=['Success_Unit'])


cleaned_df.to_csv("C:\\Users\\Kirbs\\Desktop\\BSIT_3A\\LAURENTE_DASHB\\cleaned_cessation_data.csv", index=False)
print("Success! Cleaned file saved as 'cleaned_cessation_data.csv'")