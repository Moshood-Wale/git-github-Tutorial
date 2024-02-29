from django.test import TestCase
from .models import Question, Choice
from django.utils import timezone
import datetime


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        future_question = Question(pub_date=timezone.now() + timezone.timedelta(days=30))

        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        old_question = Question(pub_date=timezone.now() - timezone.timedelta(days=1, seconds=1))

        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        recent_question = Question(pub_date=timezone.now() - timezone.timedelta(hours=23, minutes=59, seconds=59))

        self.assertIs(recent_question.was_published_recently(), True)


class ChoiceModelTests(TestCase):
    def test_choice_str_representation(self):
        question = Question.objects.create(question_text="What's your favorite color?", pub_date=timezone.now())
        choice = Choice.objects.create(question=question, choice_text="Blue")

        self.assertEqual(choice.__str__(), "Blue")        



