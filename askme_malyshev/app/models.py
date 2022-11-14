from django.db import models

# Create your models here.

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

