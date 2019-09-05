from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Object, Relationship, Tag


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        ismain_choice = False
        for form in self.forms:
            if 'isMain' in form.cleaned_data and form.cleaned_data['isMain'] == True:
                ismain_choice = True
        if ismain_choice:
            raise ValidationError('Много тегов!')
        return super().clean()  # вызываем базовый код переопределяемого метода


class RelationshipInline(admin.TabularInline):
    model = Relationship
    formset = RelationshipInlineFormset


@admin.register(Object)
class ObjectAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]


admin.site.register(Tag)
