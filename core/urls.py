from django.urls import path
from . import views

urlpatterns = [

    # HOME
    path('', views.home, name='home'),

    # COURSE BROWSING
    path('faculties/', views.faculty_list, name='faculty_list'),
    path('faculty/<slug:slug>/', views.department_list, name='department_list'),
    path('department/<slug:slug>/', views.programme_list, name='programme_list'),
    path(
        'programme/<int:programme_id>/<int:level>/',
        views.level_courses,
        name='level_courses'
    ),

    # COURSE
    path('course/<int:pk>/', views.course_detail, name='course_detail'),

    path(
        'course/<int:course_id>/qa/',
        views.course_qa,
        name='course_qa'
    ),

    # DOWNLOAD PDF
    path(
        'course/<int:course_id>/qa/download/',
        views.course_qa_pdf,
        name='course_qa_pdf'
    ),

    # DOWNLOAD TXT
    path(
        'course/<int:course_id>/qa/download-text/',
        views.download_course_qa,
        name='download_course_qa'
    ),

    path(
        'course/<int:course_id>/enroll/',
        views.enroll_course,
        name='enroll_course'
    ),

    # PLAYER
    path(
        'course/<int:pk>/learn/',
        views.course_player,
        name='course_player'
    ),

    path(
        'course/<int:pk>/learn/<int:lesson_id>/',
        views.course_player,
        name='course_player_lesson'
    ),

    path(
        'lesson/<int:lesson_id>/toggle-complete/',
        views.toggle_lesson_complete,
        name='toggle_lesson_complete'
    ),

    # DASHBOARD
    path('dashboard/', views.dashboard, name='dashboard'),
    path('my-courses/', views.my_courses, name='my_courses'),
    path('explore/', views.explore, name='explore'),
    path('progress/', views.progress, name='progress'),

    # AI
    path('ai-lecturer/', views.ai_lecturer, name='ai_lecturer'),
    path('ai-chat/', views.ai_chat, name='ai_chat'),

    # PUSH
    path(
        'push/vapid-key/',
        views.push_vapid_key,
        name='push_vapid_key'
    ),

    path(
        'push/subscribe/',
        views.push_subscribe,
        name='push_subscribe'
    ),

    path(
        'push/unsubscribe/',
        views.push_unsubscribe,
        name='push_unsubscribe'
    ),

    # AUTH
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('logout/confirm/', views.logout_confirm, name='logout_confirm'),

    path(
        'drop-course/<int:enrollment_id>/',
        views.drop_course,
        name='drop_course'
    ),
    path('lesson/<int:lesson_id>/save-position/', views.save_video_position, name='save_video_position'),
    path('course/<int:course_id>/lesson/<int:lesson_id>/complete/', views.mark_lesson_complete, name='mark_lesson_complete'),
    path('gpa-calculator/', views.gpa_calculator, name='gpa_calculator'),
]