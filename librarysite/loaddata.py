from library.models import BookInfo, BookCopies, Authors, PhysicalCopyQualities, GeneralCopyMiscellaneous
from django.conf import settings

settings.configure()
# load book info

objects = []
with open("../cleaned_db/bookinfo.csv") as f:
    reader = csv.reader(f)
    rowNum = 0
    for row in reader:
        rowNum += 1
        if rowNum != 1:
            b = BookInfo()
            b.bookID = row[0]
            b.title = row[1] 
            if row[2] != "0":
                b.publisher = row[2] 
            else:
                b.publisher = None
            if row[3] != "0":
                b.pubDate = row[3]
            else:
                b.pubDate = None
            if row[4] != "0":
                b.isbn10 = row[4]
            else:
                b.isbn10 = None
            if row[5] != "0":
                b.isnb13 = row[5]    
            else:
                b.isbn13 = None 
            print(f"row {rowNum}") 
            objects.append(b)
        
    print(len(objects))
    BookInfo.objects.bulk_create(objects)

    


with open("../cleaned_db/bookcopies.csv") as f:
    reader = csv.reader(f)
    rowNum = 0
    objects = []
    for row in reader:
        rowNum += 1
        if rowNum != 1:
            bc = BookCopies()
            bc.copyID = row[0]
            bc.book = BookInfo.objects.get(bookID = row[1])
            objects.append(bc)
            print(f"row: {rowNum}")
    BookCopies.objects.bulk_create(objects)
        


with open("../cleaned_db/authors.csv") as f:
        reader = csv.reader(f)
        rowNum = 0
        objects = []
        for row in reader:
            rowNum += 1
            if rowNum != 1:
                a = Authors()
                a.authorID = row[0]
                a.book = BookInfo.objects.get(bookID = row[1])
                a.authorName = row[2]
                objects.append(a)
                print(f"row {rowNum}")
        Authors.objects.bulk_create(objects)

with open("../cleaned_db/physicalcopyqualities.csv") as f:
        reader = csv.reader(f)
        rowNum = 0
        for row in reader:
            rowNum += 1
            if rowNum != 1:
                p = PhysicalCopyQualities.objects.create()
                p.copy = BookCopies.objects.get(copyID = row[0])
                if row[1] != "0":
                    p.condition = row[1] 
                else:
                    p.condition = None
                if row[2] == "0": 
                    p.price = None
                else:
                    p.price = row[2] 
                if row[3] == "0": 
                    p.signed = None
                else:    
                    p.signed = row[3] 
                if row[4] == "0": 
                    p.dustjacket = None
                else:
                    p.dustjacket = row[4] 
                if row[5] == "0": 
                    p.binding = None
                else:
                    p.binding = row[5]
                if row[6] == "0":
                    p.description = None
                else:
                    p.description = row[6]
                print(f"row {rowNum}")
                p.save()
                

with open("../cleaned_db/generalcopymiscellaneous.csv") as f:
        reader = csv.reader(f)
        rowNum = 0
        for row in reader:
            rowNum += 1
            if rowNum != 1:
                g = GeneralCopyMiscellaneous.objects.create()
                g.copy = BookCopies.objects.get(copyID = row[0])
                if row[1] == "0":
                    g.edition = None
                else:
                    g.edition = row[1]
                if row[2] == "0":
                    g.about_auth = None
                else:
                    g.about_auth = row[2]
                if row[3] == "0":
                    g.synopsis = None
                else:
                    g.synopsis = row[3]
                g.save()
                print(f"row {rowNum}")

                
                

                