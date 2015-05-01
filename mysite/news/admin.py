from django.contrib import admin
from suit.admin import SortableModelAdmin
from image_cropping import ImageCroppingMixin
from easy_thumbnails.files import get_thumbnailer

from .models import News


class NewsAdmin(ImageCroppingMixin, SortableModelAdmin):
    readonly_fields = ('News_image_url', 'News_thumb_url',)
    sortable = 'order'


    def News_image_url(self, obj):
        if not obj.image:
            return ''
        return '<a target="_blank" href="' + obj.image.url + '">' + obj.image.url + '</a>'
    News_image_url.allow_tag = True

    def News_thumb_url(self, obj):
        if not obj.image or not obj.thumb_image_width or not obj.thumb_image_height:
            return ''
        url = get_thumbnailer(obj.image).get_thumbnail({
                'size': (obj.thumb_image_width, obj.thumb_image_height),
                'box': obj.min_free_cropping,
                'crop': True,
                'detail': True,
                }).url
        return '<a target="_blank" href="' + url + '">' + url + '</a>'
    News_thumb_url.allow_tag = True

admin.site.register(News, NewsAdmin)

