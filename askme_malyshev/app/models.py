from django.db import models
from django.contrib.auth.models import User

# Create your models here.

### example ###

# class Genre(models.Model):
#     name = models.CharField(max_length=30)

# class Author(models.Model):
#     name = models.CharField(max_length=30)
#     birth_date = models.DateField(blanck=True, null=True)

# class Book(models.Model):
#     name = models.CharField(max_length=30)
#     genre = models.ManyToManyField(Genre)
#     author = models.ManyToManyField(Author)
#     published_date = models.DateField(blanck=True, null=True)

# class BookInstance(models.Model):
#     book = models.ForeignKey(Book, on_delete=models.PROTECT)
#     # available
#     # taken
#     # repair

#     TAKEN = 't'
#     AVAILABLE = 'a'
#     REPAIR = 'r'

#     STATUCES = [
#         (TAKEN, 'taken'),
#         (AVAILABLE, 'available'),
#         (REPAIR, 'repair'),
#     ]

#     status = models.CharField(max_length=1, choices=STATUCES)

###


TEXT_LENGTH = 500
NAME_LENGTH = 100
PREVIEW_LEN = 10

class UserProfileModel(User):

    picture = models.ImageField(blank=True, null=True)

    def __str__(self):
        return f'User: {self.get_short_name()}'

    class UserProfileModelManager(models.Manager):
        
        def get_smth(self):
            return 0
    
    objects = UserProfileModelManager()

class TagModel(models.Model):
    name = models.TextField(max_length=NAME_LENGTH)

    def __str__(self):
        return f'Tag: {self.name[:PREVIEW_LEN]}'



class QuestionModel(models.Model):
    name = models.TextField(max_length=NAME_LENGTH)
    text = models.TextField(max_length=TEXT_LENGTH)
    
    user_profile = models.ForeignKey(UserProfileModel, on_delete=models.CASCADE)
    tag = models.ManyToManyField(TagModel)

    def __str__(self):
        return f'Question: {self.name[:PREVIEW_LEN]}'

class AnswerModel(models.Model):
    text = models.TextField(max_length=TEXT_LENGTH)
    correct = models.BooleanField(default=False)

    question = models.ForeignKey(QuestionModel, on_delete=models.CASCADE)
    user_profile = models.ForeignKey(UserProfileModel, on_delete=models.CASCADE)

    def __str__(self):
        return f'Question: {self.text[:PREVIEW_LEN]}'

class LikeModel(models.Model):

    user_profile = models.ForeignKey(UserProfileModel, on_delete=models.CASCADE)
    question = models.ForeignKey(QuestionModel, on_delete=models.CASCADE)

    def __str__(self):
        return f'Question: {self.user.get_short_name()}'





TAGS = [
    {
        'title': f'TAG-{i+1}'
    } for i in range(50)
]

ANSWERS = [
    {
        'id': i,
        'text': f'answer-{i}' * ((i * i * i * i) % 200 + 1),
        'likes': (i * i) % 773,
        'is_correct': False
    } for i in range(100)
]

QUESTIONS = [
    {
        'id': i,
        'title': f'question-{i}',
        'text': f'text-{i}' * ((i * i * i * i) % 100 + 1),
        'likes': (i * i) % 773,
        'answer_amount': (i * i * i) % 773,
        'tags': [
            TAGS[i % len(TAGS)],
            TAGS[(i * i) % len(TAGS)],
            TAGS[(i * i * i) % len(TAGS)],
            TAGS[(i * i * i * i) % len(TAGS)]
        ],
        'answers': [
            ANSWERS[(j * j * j + i * i * i + i * j + 4567) % len(ANSWERS)] for j in range(30)
        ],
    } for i in range(100)
]

USERS = [
    {
        'name': f'user-{i+1}'
    } for i in range(25)
]

