from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.
def index(request):
    sem = Semester.objects.all()
    context = {'sem': sem}
    
    if request.GET.get('semester'):
        semester = Semester.objects.get(id=request.GET.get('semester'))
        context['semester'] = semester
    
    if request.method == 'POST':
        subject_mark_list = request.POST.getlist('subject_mark[]')
        print(subject_mark_list)

        subject_len = len(subject_mark_list)
        total_mark = 0
        
        try:
            for i in subject_mark_list:
                total_mark+=int(i)
        except:
            messages.error(request, 'invalid Input!')
            return redirect(request.META['HTTP_REFERER'])
        
        avarage_mark = total_mark / subject_len
        context['avarage_mark'] = avarage_mark
        
        if 80 <= avarage_mark < 100:
            gpa = 'A+'
            point = 4
        elif 70 <= avarage_mark < 80:
            gpa = 'A'
            point = 3.50
        elif 60 <= avarage_mark < 70:
            gpa = 'A-'
            point = 3.00
        elif 50 <= avarage_mark < 60:
            gpa = 'B'
            point = 2.50
        elif 40 <= avarage_mark < 50:
            gpa = 'C'
            point = 2.00
        elif 33 <= avarage_mark < 40:
            gpa = 'D'
            point = 1.00
        else:
            gpa = 'F'
            point = 0

        context['gpa'] = gpa
        context['point'] = point

    return render(request, 'home.html', context)

