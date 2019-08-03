from django.shortcuts import render, get_object_or_404
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny
from .models import Page
from .serializers import PageSerializer

class PageView(RetrieveAPIView):
    """
    获取文章详情
    """
    permission_classes = (AllowAny,)
    model = Page
    queryset = Page.objects.filter(is_active=True)
    serializer_class = PageSerializer
    lookup_field = 'slug'

def page_view(request, slug):
    " 文章详情页面 "
    obj = get_object_or_404(Page, slug=slug)
    children = obj.page_set.filter(is_active=True)
    return render(request, 'page/%s.html' % obj.template, {'obj':obj, 'children':children})
