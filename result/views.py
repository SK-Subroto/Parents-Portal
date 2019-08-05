from django.shortcuts import render
from .models import Result
from student.models import Student
from admission.models import Admission


def resultSearch(request):
    return render(request, 'result/result.html')

def viewResult(request):
    if request.method=='POST':
        stu_id = request.POST['student_id']
        clss_no = request.POST['class_no']
        results = Result.objects.filter(admission_id__student__stu_id = stu_id, admission_id__clss = clss_no)
        subjects = Admission.objects.filter(student__stu_id = stu_id)
        student = Student.objects.filter(stu_id = stu_id).first()
        result = zip(subjects, results)
        context = {
            'results' : result,
            'student' : student
        }
    
    return render(request, 'result/showResult.html', context)
