from django.contrib import admin

from .models import Choice, Question, Student


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        (None,               {'fields': ['country']}),
        ('Date information', {'fields': ['birth_date'], 'classes': ['collapse']}),
    ]
    list_display = ('name', 'country', 'birth_date')
    search_fields = ['name']
    list_filter = ['birth_date']