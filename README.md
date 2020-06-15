How would we filter for all books with titles containing the word ‘Django’?
- django_book_list = Book.objects.filter(title__icontains='Django')
How would we filter for all books with tag ‘Fiction’?
- fiction_books = Book.objects.filter(tags__name__contains='Fiction')
How would we filter for all authors who have written books containing the word ‘Django’?
- django_book_authors = Author.objects.filter(book_title__icontains='Django')
