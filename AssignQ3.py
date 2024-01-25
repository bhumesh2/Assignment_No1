"""Q3. In DevOps, automating configuration management tasks is essential for maintaining consistency and managing infrastructure efficiently.
●       The program should read a configuration file (you can provide them with a sample configuration file).
●       It should extract specific key-value pairs from the configuration file.
●       The program should store the extracted information in a data structure (e.g., dictionary or list).
●       It should handle errors gracefully in case the configuration file is not found or cannot be read.
●       Finally save the output file data as JSON data in the database.
●       Create a GET request to fetch this information."""

#import add
#importing flask
from flask import Flask, request, jsonify

database=[{"host":"localhost","port":3306, "username":"admin", "password":"secret"}, {"address":"192.168.0.1", "port":8080}]
#create the server
app = Flask(__name__)

####Root
@app.route("/")   #decorator
def Database():
    print ("*****Database*****")
    return "<H1>Database (information of server and data)</H1>"

@app.route("/database",methods=['GET'])
def api():
    if(request.method=='GET'):
        return (jsonify(database))
    #elif(request.method == 'POST'):

    jsonData = request.get_json
    print(request.get_json)
    #sample.append(jsonData)
    #return jsonify("new data is added")
    

if (__name__ == "__main__"):
    app.run(debug=True)