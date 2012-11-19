from about.models import About
from django.contrib import admin
from django import forms

class AboutAdmin(admin.ModelAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(AboutAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'body':
            formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
        return formfield
    fieldsets = [
        (None,               {'fields': ['title','body','is_current']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

admin.site.register(About, AboutAdmin)