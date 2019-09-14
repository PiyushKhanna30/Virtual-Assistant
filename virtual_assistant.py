import wikipedia
import wolframalpha
while (True):
	user_input = input("Question: ")
	try:
		try:
			app_id = "******-**********"            #Your app id
			client = wolframalpha.Client(app_id)
			res = client.query(user_input)
			answere = next(res.results).text
			print(answere)
		except:	
			answere = wikipedia.summary(user_input)
			print(answere)
	except:
		print("Some error encountered")