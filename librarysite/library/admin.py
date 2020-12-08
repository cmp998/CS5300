from django.contrib import admin

from .models import BookInfo, Authors, BookCopies, PhysicalCopyQualities, GeneralCopyMiscellaneous

admin.site.register(BookInfo)
admin.site.register(Authors)
admin.site.register(BookCopies)
admin.site.register(PhysicalCopyQualities)
admin.site.register(GeneralCopyMiscellaneous)

# Register your models here.
