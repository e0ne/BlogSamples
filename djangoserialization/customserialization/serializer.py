from customserialization.models import Employee

def to_json(obj):
    if isinstance(obj, Employee):
        return {'FirstName':obj.firstName,
                'LastName':obj.lastName,
                'City': obj.address.city,
                'Street': obj.address.street,
                'Title': obj.title}

    raise TypeError(repr(obj) + ' is not JSON serializable')
  