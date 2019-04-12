from rest_framework.routers import DefaultRouter

from app_kochbuch.views.category import ViewCategory
from app_kochbuch.views.favourite import ViewFavourite
from app_kochbuch.views.ingredient import ViewIngredient
from app_kochbuch.views.rating import ViewRating
from app_kochbuch.views.recipe import ViewRecipe
from app_kochbuch.views.recipecategory import ViewRecipeCategory
from app_kochbuch.views.severity import ViewSeverity
from app_kochbuch.views.unit import ViewUnit
from app_kochbuch.views.user import ViewUser

router = DefaultRouter()
router.register(r'unit', ViewUnit, base_name='unit')
router.register(r'severity', ViewSeverity, base_name='severity')
router.register(r'recipe', ViewRecipe, base_name='recipe')
router.register(r'rating', ViewRating, base_name='rating')
router.register(r'ingredient', ViewIngredient, base_name='ingredient')
router.register(r'category', ViewCategory, base_name='category')
router.register(r'user', ViewUser, base_name='user')
router.register(r'favourite', ViewFavourite, base_name='favourite')
router.register(r'recipecategory', ViewRecipeCategory, base_name='recipecategory')
urlpatterns = router.urls