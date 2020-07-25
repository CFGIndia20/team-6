"""
pip install address-net
"""
from addressnet.predict import predict_one

def postcode(data):
    loc_details = predict_one(data)
    return loc_details["postcode"]

"""
eg data -  "I live in Keluskar Rd S, Dadar West, Shivaji Park, \
Mumbai, Maharashtra 400028, India. This is not my home. It is just a sample"
"""