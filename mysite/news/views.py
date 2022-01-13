from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, DeleteView, UpdateView

from .models import News, Category
from .forms import NewsForm


class HomeNews(ListView):
    model = News  #аналог news = News.objects.all() в index
    template_name = 'news/home_news_list.html'  # шаблон
    context_object_name = 'news'  #имя переменной, которая отправляется в шаблон
    # extra_context = {'title': 'Главная'}  # не рекомендуется но очень удобно для титульника вместо функции внизу

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True)  # покажет только новости с чекбоксами


class UpdateNews(UpdateView):
    model = News
    template_name = 'news/add_news.html'

    form_class = NewsForm

class DeleteNews(DeleteView):
    model = News
    template_name = 'news/delete_news.html'

    success_url = '/'



class NewsByCategory(ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news' #имя переменной, которая отправляется в шаблон
    allow_empty = False     #запрещаем показ пустых списков (не существующих) это исключает 500 ошибку при выборе и отдаст 404


    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

class ViewNews(DetailView):
    model = News
    context_object_name = 'news_item'  #имя переменной, которая отправляется в шаблон
    # template_name = 'news/news_detail'
    # pk_url_kwarg = 'news_id'

# def index(request):
#     news = News.objects.all()
#     context = {
#         'news': news,
#         'title': 'Список новостей',
#     }
#     return render(request, template_name='news/index.html', context=context)


# def get_category(request, category_id):
#     news = News.objects.filter(category_id=category_id)
#     category = Category.objects.get(pk=category_id)
#     return render(request, 'news/category.html', {'news': news, 'category': category})




# def view_news(request, news_id):
#     # news_item = News.objects.get(pk=news_id)
#     news_item = get_object_or_404(News, pk=news_id)
#     return render(request, 'news/view_news.html', {"news_item": news_item})


def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save()
            return redirect(news)  # переадресация после сохранения
    else:
        form = NewsForm()  #  создается пустая форма
    return render(request, 'news/add_news.html', {'form': form})    #рисуем шаблон


# не связанные формы
# def add_news(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             news = News.objects.create(**form.cleaned_data)  # сохраняет новость (в связаных формах - save())
#             return redirect(news)  # переадресация после сохранения
#     else:
#         form = NewsForm()
#     return render(request, 'news/add_news.html', {'form': form})
