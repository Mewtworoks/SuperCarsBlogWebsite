from.models import Blog_Category
from django.forms import ModelForm
from.models import blog_post
 


class Blog_Form(ModelForm):
    class Meta:
         model = Blog_Category
         fields = "__all__"

class BlogPost_Form(ModelForm):
    class Meta:
         model = blog_post
         fields = "__all__"