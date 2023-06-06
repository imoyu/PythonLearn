class AnonymousSurvey:
    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_question(self):
        print(self.question)

    def store_response(self, new_response):
        self.responses.append(new_response)

    def show_responses(self):
        print('Survey result:')
        for response in self.responses:
            print('- ' + response)


if __name__ == '__main__':
    question = 'What language did you first learn to speak?'
    survey = AnonymousSurvey(question)

    survey.show_question()
    print('Enter q to quit survey')
    while True:
        response = input('Language: ')
        if response == 'q':
            break
        survey.responses.append(response)

    survey.show_responses()
