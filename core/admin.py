from django.utils.html import format_html
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Notary, Rate, Page, PageContent


class InlineTabularRate(admin.TabularInline):
    model = Rate
    readonly_fields = ["id", ]


class NotaryAdmin(admin.ModelAdmin):
    inlines = [InlineTabularRate, ]

    list_display = ('id', 'name', 'view_account', 'address', 'house_number', 'latitude', 'longitude', 'phone',
                    'whatsapp', 'telegram', 'email', 'website', 'description', 'image', 'schedule', 'view_rates')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    summernote_fields = ('schedule', )

    def view_rates(self, obj):
        return format_html(f'<a href="/admin/core/rate/?notary__id__exact={obj.id}">{obj.rates.count()} тарифов </a>')
    
    def view_account(self, obj):
        return format_html(f'<a href="/admin/account/account/?notary__id__exact={obj.id}">{obj.account}</a>')
    

class RateAdmin(admin.ModelAdmin):
    list_display = ('id', 'notary', 'rate', 'view_notary')
    list_display_links = ('id', )
    search_fields = ('name',)
    list_filter = ('notary',)

    def view_notary(self, obj):
        return format_html(f'<a href="/admin/core/notary/?rate__id__exact={obj.id}">{obj.notary}</a>')
    view_notary.short_description = "Нотариус"


class InlineTabularPageContent(admin.TabularInline):
    model = PageContent
    readonly_fields = ["id", ]


class PageAdmin(admin.ModelAdmin):
    inlines = [InlineTabularPageContent, ]

    list_display = ('id', 'name', 'slug', "view_page_content")
    list_display_links = ('id', 'name', 'slug')
    search_fields = ('name',)
    list_filter = ('name',)

    def view_page_content(self, obj):
        return format_html(f'<a href="/admin/core/pagecontent/?page__id__exact={obj.id}">{obj.contents.count()} '
                           f'контента </a>')
    view_page_content.short_description = "Контент страницы"
    

class PageContentAdmin(SummernoteModelAdmin):
    list_display = ('id', 'page', 'title', 'content', 'footer', 'body', 'class_name', 'order', 'style', 'user')
    summernote_fields = ('content', )
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_filter = ('page',)


admin.site.register(Notary, NotaryAdmin)
admin.site.register(Rate, RateAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(PageContent, PageContentAdmin)