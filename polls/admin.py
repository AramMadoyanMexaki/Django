from django.contrib import admin
from .models import Question, Choice, PollUser

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3



class QuestionAdmin(admin.ModelAdmin):
    list_display = ["pub_date", "question_text", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]

    fieldsets = [
        ("Main Info", {"fields": ["question_text"], "classes": ["collapse"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]

    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(PollUser)
