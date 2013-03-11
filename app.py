
# initialize the newrelic agent first, development environment
import newrelic.agent
newrelic.agent.initialize('newrelic.ini', 'development')

# now proceed to initialize the Flask app as normal
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
