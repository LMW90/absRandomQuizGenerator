#! python3
# randomQuizenerator.py = genereates quizzes in random order along with answer key
import random
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock', 'California': 'Sacramento',
'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahasse', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu',
 'Idaho': 'Boise', 'Illinois': 'Sprngfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort',
 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 'Lansing',
 'Minnesota': 'Saint Paul', 'Mississipi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln',
 'Nevada': 'Carlson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany',
 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem',
 'Pennsylvania': 'Harrisbourg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia', 'South Dakota': 'Pierre',
 'Tennessee': 'Nashvilee', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond', 
 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

for quizNum in range(35):
    # create quiz and answer files
    quizFile = open(f'capitalsquiz{quizNum + 1}.txt', 'w')
    answerKeyFile = open(f'capitalsquizanswer{quizNum + 1}.txt', 'w')
    # write quiz header
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write(' ' * 20 + f'State Capitals Quiz (Form {quizNum +1})')
    quizFile.write('\n\n')
    # shuffle the order of the states
    states = list(capitals.keys())
    random.shuffle(states)

    for questionNum in range(50):
        # determine correnct answer
        correctAnswer = capitals[states[questionNum]]
        # generate list of capitals, remove correct anwser from the list
        wrongAnswer = list(capitals.values())
        del wrongAnswer[wrongAnswer.index(correctAnswer)]
        # pick 3 random wrong anwsers
        wrongAnswer = random.sample(wrongAnswer, 3)
        # append correct answe
        answerOptions = wrongAnswer + [correctAnswer]
        # shuffle
        random.shuffle(answerOptions)
        # write out questions
        quizFile.write(f'{questionNum + 1}. What is the capital of {states[questionNum]}?\n')
        # write 4 options for each question
        abcd = 'ABCD'
        for i in range(4):
            quizFile.write(f'     {abcd[i]}. {answerOptions[i]}\n')
        quizFile.write('\n')
        # write answers int answerKeyFile
        answerKeyFile.write(f'{questionNum + 1}. {abcd[answerOptions.index(correctAnswer)]}\n')
    # cleanup
    quizFile.close()
    answerKeyFile.close()
