def create_database_entry(name, id_no, age):
    new_patient=[name, id_no, age, []]
    new_patient={"name": name, "id": id_no, "age": age, "test": list()}
    return new_patient

def print_directory(db):
    other_data=["room 2", "room 3", "room 4", "room 5"]
    for i, patient in enumerate(db):
        print(i)
        print ("Name: {}, id: {}, age: {}".format(patient[0], 
                                                patient[1], 
                                                patient[2]))
        print("patient is in {}".format(other_data[i]))

def find_patient(id_no, db):
    for patient in db:
        if patient[1] == id_no:
            answer = patient[0]
            break
#    print('found results')
    return answer

def add_test_result(id_no, db, test_name, test_result):
    for patient in db:
        if patient["id"] == id_no:
            patient["test"].append((test_name, test_result))
    print(db)
#def find_patient(id_no, db):
#    for patient in db:
#       if patient[1] == id_no:
#            return patient[0]
#    return "Patient not found"
def print_db(db):
    for patient in db:
        print_patient(patient)

def print_patient(patient):
    for key in patient:
        print(" {} = {}".format(key, patient[key]))

def demo(patient):
# another way to do it    
#    if patient.get("name") is not None:
    if "name" in patient:
        print("Name is {}".format(patient["name"]))
    if "DOB" in patient:
        print("DOB is {}".format(patient["DOB"]))
def adult_or_minor(patient):

    if patient["age"] >= 18:
        return "adult"
    else:
        return "minor"
def main():
    db=list()
    db.append(create_database_entry("Ann Ables", 1, 30))
    db.append(create_database_entry("Bob Bayles", 2, 31))
    db.append(create_database_entry("Chris Chou", 3, 32))
    db.append(create_database_entry("David Dikins", 4, 33))
    print_db(db)
    demo(db[0])

   # add_test_result(3, db, "HDL", 65)
   # print(db)
   # add_test_result(3, db, "LDL", 80)
   # print(db)
    
    #print last entry
#    print(db[-1])
   
    #print index 0 but not 2
#    print(db[0:2])

    #print index 1 and not 3
#    print(db[1:3])

    #everything but the first entry:
#    print(db[1:])

    #start on a certain place and go to a particular index
#    print(db[:3])

    #iterate over the db over each i but its going to put in my list the first entry
#    names=[i[0] for i in db]

    #just want oto look firrt 2 characters of a string
if __name__=="__main__":
    name="Dr Smith"
#    print(name[:2])
    main()