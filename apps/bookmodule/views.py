from django.shortcuts import render

from django.http import HttpResponse

from .models import Book

from django.db.models import Q, Count, Sum, Avg, Max, Min


#def index(request): 
  #name = request.GET.get("name") or "world!"
 # return render(request, "bookmodule/index.html" , {"name": name})  #your render line


#def index2(request, val1 = 0):   #add the view function (index2)
#   return HttpResponse("value1 = "+str(val1))


'''def viewbook(request, bookId):
    # assume that we have the following books somewhere (e.g. database)
    book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'}
    book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'}
    targetBook = None
    if book1['id'] == bookId: targetBook = book1
    if book2['id'] == bookId: targetBook = book2
    context = {'book':targetBook} # book is the variable name accessible by the template
    return render(request, 'bookmodule/show.html', context)'''

def index(request):
    return render(request, "bookmodule/index.html")
 
def list_books(request):
    return render(request, 'bookmodule/list_books.html')
 
def viewbook(request, bookId):
    return render(request, 'bookmodule/one_book.html')
 
def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')

def lab5(request):
    return render(request, 'bookmodule/lab5.html')


def __getBooksList():
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
    book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
    book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
    return [book1, book2, book3]

def search(request):
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')
        # now filter
        books = __getBooksList()
        newBooks = []
        for item in books:
            contained = False
            if isTitle and string in item['title'].lower(): contained = True
            if not contained and isAuthor and string in item['author'].lower():contained = True
            
            if contained: newBooks.append(item)
        return render(request, 'bookmodule/list_books.html', {'books':newBooks})
    return render(request, 'bookmodule/search.html')


#lab7
def simple_query(request):

 mybooks=Book.objects.filter(title__icontains='and') # <- multiple objects

 if len(mybooks)>=1:
     return render(request, 'bookmodule/list_books.html', {'books':mybooks})
 else:
     return render(request, 'bookmodule/index.html')



def complex_query(request):

 mybooks=books=Book.objects.filter(author__isnull = False).filter(title__icontains='nd').filter(edition__gte = 2).exclude(price__lte = 200)[:10]

 if len(mybooks)>=1:
     return render(request, 'bookmodule/list_books.html', {'books':mybooks})
 else:
     return render(request, 'bookmodule/index.html')
 
#lab8
def task1(request):
    mybooks = Book.objects.filter(Q(price__lte = 80))
    return render(request, 'bookmodule/lab8.html', {'books':mybooks})
 
def task2(request):
    mybooks = Book.objects.filter(Q(edition__gt = 3) & (Q(title__icontains='co') | Q(author__icontains='co')))
    return render(request, 'bookmodule/lab8.html', {'books': mybooks})

def task3(request):
    mybooks = Book.objects.filter(~Q(edition__gt = 3) & (~Q(title__icontains='co') | Q(author__icontains='co')))
    return render(request, 'bookmodule/lab8.html', {'books': mybooks})

def task4(request):
    mybooks = Book.objects.all().order_by('title')
    return render(request, 'bookmodule/lab8.html', {'books': mybooks})

def task5(request):
    stats = Book.objects.aggregate(
        totalbooks=Count('id'),
        totalprice=Sum('price'),
        average=Avg('price'),
        max=Max('price'),
        min=Min('price')
    )
    return render(request, 'bookmodule/lab8.html', {'stats': stats})