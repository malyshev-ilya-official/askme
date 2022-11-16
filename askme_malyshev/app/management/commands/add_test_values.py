from django.core.management.base import BaseCommand
from app import models
from random import randint, shuffle

USER_COUNT = 10000
TAG_COUNT = 10000
QUESTION_COUNT = 100000
ANSWER_COUNT = 1000000

class Command(BaseCommand):
    help = 'generator'

    def handle(self, *args, **options):

        # users = []

        # for i in range(USER_COUNT):
        #     # users.append(models.UserProfileModel(username=f'user-{i}'))
        #     a = models.UserProfileModel(username = f'user-{i}')
        #     a.save()
        
        # models.UserProfileModel.objects.bulk_create(users)

        # tags = []
        # for i in range(TAG_COUNT):
        #     tags.append(models.TagModel(name = f'TAG-{i}'))
        
        # models.TagModel.objects.bulk_create(tags)

        # shuffle(tags)

        # questions = []
        # for i in range(QUESTION_COUNT):
        #     author = models.UserProfileModel.objects.get(pk = randint(1, USER_COUNT - 1))
        #     # qts = randint(0, TAG_COUNT - 30)
        #     # qtf = qts + randint(0, 10)
        #     # qtags = tags[qts:qtf]
        #     title = f'QUESTION-{i}'
        #     text = f'TEXT-{i}-' * randint(1, 10)
        #     q = models.QuestionModel(name = title, text = text, user_profile = author)
        #     # q.tag.set(qtags)
        #     questions.append(q)
        
        # models.QuestionModel.objects.bulk_create(questions)
        
        # tags = models.TagModel.objects.all()
        # shuffle(tags)
        # questions = models.QuestionModel.objects.all()
        # for i in range(len(questions)):
        #     qts = randint(0, len(tags) - 30)
        #     qtf = qts + randint(0, 10)
        #     qtags = tags[qts:qtf]
        #     questions[i].tag.set(qtags)
        # models.QuestionModel.objects.bulk_update(questions)

        answers = []
        us = models.UserProfileModel.objects.all()
        qs = models.QuestionModel.objects.all()
        for i in range(ANSWER_COUNT):
            if i % 1000 == 0:
                print(i)
            # u = models.UserProfileModel.objects.get(pk = (i % USER_COUNT) + 1)
            # q = models.QuestionModel.objects.get(pk = (i % QUESTION_COUNT) + 1)
            u = us[i % USER_COUNT]
            q = qs[i % QUESTION_COUNT]
            text = f'ANSWER-{i}'
            a = models.AnswerModel(text = text, question = q, user_profile = u)
            answers.append(a)
        models.AnswerModel.objects.bulk_create(answers)


