Hello,

Welcome to my script!

the follow directory has three components:
1. generator-windows-amd64, a blackbox shooting out infine data stream just waiting to be catched.
2. source.py, the main service script that save the data stream into a json file called "data.txt"
3. server.py, a simple flask server that enables you to see the data parsed as json.

In order run this scripts you will need to:
1. open a cmd, go to the directory and run source.py with python ("python source.py")
2. open a second cmd, go to the directory and run server.py with python ("python server.py")

Now you can go to the url:
http://127.0.0.1:5000/

And check the instructions there for seeing the parsed json data


Things I would improve in my submission:
1. I would certainly would write my code cleaner and more readable.
2. I would get more familliar with reactive programming


With that said, I tried not to over-engineered as suggested in the challenge, and I have actually handeld it as a speed code test.

Thanks and Enjoy!!