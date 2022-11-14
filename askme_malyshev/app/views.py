from django.http import Http404
from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator

from .models import QUESTIONS, TAGS, USERS

OBJECTS_PER_PAGE = 10

# Create your views here.

class IndexView(View):
    template_name = 'index.html'

    def get(self, request):
        questions = QUESTIONS
        paginator = Paginator(questions, OBJECTS_PER_PAGE)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'tags': TAGS,
            'users': USERS[:10],
            'page_obj': page_obj
        }
        return render(request, template_name=self.template_name, context=context)


class HotView(View):
    template_name = 'index.html'

    def get(self, request):
        questions = QUESTIONS.copy()
        questions.sort(key=lambda e: -e['likes'])
        paginator = Paginator(questions, OBJECTS_PER_PAGE)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'tags': TAGS,
            'users': USERS[:10],
            'is_hot': True,
            'page_obj': page_obj
        }
        return render(request, template_name=self.template_name, context=context)


class QuestionView(View):
    template_name = 'question.html'

    def get(self, request, id):

        question = list(filter(lambda e: e['id'] == id, QUESTIONS))
        if not question:
            raise Http404
        question = question[0]

        answers = question['answers']
        paginator = Paginator(answers, OBJECTS_PER_PAGE)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'question': question,
            'page_obj': page_obj,
            'tags': TAGS,
            'users': USERS[:10]
        }
        return render(request, template_name=self.template_name, context=context)


class AskView(View):
    template_name = 'ask.html'

    def get(self, request):
        context = {
            'tags': TAGS,
            'users': USERS[:10]
        }
        return render(request, template_name=self.template_name, context=context)


class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        context = {
            'tags': TAGS,
            'users': USERS[:10]
        }
        return render(request, template_name=self.template_name, context=context)


class SignupView(View):
    template_name = 'signup.html'

    def get(self, request):
        context = {
            'tags': TAGS,
            'users': USERS[:10]
        }
        return render(request, template_name=self.template_name, context=context)


class SettingsView(View):
    template_name = 'settings.html'

    def get(self, request):
        context = {
            'tags': TAGS,
            'users': USERS[:10]
        }
        return render(request, template_name=self.template_name, context=context)


class TagView(View):
    template_name = 'tag.html'

    def get(self, request, slug):
        tag = list(filter(lambda e: e['title'] == slug, TAGS))
        if not tag:
            raise Http404
        tag = tag[0]

        questions = []
        for q in QUESTIONS:
            for qt in q['tags']:
                if qt['title'] == tag['title']:
                    questions.append(q)
                    break
        
        paginator = Paginator(questions, OBJECTS_PER_PAGE)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'tags': TAGS,
            'users': USERS[:10],
            'tag': tag,
            'page_obj': page_obj
        }
        return render(request, template_name=self.template_name, context=context)
