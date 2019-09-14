# Virtual-Assistant
Here I created Virtual Assistant through following steps;
1.WolframAlpha : http://developer.wolframalpha.com/portal/myapps/
Visit here create account and get the key to use api. 
>>>pip install wolframalpha
now you can use it in your assistant.
Code refference : https://pypi.org/project/wolframalpha/
2.Wikipedia
>>>pip install wikipedia
Code refference : https://pypi.org/project/wikipedia/
We can use some conditions for wikipedia. First to limit the number of sentences to be displayed and other is the language.
wikipedia.summary(user_input,sentences=3)
wikipedia.set_lang("es")
