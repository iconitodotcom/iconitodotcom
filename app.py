#iconitodotcom/app.py
from iconitodev import app
from waitress import serve

if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=5000) # Non-prod and prod
    #app.run(debug=True,port=5000) # test