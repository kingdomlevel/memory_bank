from django.shortcuts import render

# Create your views here.


def index(request):
    # request.session.set_test_cookie()

    # category_list = Category.objects.order_by('-likes')[:5]
    # page_list = Page.objects.order_by('-views')[:5]
    # context_dict = {'categories': category_list, 'pages': page_list}

    # visitor_cookie_handler(request)
    # context_dict['visits'] = request.session['visits']

    response = render(request, 'memoryBankApp/index.html')
    return response
