from django.shortcuts import render

# Create your views here.
def indexPage(request):
    return render(request, 'index.html')

def aboutUs(request):
    return render(request, 'about.html')


def contactUs(request):
    return render(request, 'contact.html')

def card_color(request):
    context = {
        'color': 'all',
    }

    if request.method == "GET" and request.GET.get('color') != None:
        context['color'] = request.GET.get('color')

    return render(request, 'card_color.html', context)

def for_test(request):
    context = {}
    lt = list(range(0, 100))
    context["list"] = lt

    return render(request, 'for_test.html', context)

def for_page(request):
    email = ''
    password = ''

    context = {}

    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('my-password')

    context['email'] = email
    context['password'] = password

    return render(request, 'for_page.html', context)