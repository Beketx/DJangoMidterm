from rest_framework.routers import DefaultRouter
from .views import *
router = DefaultRouter()
router.register(r'books', BookViewSet, basename='books')
router.register(r'journals', JournalViewSet, basename='journal')


urlpatterns = router.urls