from django.contrib import admin
from .models import Team, Osoba, Stanowisko

class OsobaAdmin(admin.ModelAdmin):
    @admin.display(description='Stanowisko (id)')
    def stanowisko_id(self, obj):
        return f'{obj.stanowisko.nazwa} ({obj.stanowisko.id})'
    list_display = ('imie', 'nazwisko', 'plec', 'data_dodania', 'stanowisko_id')
    list_filter = ('stanowisko', 'data_dodania')
    readonly_fields = ['data_dodania']

class StanowiskoAdmin(admin.ModelAdmin):
    list_filter = ('nazwa',)

admin.site.register(Team)
admin.site.register(Osoba, OsobaAdmin)
admin.site.register(Stanowisko, StanowiskoAdmin)

