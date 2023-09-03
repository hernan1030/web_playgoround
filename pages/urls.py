from django.urls import path
from .views import PagesListViews, PageDatailViews, PageCreateViews, PageUpdateViews, PageDeleteViews


urlpatterns = [
    path('', PagesListViews.as_view(), name="pages",),
    path('<int:pk>/', PageDatailViews.as_view(), name="page",),
    path('create/', PageCreateViews.as_view(), name="create",),
    path('update/<int:pk>/', PageUpdateViews.as_view(), name="update",),
    path('delete/<int:pk>/', PageDeleteViews.as_view(), name="delete",),
]
