from website import create_app
from flask import * 

app=create_app()

@app.route('/')  
def index():  
    return render_template("home.html")
                                          
if __name__=='__main__':
    app.run(debug=True)    