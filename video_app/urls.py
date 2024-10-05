from django.urls import path, include
from . import views
from .media_views import upload_media, delete_media, edit_media, like_media
from .session_views import start_session, session, pause_session, delete_session, generate_users_for_section
from .auth_views import student_login, student_logout, update_teacher_info
from django.contrib.auth import login as auth_login 
from django.contrib import admin
from .student_management_views import download_students, delete_student, student_detail

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Authentication
    path('student-login/', student_login, name='student_login'),
    path('student-logout/', student_logout, name='student_logout'),
    path('login/', auth_login, name='login'),
    path('accounts/', include('django.contrib.auth.urls')),

    # Media
    path('upload/<int:session_pk>/', upload_media, name='upload_media'),
    path('delete-media/<int:pk>/', delete_media, name='delete_media'),
    path('edit-media/<int:pk>/', edit_media, name='edit_media'),
    path('like/<int:media_id>/', like_media, name='like_media'),
    path('like-media/<int:media_id>/<str:like_type>/', like_media, name='like_media'),
    path('filter_media/<int:session_pk>/', views.filter_media, name='filter_media'),
    path('set-media-password/', views.set_media_password, name='set_media_password'),

    # Sessions
    path('start-session/', start_session, name='start_session'),
    path('session/<int:session_pk>/', session, name='session'),
    path('session/<int:session_pk>/delete/', delete_session, name='delete_session'), 
    path('session/<int:session_pk>/pause/', pause_session, name='pause_session'),
    path('join-session/<str:session_code>/', student_login, name='student_login'),

    # Students
    path('download-students/', download_students, name='download_students'),
    path('delete-student/<int:student_id>/', delete_student, name='delete_student'),
    path('generate-students/', generate_users_for_section, name='generate_students'),
    path('student/<int:student_id>/', student_detail, name='student_detail'),

    # Miscellaneous
    path('', views.index, name='home'),
    path('post/<int:id>/', views.post, name='post'),
    path('teacher_view/', views.teacher_view, name='teacher_view'),
    path('delete-comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('update_teacher_info/', update_teacher_info, name='update_teacher_info'),
]