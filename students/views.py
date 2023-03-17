from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, HttpResponse, redirect
from django.urls import reverse
from .forms import *
from django.contrib import messages
from datetime import datetime
from payments.models import *
from qrcode import *
from django.conf import settings
import time

# Course Views
def addCourse(request):
    form = CourseForm(request.POST or None)
    context = {
        'form': form,
        'page_title': 'Add Course'
    }
    if request.method == 'POST':
        if form.is_valid():
            name = form.cleaned_data.get('name')
            try:
                course = Course()
                course.name = name
                course.save()
                messages.success(request, "Successfully Added")
                return HttpResponseRedirect("/students/add_course")
            except:
                messages.error(request, "Could Not Add")
        else:
            messages.error(request, "Could Not Add")
    return render(request, 'hod_template/add_course_template.html', context)

def manageCourse(request):
    courses = Course.objects.all()
    context = {
        'courses': courses,
        'page_title': 'Manage Courses'
    }
    return render(request, "hod_template/manage_course.html", context)

def editCourse(request, course_id):
    instance = get_object_or_404(Course, id=course_id)
    form = CourseForm(request.POST or None, instance=instance)
    context = {
        'form': form,
        'course_id': course_id,
        'page_title': 'Edit Course'
    }
    if request.method == 'POST':
        if form.is_valid():
            name = form.cleaned_data.get('name')
            try:
                course = Course.objects.get(id=course_id)
                course.name = name
                course.save()
                messages.success(request, "Successfully Updated")
            except:
                messages.error(request, "Could Not Update")
        else:
            messages.error(request, "Could Not Update")

    return render(request, 'hod_template/edit_course_template.html', context)

def deleteCourse(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    try:
        course.delete()
        messages.success(request, "Course deleted successfully!")
    except Exception:
        messages.error(
            request, "Sorry, some Batches are assigned to this course already. Kindly change the affected Batches and try again")
    return HttpResponseRedirect("/students/manage_course")

# Batch Views
def addBatch(request):
    form = BatchForm(request.POST or None)
    context = {
        'form': form,
        'page_title': 'Add Batch'
    }
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Batch Added Successfully")
            return HttpResponseRedirect("/students/add_batch")
        else:
            messages.error(request, "Fill the Form Properly")

    return render(request, 'hod_template/add_subject_template.html', context)

def manageBatch(request):
    batches = Batch.objects.all()
    context = {
        'batches': batches,
        'page_title': 'Manage Batches'
    }
    return render(request, "hod_template/manage_subject.html", context)

def editBatch(request, batch_id):
    instance = get_object_or_404(Batch, id=batch_id)
    form = BatchForm(request.POST or None, instance=instance)
    context = {
        'form': form,
        'course_id': batch_id,
        'page_title': 'Edit Batch'
    }
    if request.method == 'POST':
        if form.is_valid():
            # name = form.cleaned_data.get('name')
            # course = form.cleaned_data.get('course')
            # try:
            #     batch = Batch.objects.get(id=batch_id)
            #     batch.name = name
            #     batch.course = course
            #     batch.save()
            form.save()
            messages.success(request, "Successfully Updated")
            # except:
            #     messages.error(request, "Could Not Update")
        else:
            messages.error(request, "Could Not Update")

    return render(request, 'hod_template/edit_subject_template.html', context)

def deleteBatch(request, batch_id):
    batch = get_object_or_404(Batch, id=batch_id)
    try:
        batch.delete()
        messages.success(request, "Course deleted successfully!")
    except Exception:
        messages.error(
            request, "Sorry, some students are assigned to this Batch already. Kindly change the affected students to this Batch and try again")
    return HttpResponseRedirect("/students/manage_batch")

# Student Views
def addStudent(request):
    student_form = StudentForm(request.POST or None, request.FILES or None)
    context = {'form': student_form, 'page_title': 'Add Student'}
    if request.method == 'POST':
        if student_form.is_valid():
            payment_mode = student_form.cleaned_data['payment_mode']
            # admission_fees = student_form.cleaned_data['admission_fees']
            name = student_form.cleaned_data['name']
            batch = student_form.cleaned_data['batch']

            training_fees = student_form.cleaned_data['training_fees']
            food_and_lodging_fees = student_form.cleaned_data['food_and_lodging_fees']
            uniform_fees = student_form.cleaned_data['uniform_fees']
            shoes_fees = student_form.cleaned_data['shoes_fees']
            ccrup_fees = student_form.cleaned_data['ccrup_fees']
            cap_fees = student_form.cleaned_data['cap_fees']
            belt_fees = student_form.cleaned_data['belt_fees']
            admission_fees = student_form.cleaned_data['admission_fees']
            membership_fees = student_form.cleaned_data['membership_fees']

            student1 = student_form.save()

            applying_for = "Hindustan Scout and Guides"

            registrationNumber = "TRS-"+str(student1.id)+"-"+datetime.now().strftime('%y')
            img = make(registrationNumber)
            img_name = 'qr' + str(time.time()) + '.png'
            img.save(settings.MEDIA_ROOT + '/qrcodes/' + img_name)
            try:
                RegistrationNumber.objects.create(
                    registration_number = registrationNumber,
                    student = student1,
                    qr_code = f"qrcodes/{img_name}"
                ).save()
                scout_payment = ScoutPayment.objects.create(
                student = student1,
                training_fees = training_fees,
                food_and_lodging_fees = food_and_lodging_fees,
                uniform_fees = uniform_fees,
                shoes_fees = shoes_fees,
                ccrup_fees = ccrup_fees,
                cap_fees = cap_fees,
                belt_fees = belt_fees,
                admission_fees = admission_fees,
                membership_fees = membership_fees
                )
                scout_payment.save()
                if payment_mode == "ONLINE":
                    return HttpResponseRedirect(f"/payments/initiate/{student1.id}/{scout_payment.id}/fees for {applying_for}/Student {name} getting admitted to TRS APD for {applying_for} Course.")
            except:
                messages.error(request, "Please Try Again Later")

            messages.success(request, "Student Added Successfully")
        else:
            messages.error(request, "Could Not add Student")
    return render(request, 'hod_template/add_student_template.html', context)

def manageStudents(request):
    students = RegistrationNumber.objects.all()
    context = {
        'students': students,
        'page_title': 'Manage Students'
    }
    return render(request, "hod_template/manage_student.html", context)

def editStudent(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    form = StudentForm(request.POST or None, request.FILES or None, instance=student)
    context = {
        'form': form,
        'student_id': student_id,
        'page_title': 'Edit Student'
    }
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully Updated")
            return HttpResponseRedirect("/students/manage_students/")
        else:
            messages.error(request, "Please Fill Form Properly!")
    else:
        return render(request, "hod_template/edit_student_template.html", context)

def deleteStudent(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    registration_number = RegistrationNumber.objects.filter(student=student).last()
    registration_number.delete()
    messages.success(request, "Student deleted successfully!")
    return HttpResponseRedirect("/students/manage_students")

def studentProfile(request,registration_number):
    registered = RegistrationNumber.objects.filter(registration_number=registration_number).last()
    payments = Payment.objects.filter(student=registered.student)
    context = {
        'registered': registered,
        'payments':payments,
    }
    return render(request, "hod_template/student_profile.html",context)

# Add Staff view
def addStaff(request):
    staff_form = StaffForm(request.POST or None)
    staffs = User.objects.filter(is_superuser=False)
    context = {'form': staff_form, 'page_title': 'Add Staff','staffs':staffs}
    if request.method == 'POST':
        if staff_form.is_valid():
            staff_form.save()
            messages.success(request, "Staff Added Successfully")
        else:
            messages.error(request, "A Staff With the Phone number already Exists!")
    return render(request, 'hod_template/add_staff_template.html', context)

def deleteStaff(request,staff_id):
    User.objects.filter(id=staff_id).delete()
    messages.success(request, "Staff Deleted Successfully!")
    return HttpResponseRedirect("/students/add_staff")


