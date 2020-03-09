from django.shortcuts import render, redirect
from .models import Tutorial, TutorialCategory, TutorialSeries
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm
from django.http import HttpResponse

def single_slug(request, single_slug):
    categories = [c.category_slug for c in TutorialCategory.objects.all()]
    if single_slug in categories:
        matching_series = TutorialSeries.objects.filter(tut_category__category_slug=single_slug)

        series_urls = {}
        for m in matching_series.all():
            part_one = Tutorial.objects.filter(tut_series__series=m.series).earliest('date')
            series_urls[m] = part_one.tutorial_slug

        return render(
            request,
            'simplesite/category.html',
            context={'tut_series':matching_series, 'part_ones':series_urls}
            )

    tutorials = [tut.tutorial_slug for tut in Tutorial.objects.all()]
    if single_slug in tutorials:
        this_tutorial = Tutorial.objects.get(tutorial_slug=single_slug)
        tutorial_from_series = Tutorial.objects.filter(tut_series__series=this_tutorial.tut_series).order_by('date')
        this_tutorial_idx = list(tutorial_from_series).index(this_tutorial)

        return render(
            request,
            'simplesite/tutorial.html',
            context={
                'tutorial': this_tutorial,
                'sidebar': tutorial_from_series,
                'this_tut_idx': this_tutorial_idx}
            )

    return HttpResponse(f'{single_slug} does not exist')

def homepage(request):
    return render(
        request,
        'simplesite/categories.html',
        context={'categories': TutorialCategory.objects.all()}
    )

def register(request):
    if request.method=='POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'User created: {username}')
            login(request, user)
            return redirect("/")
            
        else:
            for msg in form.error_messages:
                messages.error(request, f'{msg}: {form.error_messages[msg]}')

            return render(
                request,
                'simplesite/register.html',
                context={'form':form}
            )

    form = NewUserForm
    return render(
        request,
        'simplesite/register.html',
        context={'form':form}
    )

def logout_request(request):
    logout(request)
    messages.info(request, f'Successfully logout')
    return redirect('/')


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST )
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'{username} is logged')
                return redirect('/')
            else:
                messages.error(request, f'Invalid username or password')
        else:
            messages.error(request, f'Invalid username or password')

    form = AuthenticationForm()
    return render(
        request,
        'simplesite/login.html',
        context={'form':form}
    )