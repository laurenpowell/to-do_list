from django.urls import path
from . import views

urlpatterns = [
    path("todo/", views.ToDoView.as_view(), name="todo"),
    path("personal/", views.PersonalView.as_view(), name="personal"),
    path("work/", views.WorkView.as_view(), name="work"),
    path("shopping/", views.ShoppingView.as_view(), name="shopping"),
    path("wishlist/", views.WishlistView.as_view(), name="wishlist"),

    path("list/add/", views.ListCreate.as_view(), name="list-add"),
    path("list/<int:list_id>/item/add/", views.TaskCreate.as_view(), name="task-add"),

    path('detail/<int:pk>/', views.ListDetail.as_view(), name='list-detail'),
    path('detail/<int:pk>/list-edit/', views.ListEdit.as_view(), name='list-edit'),
    path('detail/task-edit/<int:pk>/', views.TaskEdit.as_view(), name='task-edit'),
    path("detail/<int:pk>/delete/", views.ListDelete.as_view(), name="list-delete"),
    path("detail/<int:list_id>/task-delete/<int:pk>/",views.TaskDelete.as_view(),name="task-delete"),



]