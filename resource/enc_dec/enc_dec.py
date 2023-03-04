from flask_restful import Resource, request
import phe as paillier
from flask import jsonify

class EncDec(Resource):

    def serializeData(self, public_key, encrypted_data_list):
        encrypted_data={}
        encrypted_data['public_key'] = {'n': str(public_key.n)}
        encrypted_data['values'] = [(str(x.ciphertext()), x.exponent) for x in encrypted_data_list]
        return jsonify(encrypted_data)


    def post(self, name):
        if(name == 'encrypt'):
            data = request.get_json()
            
            values = data['values']
            public_key = paillier.PaillierPublicKey(n=int(data['public_key']['n']))
            encrypted_data_list = [ public_key.encrypt(float(x)) for x in values ]
            
            return self.serializeData(public_key, encrypted_data_list)
        
        if(name == 'decrypt'):
            data = request.get_json()
            public_key = paillier.PaillierPublicKey(n=int(data['public_key']['n']))
            private_key = paillier.PaillierPrivateKey(public_key, data['private_key']['p'], data['private_key']['q'])
            answers = [ paillier.EncryptedNumber(public_key, int(x[0]), int(x[1])) for i, x in enumerate(data['values'])]
            result = [ private_key.decrypt(x) for x in answers ] 
            return jsonify(result)

        return name

    def get(self, name):
        if(name == 'generate_key_pair'):
            public_key, private_key = paillier.generate_paillier_keypair()
            keys={}
            # Convert public key and private key from float to str
            # Don't forget to convert back from str to float before use
            keys['public_key'] = {'n': str(public_key.n)}
            keys['private_key'] = {'p': str(private_key.p),'q': str(private_key.q)}
            return jsonify(keys)
            
        return 404
    

