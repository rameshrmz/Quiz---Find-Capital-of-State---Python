Capitals_dict = {
		'Tamilnadu' : 'Chennai',
		'Karnataka' : 'Bangalore',
		'Maharastra' : 'Mumbai',
		'Kerala' : 'Thiruvananthapuram',
		'AndhraPradesh' : 'Amaravati',
		'Telungana' : 'Hyderabad'
}

import random

states = list(Capitals_dict.keys())

for i in [1,2,3,4,5]:
	State = random.choice(states)
	Capital = Capitals_dict[State] 
	Capital_guess = input("What is the Capital of " + State + " ?")
        
	if (Capital_guess == Capital):
		print("Correct Answer. Good Job!!!")
	else:
		print("Wrong Answer. Capital of " + State + " is " + Capital + ".")

print("All Done!!!")