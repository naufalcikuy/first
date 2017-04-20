from django.contrib import admin
from .models import Post
from .models import Knowledge
from .models import BabyBio
from .models import History, Event
class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'text', 'created_date', 'published_date']
    search_fields = ['title']
    list_per_page = 25

admin.site.register(Post, PostAdmin)

class KnowledgeAdmin(admin.ModelAdmin):
    list_display = ['category', 'title', 'text', 'created_date', 'published_date']
    search_fields = ['title', 'category']
    list_per_page = 25
admin.site.register(Knowledge, KnowledgeAdmin)

class BabyBioAdmin(admin.ModelAdmin):
    list_display = ['id_baby', 'baby_name', 'date_birth', 'address', 'mother_name', 'father_name', 'weight_birth', 'height_birth', 'headcircumference_birth', 'created_date']
    search_fields = ['id_baby', 'baby_name']
    list_per_page = 25
admin.site.register(BabyBio, BabyBioAdmin)

class HistoryAdmin(admin.ModelAdmin):
	list_display = ['baby','check','value','imun_value','status','created_date','published_date']
	search_fields = ['check']
admin.site.register(History, HistoryAdmin)

#class EventAdmin(admin.ModelAdmin):

admin.site.register(Event)


# Register your models here.
