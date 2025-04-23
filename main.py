import functions_framework
from google.cloud import firestore
from flask import jsonify

db = firestore.Client()

@functions_framework.http
def add_user(request):
    request_json = request.get_json(silent=True)
    name = request_json.get('name', 'Anonymous')

    doc_ref = db.collection('users').document(name)
    doc_ref.set({'name': name})

    return jsonify({"message": f"User {name} added."})
