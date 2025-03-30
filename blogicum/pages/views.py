from django.shortcuts import render

# Create your views here.
def about(request):
    # Адрес шаблона сохранён в переменную, это не обязательно, но удобно.
    template_name = 'pages/about.html'

    # Третьим аргументом в render() передаём словарь context:
    return render(request, template_name)


def rules(request):
    # Адрес шаблона сохранён в переменную, это не обязательно, но удобно.
    template_name = 'pages/rules.html'

    # Третьим аргументом в render() передаём словарь context:
    return render(request, template_name)
