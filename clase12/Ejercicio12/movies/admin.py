from django.contrib import admin

from .models import Movies, Director

class MovieInLine(admin.StackedInline):
    model = Movies
    extra = 1 

class DirectorAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ('name', 'last_name', 'biography', 'image')}),
        ('Fechas', {
            'fields': ('born_date' , 'dead_date'),
            'classes' : ('collapse')
        }),
    ]
    inlines = [MovieInLine]


admin.site.register(Director, DirectorAdmin)
