from flask import Flask, request
import sys, requests, base64
from flask_cors import CORS
import json 
app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/api/v1/rmlst', methods= ['POST'])
def rmlst_proxy():
    data = json.loads(request.data)
    fasta=  data['sequence']
    uri = 'http://rest.pubmlst.org/db/pubmlst_rmlst_seqdef_kiosk/schemes/1/sequence'
    if data['base64'] == 'true':
        fasta =  base64.b64encode(fasta.encode()).decode()
    payload = '{"base64":true,"details":true,"sequence":"' + fasta + '"}'
    response = requests.post(uri, data=payload)
    if response.status_code == requests.codes.ok:
        data = response.json()
        return data 
    else:
        print(response.text)
        return response.text        
        # try: 
        #     data['taxon_prediction']
        # except KeyError:
        #     print("No match")
        #     sys.exit(0)
        # for match in data['taxon_prediction']:
        #         print("Rank: " + match['rank'])
        #         print("Taxon:" + match['taxon'])
        #         print("Support:" + str(match['support']) + "%")
        #         print("Taxonomy" + match['taxonomy'] + "\n")



if __name__ == '__main__':
    app.run()