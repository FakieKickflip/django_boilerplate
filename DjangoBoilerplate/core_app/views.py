from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django_q.models import Schedule
from .models import Author, Book
from .forms import AuthorForm, BookForm, EmailForm

# Create your views here.




def index(request):

    title_text = 'work in progress... '
    

    return render(request, "core_app/index.html",
    {"title_text": title_text})



def contact(request):
    return render(request, "core_app/contact.html")



def scheduled_task(request):
    try:
        Schedule.objects.create(func='core_app.scheduled_tasks.print_me', args="'Hey.'", schedule_type=Schedule.ONCE, repeats=-1)
        #‘O’ the schedule will only run once. If it has a negative repeats it will be deleted after it has run. If you want to keep the result, set repeats to a positive number.
        messages.success(request, message=f'Scheduled task started.')
    except:
        messages.warning(request, message=f'Something went wrong with the scheduled task.')   
    return render(request, "core_app/index.html")



def create_author(request):
    
    if request.method == "POST": 
        form = AuthorForm(data=request.POST)
        if form.is_valid(): 
            if len(request.POST.keys()) > 1: #nicht nur der csrf-token enthalten
                
                name = form.cleaned_data['name']
                age = form.cleaned_data['age']
                new_author = Author(name=name, age=age)
                new_author.save() 
                messages.success(request, message=f'Author wurde erfolgreich angelegt.')
        return redirect("/create_author/")  

    else:
        form = AuthorForm()

        action_endpoint = "/create_author/"

        return render(request, "core_app/forms.html",
        {"form": form, "action_endpoint": action_endpoint})



def create_book(request):
    if request.method == "POST": 
        form = BookForm(data=request.POST)
        if form.is_valid(): 
            if len(request.POST.keys()) > 1: #not only the csrf-token
                form.save() #ModelForm does not need to perform clean_data. You can safe it from the form directly.
                messages.success(request, message=f'Das Buch wurde erfolgreich angelegt.')
        return redirect("/create_book/")  

    else:
        form = BookForm()

        action_endpoint = "/create_book/"

        return render(request, "core_app/forms.html",
        {"form": form, "action_endpoint": action_endpoint})         



def all_authors(request):
    if request.method == "POST":
        datas = {'success': False} 
        if len(request.POST.keys()) > 1: #not only the csrf token
            if 'trash_id' in request.POST:
                book_id = request.POST['trash_id'] #the book_id gets passed via name:trash_id. For more info check out the html template
                Book.objects.filter(id=book_id).first().delete()
                datas['success'] = True  
                return JsonResponse(datas)

    authors = Author.objects.all()

    #use the relationship
    for author in authors:
        for book in author.book_set.all():
            print(book.title)

    return render(request, "core_app/all_authors.html",
    {"authors": authors} )



def send_email(request):
    if request.method == "POST": 
        form = EmailForm(data=request.POST)
        if form.is_valid(): 
            if len(request.POST.keys()) > 1: #not only the csrf-token
                
                receiver_email = form.cleaned_data['email']
                text = form.cleaned_data['text']

                print(settings.EMAIL_HOST_USER)

                send_mail('A cool subject', text, settings.EMAIL_HOST_USER, [receiver_email])                

                messages.success(request, message=f'The message has been send.')
        return redirect('/send_email/')

    else:
        form = EmailForm()
        return render(request, "core_app/forms.html",
        {'form': form})

