from django.contrib import admin

from contents.models import Content, Image, FollowRelation


class ImageInline(admin.TabularInline):
    model = Image


class ContentAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    list_display = ('user', 'created_at',)
# 콘텐츠어드민이 이미지인라인의 상위개념이 된다고 보면된다.
# imageinline 을 쓸떄 model을 변수로 안해주면 오류가 생기며, contentadmin에서도 inlines으로 받아줘야한다.


admin.site.register(Content, ContentAdmin)


class ImageAdmin(admin.ModelAdmin):
    pass


admin.site.register(Image, ImageAdmin)


class FollowRelationAdmin(admin.ModelAdmin):
    pass


admin.site.register(FollowRelation, FollowRelationAdmin)
