import pandas as pd
import numpy as np

def clean_title(df):
    #title
    df['title'] = df['title'].str.replace(r"\(.*\)", "")
    df['title'] = df['title'].str.lower()
    df['title'] = df['title'].str.replace(r'[^\w\s]','')

    #print(df['title'])
    return

def clean_author(df):
    #author
    print(df['author'])
    df['author'] = df['author'].apply(remove_etal)
    df['author'] = df['author'].apply(name_swap)
    df['author'] = df['author'].str.replace(r"\(.*\)", "")
    df['author'] = df['author'].str.lower()
    print(df['author'])

def name_swap(name):
    if name.count(',') == 1:
        return name.split(',')[1].strip(' ') + " " + name.split(',')[0]
    else:
        return name

def remove_etal(name):
    name = name.replace(r'\(?.*editor.*\)?', "")
    #name = name.replace(r'')

#df['title'] = df['title'].str.replace(r'[^\w\s]','')




#binding
#Publisher
#descr

if __name__ == '__main__':
    df = pd.read_csv('inventory.csv')
    #pd.set_option('display.max_columns', None)
    #print(df.head())
    clean_title(df)
    clean_author(df)