from flask import Flask, render_template


from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"


# ALL ROUTES 

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello():
    return "HELLO FLASK"

@app.route('/play')          # The "@" decorator associates this route with the function immediately following
@app.route('/play/<int:x>')          # The "@" decorator associates this route with the function immediately following
@app.route('/play/<int:x>/<string:color>')          # The "@" decorator associates this route with the function immediately following
def changeColor(x = 3, color = 'skyblue'):
    return render_template("play.html", x=x, color=color)




if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.