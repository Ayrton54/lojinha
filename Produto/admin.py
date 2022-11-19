from django.contrib import admin
from . import models


class VariacaoInline(admin.TabularInline):
    model = models.Variacao
    extra = 1


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'Preço', 'Preço_Promocional')
    inlines = [VariacaoInline]


admin.site.register(models.Produto, ProdutoAdmin)
admin.site.register(models.Variacao)
