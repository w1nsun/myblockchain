# Module 1 - Create blockchain

import datetime
import hashlib
import json
from flask import Flask, jsonify

class Blockchain:
    
    def __init__(self):
        self.chain = []
        self.create_block(prof = 1, previous_hash = '0')
        
    def create_block(self, proof, previous_hash):
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()), 
                 'proof': proof,
                 'previous_hash': previous_hash}
        self.chain.append(block)
        return block
