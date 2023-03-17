from django.urls import path, include
from .import views
urlpatterns = [
    # path('', views.index),

    path('add_course',views.addCourse),
    path('manage_course',views.manageCourse),
    path('edit_course/<int:course_id>/',views.editCourse),
    path('delete_course/<int:course_id>/',views.deleteCourse),

    path('add_batch',views.addBatch),
    path('manage_batch',views.manageBatch),
    path('edit_batch/<int:batch_id>/',views.editBatch),
    path('delete_batch/<int:batch_id>/',views.deleteBatch),

    path('add_student/',views.addStudent),
    path('student_profile/<str:registration_number>/',views.studentProfile),
    path('manage_students/',views.manageStudents),
    path('edit_student/<int:student_id>/',views.editStudent),
    path('delete_student/<int:student_id>/',views.deleteStudent),

    path('add_staff/',views.addStaff),
    path('delete_staff/<int:staff_id>/',views.deleteStaff),
]
