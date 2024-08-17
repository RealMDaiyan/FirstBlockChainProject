import hashlib
import json
from crypt import methods
from time import time
from textwrap import dedent
from uuid import uuid4
from flask import Flask


class BlockChain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

        #Creates the genesis block
        self.new_block(1, 100)

    def new_block(self, proof, previous_hash=None):
        # Function that creates a new block and add to the chain
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1])
        }
        # Reset list of transactions
        self.current_transactions = []
        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        # Function that creates a new transaction and adds it to the list of transaction
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })
        return self.last_block['index'] + 1

    def proof_of_work(self, last_proof):
        """
         - Find a number p' such that hash(pp') contains leading 4 zeroes, where p is the previous p'
         - p is the previous proof, and p' is the new proof
        """

        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
        return proof

    @staticmethod
    def hash(block):
        # Hashes a block
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @staticmethod
    def valid_proof(self, last_proof, proof):
        # Validates the Proof: Does hash(last_proof, proof) contain 4 leading zeroes?
        guess =  f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

    @property
    def last_block(self):
        # Returns the last block in a chain
        return self.chain[-1]

# instantiate the node
app = Flask(__name__)

# Generate an address for this node
node_identifier = str(uuid4()).replace('-', '')

# Instantiate the blockChain
blockchain = BlockChain()

@app.route('/mine', methods=['GET'])
def mine():
    return "We'll mine a new block"

@app.route('/transactions/new', methods=['GET'])
def new_transaction():
    return "Well add a new transaction"


@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,

    }




