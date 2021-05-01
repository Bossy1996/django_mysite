import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question
# Create your tests here.

class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_questions(self):
        """
        was_published_recently() returns false for questions
        whose pub_date is in the furute.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)

        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_questions(self):
        """
        was_published_recently() returns false for questions whose pub_date is older
        that 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_questions = Question(pub_date=time)

        self.assertIs(old_questions.was_published_recently(), False)

    def test_was_published_recently_with_recent_questions(self):
        """
        was_published_recently() returns True for questions whose pub_date is 
        within the las day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_questions = Question(pub_date=time)

        self.assertIs(recent_questions.was_published_recently(), True)