from django.contrib import admin
from .models import Categoria, Contato


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'twitter', 'data_nascimento')

    #list_display_links = ('id', 'nome', 'email')
    # list_filter = ('nome', 'sobrenome')
    list_per_page = 10
    #search_fields = ('nome', 'email')
    #list_editable = ('nome', 'email')


admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)