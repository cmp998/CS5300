import pandas as pd
import numpy as np
import csv

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
    df['author'] = df['author'].str.lower()
    df['author'] = df['author'].str.replace(r"&", ";")
    df['author'] = df['author'].str.replace(r", -,?", ",")
    df['author'] = df['author'].str.replace(r" and ", "")
    df['author'] = df['author'].str.replace(r". - ", ";")
    df['author'] = df['author'].apply(remove_etal)
    df['author'] = df['author'].apply(name_swap)
    df['author'] = df['author'].str.replace(r"\(.*\).*", "")
    df['author'] = df['author'].str.replace(r"  ", " ")
    df['author'] = df['author'].str.replace(r",? et[.?] al[.?]", "")
    df['author'] = df['author'].str.replace(r", e.a.", "")
    df['author'] = df['author'].str.replace(r" .ed", "")
    df['author'] = df['author'].str.replace(r", et al.", "")
    df['author'] = df['author'].str.strip()
    #print(df['author'])

def name_swap(name):
    if name is None:
        return "NA"
    #Mutliple authors ; sep
    elif name.count(';') >= 1:
        names = name.split(';')
        for i in range(len(names)):
            #Check if individual author is L,F
            if names[i].count(',') == 1:
                names[i] = names[i].split(',')[1].strip(' ') + " " + names[i].split(',')[0]
        return ",".join(names)
    #Single author , sep
    elif name.count(',') == 1 and len(name.split(',')[0].split(" ")) == 1:
        return name.split(',')[1].strip(' ') + " " + name.split(',')[0]
    #multiple author , sep and lastname firstname order
    elif name.count(',') > 1 and name.count(',') % 2:
        names = name.split(',')
        counter = 0
        fixed_names = []
        while counter < len(names):
            fixed_names.append(names[counter + 1].strip() + " " + names[counter].strip())
            counter += 2
        return ",".join(fixed_names)
    else:
        return name

#THIS IS DONE WITH THE REPLACE (*) in author
def remove_etal(name):
    name = name.replace(r"\(.*\)", "")
    name = name.replace(r"etc", "")
    #name = name.replace(r'')
    return name

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
    df['descr'] = df['descr'].str.replace(r'Ask Seller a Question.*', "")
    df['descr'] = df['descr'].str.strip()
    #print(df.iloc[17]['descr'])
  

if __name__ == '__main__':
    pd.set_option('precision', 0)
    df = pd.read_csv('inventory.csv')
    df = df.fillna('0')
    df['isbn13'] = df['isbn13'].astype(int)
    #print(len(df['title'][767]))
    # Problems, Data too long to fit into an int
    # Duplicate BookID keys
    df['copyID'] - df['copyID'].astype('int64')
    
    pd.set_option('display.max_columns', None)
    #print(df.head())
    clean_title(df)
    clean_author(df)
   
    clean_descr(df)
    clean_publisher(df)
    clean_binding(df)
    df.to_csv('cleaned.csv')


    # book info
    book_info = {}
    for ind in df.index:
        title = df['title'][ind]
        if title not in book_info.keys():  
            book_info[title] = [ind, df['publisher'][ind], df['pubdate'][ind], df['isbn10'][ind], df['isbn13'][ind]]
        else:
            if book_info[title][1] == np.nan:
                book_info[title][1] = df['publisher'][ind]
            if book_info[title][2] == np.nan:
                book_info[title][2] = df['pubdate'][ind]
            if book_info[title][3] == np.nan:
                book_info[title][3] = df['isbn10'][ind]
            if book_info[title][4] == np.nan:
                book_info[title][4] = df['isnb13'][ind]
    
    with open('bookinfo.csv', 'w') as csvfile:
        write = csv.writer(csvfile)
        write.writerow(['bookid', 'title', 'publisher', 'pubdate', 'isbn10', 'isbn13'])
        for title in book_info:
            write.writerow([book_info[title][0], title, book_info[title][1], book_info[title][2], book_info[title][3], book_info[title][4]])

    book_copies = {}
    for ind in df.index:
       
       copyID = df['copyID'][ind]
       bookID = book_info[df['title'][ind]][0]
       book_copies[copyID] = bookID
    

    
    with open('bookcopies.csv', 'w') as csvfile:
        write = csv.writer(csvfile)
        write.writerow(['copyid', 'bookid'])
        for copy in book_copies:
            #print(copy)
            write.writerow([copy, book_copies[copy]])


    authors = {}
    for ind in df.index:
        bookID = book_info[df['title'][ind]][0]
        name_list = (df['author'][ind]).split(',')
        for name in name_list:
            if name not in authors.keys():
                authors[name] = [[bookID], ind]
            elif bookID not in authors[name][0]:
                authors[name][0].append(bookID)


    #

    with open('authors.csv', 'w') as csvfile:
        write = csv.writer(csvfile)
        write.writerow(['authorid', 'bookid', 'authorname'])
        for author in authors:
            for book in authors[author][0]:
                write.writerow([authors[author][1], book, author])
    
    
            
    with open('generalcopymiscellaneous.csv', 'w') as csvfile:
        write = csv.writer(csvfile)
        write.writerow(['copyid', 'edition', 'aboutauthor','synopsis'])
        for ind in df.index:
            copyid = df['copyID'][ind]
            edition = df['edition'][ind]
            aboutauthor = df['about_auth'][ind]
            synopsis = df['synopsis'][ind]
            write.writerow([copyid, edition, aboutauthor, synopsis])


    with open('physicalcopyqualities.csv', 'w') as csvfile:
        write = csv.writer(csvfile)
        write.writerow(['copyid','condition', 'price', 'signed', 'dustjacket', 'binding', 'description'])
        for ind in df.index:
            copyid = df['copyID'][ind]
            condition = df['condition'][ind] 
            price = df['price'][ind]
            signed = df['signed'][ind]
            dustjacket = df['dustjacket'][ind]
            binding = df['binding'][ind]
            descr = df['descr'][ind]

            write.writerow([copyid, condition, price, signed, dustjacket, binding, descr])
