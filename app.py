# we are for build web application that we will ask flash here
#pip install Flask
#module from flash installed then we need to use class Flash
# We are importing the class and we r creating object of the class
#https://www.youtube.com/watch?v=yBDHkveJUf4
#https://jovian.com/learn/web-development-with-python-and-flask
#hmtldog.com , if you want to lean hlm 
#excalidraw.com 

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello_world():
  return "Hello Juhi Singh , how you are doing Good morning"
  #return render_template('home.html')

if __name__ == "__main__":
  print("I am inside if")
  
  app.run(host="0.0.0.0", debug=True)
