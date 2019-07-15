import random

Capitals_dict = {
		'Tamilnadu' : 'Chennai',
		'Karnataka' : 'Bangalore',
		'Maharastra' : 'Mumbai',
		'Kerala' : 'Thiruvananthapuram',
		'AndhraPradesh' : 'Amaravati',
		'Telungana' : 'Hyderabad'
}

States_List = list(Capitals_dict.keys())
random_states = random.sample(States_List,5)
Score = 0


for i in range(0,5):
    State = random_states[i]
    Capitals_rstates = Capitals_dict[State]
    Guess_capital = input("What is the capital of ''" + State + "''?")
    
    if Capitals_rstates == Guess_capital.title():
        print ("Correct Answer. Good Job!!!\n")
        Score += 1
    else:
        print ("Wrong Answer. Capital of " + State + " is '" + Capitals_rstates + "'.\n")
        
Score_percentage = Score * 20        
print ("Thanks for playing!!! You got " + str(Score_percentage) + "% score")
     