import requests

patient = {"name": "Evan",
            "id": 1,
            "blood_type": "O+"}

r = request.post("http://127.0.0.1:5000/new_patient", json=patient)
print(r.status_code)
print(r.text)