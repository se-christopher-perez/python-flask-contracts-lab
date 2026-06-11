#!/usr/bin/env python3

from flask import Flask, request, current_app, g, make_response

contracts = [{"id": 1, "contract_information": "This contract is for John and building a shed"},{"id": 2, "contract_information": "This contract is for a deck for a buisiness"},{"id": 3, "contract_information": "This contract is to confirm ownership of this car"}]
customers = ["bob","bill","john","sarah"]
app = Flask(__name__)

@app.route("/contract/<int:id>")
def contract(id):
    found = [contract for contract in contracts if contract["id"] == id]

    if found:
        return found[0]["contract_information"], 200
    
    return "Contract not found", 404

@app.route("/customer/<string:customer_name>")
def customer(customer_name):
    found = [name for name in customers if name == customer_name]

    if found:
        return found[0], 204
    return "Customer not found", 404

if __name__ == '__main__':
    app.run(port=5555, debug=True)
