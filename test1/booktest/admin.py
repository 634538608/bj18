from django.contrib import admin

# Register your models here.
from booktest.models import BookInfo
from booktest.models import HeroInfo

class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id','btitle','bpub_date']

class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id',' hname','hgender','isDelete','hcomment','hbook']

admin.site.register(BookInfo)
admin.site.register(HeroInfo)