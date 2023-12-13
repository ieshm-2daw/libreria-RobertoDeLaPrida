from django.contrib import admin
from .models import User, Book , Author , Editorial , Loan
from django.contrib.auth.admin import UserAdmin
# Register your models here.

admin.site.register(User,UserAdmin)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Editorial)
admin.site.register(Loan)