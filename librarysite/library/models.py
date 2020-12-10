from django.db import models

# from library.models import BookInfo, Authors, BookCopies, PhysicalCopyQualities, GeneralCopyMiscellaneous
# b1 = BookInfo(bookID = 1, title = "title1", publisher = "1", pubDate = 2021, isbn10 = 10, isbn13 = 13)
# a1 = Authors(authorID = 1, bookID = b1, authorName = "a1")
# bc1 = BookCopies(copyID = 1, bookID = b1)
# pcq1 = PhysicalCopyQualities(copyID = bc1, condition = "cond1", price = "price1", signed = "signed1", dustjacket = "dj1", binding = "bind1", description = "desc1")
# gcm1 = GeneralCopyMiscellaneous(copyID = bc1, edition = 'ed1', about_auth = "about1", synopsis = "syn1")

# Create your models here.
class BookInfo(models.Model):
    bookID = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    publisher = models.CharField(max_length=200, null = True, blank=True)
    pubDate = models.IntegerField(null = True, blank=True)
    isbn10 = models.CharField(max_length = 15, null = True, blank=True)
    isbn13 = models.CharField(max_length = 15, null = True, blank=True)

    def __str__(self):
        return str(self.bookID) + " : " + str(self.title)

class BookCopies(models.Model):
    copyID = models.IntegerField()
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.copyID) + " : " + str(self.book.title)

    class Meta:
        unique_together = (("copyID", "book"),)

class Authors(models.Model):
    authorID = models.IntegerField()
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)
    authorName = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.authorID) + " : " + self.authorName 

    class Meta:
        unique_together = (("authorID", "book"),)


class PhysicalCopyQualities(models.Model):
    copy = models.OneToOneField(BookCopies, primary_key=True, on_delete=models.CASCADE)
    condition = models.CharField(max_length=200, null=True, blank=True)
    price = models.CharField(max_length=200, null=True, blank=True)
    signed = models.CharField(max_length=200, null=True, blank=True)
    dustjacket = models.CharField(max_length=200, null=True, blank=True)
    binding = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.copy.copyID) + " : " + str(self.condition)


class GeneralCopyMiscellaneous(models.Model):
    copy = models.OneToOneField(BookCopies, primary_key=True, on_delete=models.CASCADE)
    edition = models.CharField(max_length=200, null=True, blank=True)
    about_auth = models.CharField(max_length=200, null=True, blank=True)
    synopsis = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.copy.copyID) + ":" + str(self.edition) + ":" + str(self.about_auth) + ":" + str(self.synopsis)


    
