from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name= "books.index"),
    #path('list_books/', views.list_books, name= "books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path('lab5/', views.lab5, name="books.lab5"),
    path('search/', views.search, name="books.search"),
    path('simple/query/', views.simple_query, name='books.simple_query'),
    path('complex/query/' , views.complex_query, name = 'books.complex_query'),
    
    #lab9
    path('lab9/' , views.lab9, name = 'books.lab9'),
    path('lab9/1/' , views.lab91, name = 'books.lab91'),
    path('lab9/2/' , views.lab92, name = 'books.lab92'),
    path('lab9/3/' , views.lab93, name = 'books.lab93'),
    path('lab9/4/' , views.lab94, name = 'books.lab94'),
    path('lab9/5/' , views.lab95, name = 'books.lab95'),



    
    #lab8
    path('lab8/task1/', views.task1, name="books.task1"),
    path('lab8/task2/', views.task2, name="books.task2"),
    path('lab8/task3/', views.task3, name="books.task3"),
    path('lab8/task4/', views.task4, name="books.task4"),
    path('lab8/task5/', views.task5, name="books.task5"),


 #lab10
    path('list_books/', views.listbooks , name= "books.list_books"),
    path('addBook/', views.addBook, name="books.addbook"),
    path('updateBook/<int:bID>/', views.updateBook, name="books.updatebook"),
    path('books/<int:bID>/', views.onebook, name='books.newbook'),
    path('deleteBook/<int:bID>/', views.deleteBook, name="deleteBook"),
    path('addBookf/', views.addBookf, name="books.addbookf"),
    path('updateBookf/<int:bID>/', views.updateBookf, name="books.updatebookf"),








    #path('t/', views.t, name="books.t"),

]

