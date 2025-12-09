from django.shortcuts import get_object_or_404, redirect, render

from core.models import Student

from django.db.models import Q 

# Create your views here.

def home(request):
    
    return render(request, "index.html")



def add_student(request):
    
    if request.method == "POST":
        Student.objects.create(
            student_id = int(request.POST.get('student_id')),
            full_name = request.POST.get('full_name'),
            department = request.POST.get('department'),
            dob = request.POST.get('dob'),
            gender = request.POST.get('gender'),
            address = request.POST.get('address')
        )
        return redirect('all_student')
    
    return render(request, 'student/add_student.html')


def all_student(request):
    
    query = request.GET.get('query')
    
    if query:
        data = Student.objects.filter(
            Q(full_name__icontains = query)|
            Q(student_id__icontains = query)
            )
        
    else:
       data = Student.objects.all() 
    
    
    order = request.GET.get('order')
    
    if order == 'asc':
        data = data.order_by('full_name')
    elif order == 'desc':
        data = data.order_by('-full_name')
    
   
    context = {
        "students":data
    }
    
    
    
    
    
    return render(request, 'student/all_student.html', context)


def view_student(request, id):
    student = Student.objects.filter(id=id)
    context = {
        'student': student
    }
    return render(request, 'student/view_student.html', context)




def delete_student(request, id):
    student = Student.objects.filter(id=id)
    student.delete()
    
    return redirect('all_student')

def edit_student(request, id):
    
    student = get_object_or_404(Student, id=id)
    
    context = {
        "student":student
    }
    
    if request.method =="POST":
        student.student_id = int(request.POST.get('student_id'))
        student.full_name = request.POST.get('full_name')
        student.department = request.POST.get('department')
        student.dob = request.POST.get('dob')
        student.gender = request.POST.get('gender')
        student.address = request.POST.get('address')
        
        student.save()
        return redirect('all_student')
    
    return render(request, 'student/edit_student.html', context)
    
    
