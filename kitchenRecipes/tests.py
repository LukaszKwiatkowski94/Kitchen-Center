from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from kitchenRecipes.models import Category, DifficultyLevel, Recipes, Ingredient, Instruction, RecipeRating
from django.contrib.auth import get_user_model

User = get_user_model()

class CategoryModelTest(TestCase):

    def test_category_str(self):
        category = Category(categoryName='Test Category')
        self.assertEqual(str(category), 'Test Category')

class DifficultyLevelModelTest(TestCase):

    def test_difficulty_level_str(self):
        difficulty_level = DifficultyLevel(name='Easy')
        self.assertEqual(str(difficulty_level), 'Easy')

class RecipesModelTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(categoryName='Test Category')
        self.difficulty_level = DifficultyLevel.objects.create(name='Easy')
        self.user = User.objects.create(email='test@example.com', username='testuser', password='testpassword')
        self.recipe = Recipes.objects.create(
            name='Test Recipe',
            description='Test description',
            category=self.category,
            image=SimpleUploadedFile('test_image.jpg', b'file_content'),
            author=self.user,
            difficulty_level=self.difficulty_level
        )

    def test_recipe_str(self):
        self.assertEqual(str(self.recipe), '[1]: Test Recipe')

class IngredientModelTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(categoryName='Test Category')
        self.difficulty_level = DifficultyLevel.objects.create(name='Easy')
        self.user = User.objects.create(email='test@example.com', username='testuser', password='testpassword')
        self.recipe = Recipes.objects.create(
            name='Test Recipe',
            description='Test description',
            category=self.category,
            image=SimpleUploadedFile('test_image.jpg', b'file_content'),
            author=self.user,
            difficulty_level=self.difficulty_level
        )

    def test_ingredient_str(self):
        ingredient = Ingredient(name='Test Ingredient', quantity='200g', unit='grams', recipe=self.recipe)
        self.assertEqual(str(ingredient), 'Test Ingredient 200g')

class InstructionModelTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(categoryName='Test Category')
        self.difficulty_level = DifficultyLevel.objects.create(name='Easy')
        self.user = User.objects.create(email='test@example.com', username='testuser', password='testpassword')
        self.recipe = Recipes.objects.create(
            name='Test Recipe',
            description='Test description',
            category=self.category,
            image=SimpleUploadedFile('test_image.jpg', b'file_content'),
            author=self.user,
            difficulty_level=self.difficulty_level
        )

    def test_instruction_str(self):
        instruction = Instruction(order=1, description='Test Description', recipe=self.recipe)
        self.assertEqual(str(instruction), 'Step 1: Test Description')

class RecipeRatingModelTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(categoryName='Test Category')
        self.difficulty_level = DifficultyLevel.objects.create(name='Easy')
        self.user = User.objects.create(email='test@example.com', username='testuser', password='testpassword')
        self.recipe = Recipes.objects.create(
            name='Test Recipe',
            description='Test description',
            category=self.category,
            image=SimpleUploadedFile('test_image.jpg', b'file_content'),
            author=self.user,
            difficulty_level=self.difficulty_level
        )

    def test_recipe_rating_str(self):
        recipe_rating = RecipeRating(recipe=self.recipe, user=self.user, rating=5)
        self.assertEqual(str(recipe_rating), 'Rating for Recipe Test Recipe: 5')
