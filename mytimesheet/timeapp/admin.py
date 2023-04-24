from django.contrib import admin

from timeapp.models import Employe


class EmployeInLine(admin.TabularInline):
    model = Employe
    extra = 0



@admin.register(Employe)
class EmployeAdmin(admin.ModelAdmin):

    list_display = ('nom_empl', 'prenom_empl', 'fonct_empl', 'adresse_empl', 'contact_empl', 'localisation_empl', 'genre_empl', 'signature_empl')
    List_filter = ('nom_empl', 'prenom_empl', 'fonct_empl', 'adresse_empl', 'contact_empl', 'localisation_empl', 'genre_empl', 'signature_empl')
    search_fields = ('nom_empl', 'prenom_empl','fonct_empl', 'adresse_empl', 'contact_empl', 'localisation_empl', 'genre_empl', 'signature_empl')
