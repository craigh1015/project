from .location import Location

from google.cloud import firestore

db = firestore.Client()
locations = db.collection(u'locations')


def clear(collection):
    for doc in collection.stream():
        doc.reference.delete()


def clear_locations():
    clear(locations)


def add_location(location):
    locations.add(location.to_dict(), location.id)


def get_all():
    docs = locations.order_by('name').stream()
    return [Location.from_dict(doc.to_dict()) for doc in docs]


def get_by_id(id):
    return Location.from_dict(locations.document(id).get().to_dict())


def update(location):
    doc_ref = locations.document(location.id)
    doc_ref.set(location.to_dict())


def reserve_location(location):
    location.available = False
    return update(location)


def get_available_locations():
    # return list(filter(lambda x: x.available, get_all()))
    docs = locations.where('available', '==', True).order_by('name').stream()
    return [Location.from_dict(doc.to_dict()) for doc in docs]

# def delete(id):
#     try:
#         locations.document(id).delete()
#         return True
#     except:
#         return False
