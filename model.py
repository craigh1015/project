from google.cloud import firestore

db = firestore.Client()
tasks_ref = db.collection(u'tasks')

def clear():
    try:
        for doc in tasks_ref.stream():
            doc.reference.delete()
        return True
    except:
        return False    

def getTasks():
    try:
        return ([ doc.to_dict() for doc in tasks_ref.stream()], True)
    except:
        return ([], False)

def add(doc):
    try:
        tasks_ref.add(doc, doc['id'])
        return True
    except:
        return False

def delete(id):
    try:
        tasks_ref.document(id).delete()
        return True
    except:
        return False

def update(doc):
    try:
        doc_ref = tasks_ref.document(doc['id'])
        doc_ref.set(doc)
        return True
    except:
        return False
