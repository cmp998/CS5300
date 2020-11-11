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
    #print(df['author'])
    df['author'] = df['author'].str.replace(r"&", ";")
    #df['author'] = df['author'].apply(remove_etal)
    df['author'] = df['author'].apply(name_swap)
    df['author'] = df['author'].str.replace(r"\(.*\)", "")
    df['author'] = df['author'].str.lower()
    #print(df['author'])

def name_swap(name):
    if name is None:
        return "NA"
    elif name.count(';') >= 1:
        names = name.split(';')
        for i in range(len(names)):
            if names[i].count(',') == 1:
                names[i] = names[i].split(',')[1].strip(' ') + " " + names[i].split(',')[0]
        return ",".join(names)
    elif name.count(',') == 1:
        return name.split(',')[1].strip(' ') + " " + name.split(',')[0]
    else:
        return name

#THIS IS DONE WITH THE REPLACE (*) in author
#def remove_etal(name):
#    name = name.replace(r'\(?.*editor.*\)?', "")
    #name = name.replace(r'')

#df['title'] = df['title'].str.replace(r'[^\w\s]','')




def clean_binding(df: pd.DataFrame):
    df['binding'] = df['binding'].str.lower()
    df['binding'] = df['binding'].str.replace("singleissuemagazine", "single issue magazine")
    df['binding'] = df['binding'].str.replace("dust jacket", "")
    df['binding'] = df['binding'].str.replace("with", "")
    df['binding'] = df['binding'].str.strip()
    df['binding'] = df['binding'].str.replace(r"\(.*\)", "")
    df['binding'] = df['binding'].str.replace("hardback", "hardcover")
    df['binding'] = df['binding'].str.replace("hard back", "hardcover")
    df['binding'] = df['binding'].str.replace("hard cover", "hardcover")
    df['binding'] = df['binding'].str.replace("soft cover", "paperback")
    df['binding'] = df['binding'].str.replace("soft back", "paperback")
    df['binding'] = df['binding'].str.replace("softcover", "paperback")
    df['binding'] = df['binding'].str.replace("softback", "paperback")
    df['binding'] = df['binding'].str.replace("mass market paperback", "paperback")
    df['binding'] = df['binding'].apply(binding_pull)
    
    

def binding_pull(binding: str):
    if (binding is np.nan):
        return
    if ("paperback" in binding):
        return "paperback"
    return binding

def clean_publisher(df: pd.DataFrame):
    df['publisher'] = df['publisher'].str.replace(r'[ \?\.,].*', "")
    #print(df['publisher'])

def clean_descr(df: pd.DataFrame):
    df['descr'] = df['descr'].str.replace(r'Bookseller Inventory.*', "")
    #print(df.iloc[17]['descr'])
  

if __name__ == '__main__':
    df = pd.read_csv('inventory.csv')
    pd.set_option('display.max_columns', None)
    #print(df.head())
    clean_title(df)
    clean_author(df)
   
    clean_descr(df)
    clean_publisher(df)
    clean_binding(df)
    df.to_csv('cleaned.csv', index=False)
    
    #making the tables and their info
    