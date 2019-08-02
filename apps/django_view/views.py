from django.shortcuts import render, HttpResponse, Http404, get_object_or_404
from django.http import JsonResponse
from django.views.generic import TemplateView, ListView, View, DetailView

# Create your views here.

# request 必填，名字可以修改，封装了用户请求的所有内容
def view_test(request):
    html = '<h1>i am demo01</h1>'
    print(html)
    # 此处不能直接return html, 必须返回一个HttpResponse对象
    return HttpResponse(html, status=404, charset="utf-8")


def zoos(request, id):
    id = int(id)
    if id > 100:
        raise Http404('not exist')
    return HttpResponse(f"这是第{id}个动物园的信息")

from app01.models import UserInfo
def zoos(request, id):
    id = int(id)
    1/0
    # get_object_or_404 => 从Model中获取数据，如果没有获取到，就raise一个Http404
    user = get_object_or_404(UserInfo, pk=id)
    return HttpResponse(user.username)


class MyTemplateView(TemplateView):
    # 指定要返回的模板
    template_name = "template_view.html"
    # 设置模板解析后端引擎
    # template_engine =
    # 额外
    def get_context_data(self, **kwargs):
        return {"ABC":"ABC"}




from app01.models import UserInfo
from django.views.decorators.gzip  import gzip_page

@gzip_page
def userinfo(request):
    # 获取所有的用户信息
    userlist = UserInfo.objects.all()
    title = "ABC"
    return render(request, "list_view.html", {"userlist":userlist, "title":title})


class MyListView(ListView):
    """
    把app01.models.UserInfo表中的信息查询出来放到html页面上
    Define MyListView.model, MyListView.queryset, or override MyListView.get_queryset()
    """
    template_name = "list_view.html"
    # model => 从models中查询出所有的数据 UserInfo.objects.all()
    # model = UserInfo
    # queryset => 自己写一个查询语句，返回查询结果集
    # queryset = UserInfo.objects.filter(username="cali")
    # 默认结果集名：object_list ，设置了context_object_name后，指定的名和object_list都可以用
    context_object_name = "userlist"

    def get_queryset(self):
        """
        返回查询结果集
        :return:
        """
        return UserInfo.objects.filter(username="feng")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "ABC"
        return context


class MyDetailView(DetailView):
    model = UserInfo
    template_name = "detail_view.html"
    # 查询的关键字 => pk => 默认主键id
    pk_url_kwarg = "user_id"
    # 默认名：object
    # context_object_name = ""

    def get_object(self, queryset=None):
        user = super().get_object()
        # user = self.get_object()
        user.abc = "hello"
        return user
