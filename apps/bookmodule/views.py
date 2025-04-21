from django.shortcuts import render , redirect
from django.http import HttpResponse
from .forms import BookForm
from .models import Book, Publisher, Author
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

 mybooks=Book.objects.all() # <- multiple objects

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

#lab9
def lab9(request):
     objs= Publisher.objects.annotate(bookcounter= Count("book"),oldest_pubdate= Min("book__pubdate"))
     return render(request, 'bookmodule/lab9.html', {'books': objs})

def lab91(request):
     objs= Publisher.objects.annotate(oldest_pubdate= Min("book__pubdate"))
     return render(request, 'bookmodule/lab9.html', {'books': objs})
 
def lab92(request):
     objs= Publisher.objects.annotate(avg_price= Avg('book__price'))
     return render(request, 'bookmodule/lab9.html', {'books': objs})
 
def lab93(request):
     highly_rated= Count("book", filter=Q(book__rating__gte= 7))
     objs= Publisher.objects.annotate(num_books= Count("book"), highly_rated_books= highly_rated)
     return render(request, 'bookmodule/lab9.html', {'books': objs})
 
def lab94(request):
     objs = Publisher.objects.annotate(book_count=Count('book',filter = Q(book__price__gt=50)))
     return render(request, 'bookmodule/lab9.html', {'books': objs})
  
def lab95(request):
     objs= Book.objects.annotate(author_count=Count('author')).filter(author_count__gt= 1).order_by('author_count')
     return render(request, 'bookmodule/lab9.html', {'books': objs})  
 
 #-----------------------------------------------------------------
 

#lab10
def addBook(request):
    if request.method=='POST':
        title=request.POST.get('title')
        price=request.POST.get('price')
        rating=request.POST.get('rating')
        Publisher_id=request.POST.get('Publisher_id')
        PublisherObj= Publisher.objects.get(id = Publisher_id)
        author_id=request.POST.get('author_id')
        authorObj= Author.objects.get(id = author_id)
        obj = Book(title=title, price = float(price),rating = rating, 
                publisher = PublisherObj) 
        obj.save() 
        obj.author.set({authorObj})
        return redirect('books.newbook', bID = obj.id)
    
    publishers = Publisher.objects.order_by('name')
    authors = Author.objects.all().order_by('name')
    return render(request, "bookmodule/addBook.html",{'authors': authors, 'publishers': publishers})

def addBookf(request):
    obj = None
    authors = Author.objects.all().order_by('name')
    Publisher = Publisher.objects.all().order_by('name')

    if request.method=='POST':
        form = BookForm(request.POST)
        if form.is_valid():
            obj = form.save()
            return redirect('books.newbook', bID = obj.id)
        else: form = BookForm(None)
        return render(request, "bookmodule/addBook.html",{'authors':authors, 'form':form , 'Publisher':Publisher})
    
    
# update book 
def updateBook(request, bID): 
    obj = Book.objects.get(id = bID)
    if request.method == 'POST':
        title=request.POST.get('title')
        price=request.POST.get('price')
        rating=request.POST.get('rating')
        Publisher_id=request.POST.get('Publisher_id')
        PublisherObj= Publisher.objects.get(id = Publisher_id)
        author_id=request.POST.get('author_id')
        authorObj= Author.objects.get(id = author_id)
        
        obj.title = title
        obj.price = float(price)
        obj.rating = int(rating)
        obj.publisher = PublisherObj
        obj.author.set({authorObj})
        obj.save()
        return redirect('books.newbook', bID = obj.id)
    
    publisher = Publisher.objects.all()
    author = Author.objects.all()
    return render(request, "bookmodule/updateBook.html", {'obj':obj,'author':author,'publisher': publisher})

def updateBookf(request , bID):
    obj = None
    author = Author.objects.all().order_by('name')
    publisher = Publisher.objects.all().order_by('name')
    book = Book.objects.get(id = bID)

    if request.method=='POST':
        form = BookForm(request.POST , instance=book)
        if form.is_valid():
            obj = form.save()
            return redirect('books.newbook', bID = obj.id)
    else:form = BookForm(instance=book)
    return render(request, "bookmodule/updateBook.html",{'author':author, 'form':form , 'publisher':publisher})
    

def listbooks(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/list_books.html', {'books': books })


def onebook( request , bID):
    book = Book.objects.get(id = bID)
    return render(request, 'bookmodule/onebook.html', {'books': book})

def deleteBook(request,bID):
    obj = Book.objects.get(id = bID)
    if request.method=='POST':
        obj.delete()
        return redirect('books.list_books')
    
    return render(request, "bookmodule/deleteBook.html", {'obj':obj})

