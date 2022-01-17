from urllib import response
from Blockchain import Blockchain
from flask import Flask

app = Flask(__name__)
blockchain = Blockchain()

app.route('/mineblock/<vesselname>', methods=['GET'])
def mine_block():
    previous_block = blockchain.previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create(proof, previous_hash)
    response = {'nessage': 'Block mined', 'index': block['index'], 'timestamp': block['timestamp'], 'proof': block['proof'], 'previous_hash': block['previous_hash']}
    return jsonify(response), 200

app.run('host=0.0.0.0', port = 5000)