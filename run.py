""" Web app to create a database of heights 
and sending the data through email """




from app import app



if __name__ == '__main__':
    app.debug=True
    app.run(port=5000)
