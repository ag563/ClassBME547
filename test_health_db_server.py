from health_db_server import db
db.append()


def test_add_patient_to_db():
    from health_db_server import add_patient_to_db
    from health_db_server import db
    name = "David Ward"
    id = 100
    blood_type = "O+"
    add_patient_to_db(name, id, blood_type)
    patient_added = db[-1]
    expected = {"name": name, "id": id, "blood_type": blood_type,
                "test": []}
    assert patient_added == expected

def test_get_patient_from_db():
    from health_db_server import get_patient_from_db
    from health_db_server import db
    test_patient = {"name": "Erica Emerson", 
                    "id": 200, 
                    "blood_type": "O-",
                    "test": []}
    db.appent(test_patient)
    answer = get_patient_from_db(200)
    assert answer == test_patient

def test_get_patient_from_db