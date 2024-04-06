from django.contrib import admin
from .models import Service,Blog,CommentBlog,CommentService,FavoriteService,FavoriteBlog,Review,ServiceType
admin.site.register(Service)
admin.site.register(Blog)
admin.site.register(CommentBlog)
admin.site.register(CommentService)
admin.site.register(FavoriteService)
admin.site.register(FavoriteBlog)
admin.site.register(Review)
admin.site.register(ServiceType)

