from django.shortcuts import render
from django.http import HttpResponse
from .models import BookCopies, Authors, PhysicalCopyQualities,GeneralCopyMiscellaneous, BookInfo
import sys, os, csv


def index(request):
    dictionary = {"books": [{"book1" : "page1"}, {"book2": "page2"}]}
    return render(request, 'library.html', dictionary)

def library(request):
    query = BookInfo.objects.order_by('bookID')[:]
  
    bookList = []
    
    for bi in query:

        a = Authors.objects.filter(book=bi)
        if len(a) ==1 :
            bk = {"title": bi.title, "isbn10": bi.isbn10, "isbn13": bi.isbn13, "publisher": bi.publisher, "pubdate": bi.pubDate, "author": a[0].authorName, "book_id": bi.bookID}
        if len(a) > 1:
            bk = {"title": bi.title, "isbn10": bi.isbn10, "isbn13": bi.isbn13, "publisher": bi.publisher, "pubdate": bi.pubDate, "author": a[0].authorName + " and others", "book_id": bi.bookID}
        else:

            bk = {"title": bi.title, "isbn10": bi.isbn10, "isbn13": bi.isbn13, "publisher": bi.publisher, "pubdate": bi.pubDate, "author": "None", "book_id": bi.bookID}
        bookList.append(bk)

    renderThis = {"books": bookList}
    return render(request, 'library.html', renderThis)



def libraryBook(request, book_id):
    
    query = BookCopies.objects.order_by('copyID').filter(book_id=book_id)[:]
  
    bookList = []
    
    for bc in query:
       
      
        pcq = PhysicalCopyQualities.objects.filter(copy=bc)[0]
        gcm = GeneralCopyMiscellaneous.objects.filter(copy=bc)[0]
        
        bk = {"title": bc.book.title, "isbn10": bc.book.isbn10, "isbn13": bc.book.isbn13, "publisher": bc.book.publisher, "pubdate": bc.book.pubDate, "binding": pcq.binding, "condition":pcq.binding, "price":pcq.price, "signed":pcq.signed, "dustjacket":pcq.dustjacket,"description":pcq.description, "about_author": gcm.about_auth, "edition":gcm.edition, "synopsys":gcm.synopsis}
        bookList.append(bk)

    renderThis = {"books": bookList}
    return render(request, 'library.html', renderThis)

def author(request):
    query = Authors.objects.values("authorName", "authorID").order_by('authorID').distinct()

    authorList = []
    for author in query:
        print(author)
        authorList.append({"name": author['authorName'], "author_id": author['authorID']})
    dictionary = {"authors": authorList}
    return render(request, 'author.html', dictionary)


def authorBooks(request, authorID):
    query = Authors.objects.values("authorID", "book", "authorName").filter(authorID=authorID)

    bookList = []
    for author in query:
        print(author)
        b = BookInfo.objects.filter(bookID=author['book'])

        bookList.append({"title": b[0].title, "bookID": b[0].bookID})
    dictionary = {"books": bookList, "author": query[0]['authorName']}
    return render(request, 'authorbooks.html', dictionary)

def editions(request):
    return render(request, "editions.html")