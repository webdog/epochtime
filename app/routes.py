from app import app
from epoch.times import EpochTime

@app.route('/')
@app.route('/index')
def index():
    return EpochTime().value()
    
