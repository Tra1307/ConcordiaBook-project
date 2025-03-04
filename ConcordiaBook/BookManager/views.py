from django.shortcuts import render
from .models import Textbooks
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .forms import TextbookForm

# Create your views here.

#to view all available textbooks
class AllTextbooksListView(ListView):
    model = Textbooks 
    template_name = "textbooks/all_textbooks.html"
    context_object_name = "textbooks"
    
    def get_queryset(self):
        return Textbooks.objects.filter(availability=True)
    
    # def get_queryset(self):
    #     textbooks = Textbooks.objects.all()
    #     print(textbooks)  # This will show what data is being queried in the console

    #     return textbooks






#to view available textbooks by coursecode
class TextbookListView(ListView):
    model = Textbooks
    template_name = "textbooks/textbook_list.html"
    context_object_name = "textbooks"

    def get_queryset(self):
        course_code = self.kwargs.get('course_code') 
        return Textbooks.objects.filter(course_code=course_code, availability=True)  







#View for adding textbooks (form)
class TextbookCreateView(CreateView):
    model = Textbooks
    form_class = TextbookForm
    template_name = "textbooks/textbook_form.html"
    #fields = ['title', 'author', 'edition', 'condition', 'course_code']
    success_url = reverse_lazy('textbook_list')  # Redirect after form submission

    def get_success_url(self):
        course_code = self.object.course_code
        return reverse_lazy('textbook_list', kwargs={'course_code': course_code})

 

#view for editing entries
class TextbookUpdateView(UpdateView):
    model = Textbooks
    form_class = TextbookForm
    template_name = "textbooks/textbook_form.html"
    success_url = reverse_lazy('all_textbooks')