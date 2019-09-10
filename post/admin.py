from django.contrib import admin
from django import forms
from .models import Post
from django.contrib.auth.models import User
# Register your models here.


# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = "__all__"

#     def __init__(self, *args, **kwargs):
#         super(PostForm, self).__init__(*args, **kwargs)
#         print(kwargs)
#         self.fields['author'].queryset = User.objects.filter(id=1)

class PostAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "author" and not request.user.is_superuser:
            kwargs["queryset"] = User.objects.filter(pk=request.user.pk)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Post, PostAdmin)
