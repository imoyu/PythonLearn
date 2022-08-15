from survey import AnonymousSurvey
import unittest


class AnonymousSurveyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        print('setUP ------')
        self.question = 'What language did you first learn to speak?'
        self.responses = ['English', 'Japanese', 'Chinese']

    def test_store_single_question(self):
        survey = AnonymousSurvey(self.question)
        survey.store_response('English')

        self.assertIn('English', survey.responses)

    def test_store_tree_questions(self):
        survey = AnonymousSurvey(self.question)
        for response in self.responses:
            survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, survey.responses)
