from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Story, Subscriber
from .forms import StoryForm, SubscriberForm


def index(request):
    if request.method == "POST":
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")  # Refresh page after subscribing
    else:
        form = SubscriberForm()

    return render(request, "blog/index.html", {"form": form})

def my_corner(request):
    return render(request, 'blog/mycorner.html')

def fiction(request):

    # Get recent stories for each category
    fiction_stories = Story.objects.filter(category='fiction').order_by('-created_at')[:5]

    context = {"stories": fiction_stories}
    return render(request, 'blog/fiction.html', context=context)
    

def truecrime(request):
    truecrime_stories = Story.objects.filter(category='true_crime').order_by('-created_at')[:5]
    context = {"stories": truecrime_stories}
    return render(request, 'blog/truecrime.html', context=context)


# Step 1: Upload story without category
def upload_story(request):
    if request.method == 'POST':
        form = StoryForm(request.POST)
        if form.is_valid():
            story = form.save(commit=False)
            story.category = None  # Initially no category
            story.save()
            return redirect('choose_category', story_id=story.id)
    else:
        form = StoryForm()

    # Get recent stories for each category
    fiction_stories = Story.objects.filter(category='fiction').order_by('-created_at')[:5]
    truecrime_stories = Story.objects.filter(category='true_crime').order_by('-created_at')[:5]

    return render(request, 'blog/upload_story.html', {
        'form': form,
        'fiction_stories': fiction_stories,
        'truecrime_stories': truecrime_stories,
    })


# Step 2: Choose category
def choose_category(request, story_id):
    story = get_object_or_404(Story, id=story_id)
    if request.method == 'POST':
        chosen_category = request.POST.get('category')
        story.category = chosen_category
        story.save()
        return redirect('category_list', category=chosen_category)
    return render(request, 'blog/choose_category.html', {'story': story})

# Step 3: Show stories in category
def category_list(request, category):
    stories = Story.objects.filter(category=category).order_by('-created_at')

    # Map category slug to template filename
    template_map = {
        'true_crime': 'truecrime.html',
        'fiction': 'fiction.html'
    }

    # Pick template or fallback
    template_name = template_map.get(category, 'category_list.html')

    return render(request, f'blog/{template_name}', {'stories': stories})

# Step 4: Individual story page
def story_detail(request, pk):
    story = get_object_or_404(Story, pk=pk)

# Previous story in the same category
    previous_story = Story.objects.filter(
        category=story.category, pk__lt=story.pk
    ).order_by('-pk').first()

    # Next story in the same category
    next_story = Story.objects.filter(
        category=story.category, pk__gt=story.pk
    ).order_by('pk').first()


 # Get "from" and "page" query params if available
    from_page = request.GET.get('from')
    page_number = request.GET.get('page')

    return render(request, 'blog/story_detail.html', {
        'story': story,
        'previous_story': previous_story,
        'next_story': next_story,
        'from_page': from_page,
        'page_number': page_number,
    })

def story_list(request):
    stories = Story.objects.all().order_by('-created_at')
    fiction_stories = stories.filter(category='fiction')
    truecrime_stories = stories.filter(category='true_crime')

    # Debug prints (check terminal when you load /stories/)
    print("All stories:", stories.values_list("id", "title", "category"))
    print("Fiction stories:", fiction_stories.values_list("id", "title", "category"))
    print("True crime stories:", truecrime_stories.values_list("id", "title", "category"))

    return render(request, 'blog/storylist.html', {
        'fiction_stories': fiction_stories,
        'truecrime_stories': truecrime_stories,
    })


def delete_story(request, story_id):
    story = get_object_or_404(Story, id=story_id)
    if request.method == "POST":  # only delete if user confirms with POST
        story.delete()
    return redirect('story_list')


# password
def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully!")
            return redirect("upload_story")  # redirect after login
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "blog/login.html")

def user_logout(request):
    logout(request)
    return redirect("home")

