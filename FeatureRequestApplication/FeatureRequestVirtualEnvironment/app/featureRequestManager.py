# featurerequestmanager.py acts as restful webservice which consists of 3 url end points used to create, retrieve and reprioritize Feature requests into/from database.
# Importing FeatureRequestApp model class
from app import app, FeatureRequestApp
# from sqlalchemy we can import ascending order
from sqlalchemy import asc
# imports all exceptetions from sqlalchemy package
from sqlalchemy.exc import *
# imports jsonify, request from flask package
from flask import jsonify,request
# imports featureRequestService.py
from app import featureRequestService

# FeatureRequestManger class is used to handle the url endpoints 'http://127.0.0.1:5000/createFeatureRequest' which is used to create Feature Requests and 'http://127.0.0.1:5000/retrieveFeatureRequest' which is used to retrieve Feature Request records from database
class FeatureRequestManger:
    """FeatureRequestManger Class is used to manage url end points /createFeatureRequest and /retrieveFeatureRequest"""
    try:
        # createFeatureRequest function is used to create New Feature Request in Database
        @app.route('/createFeatureRequest', methods=['POST'])
        def createFeatureRequestManager():
            # Instance of FeatureRequestService class is created to accesss functions createFeatureRequestService
            featurerequestservice= featureRequestService.FeatureRequestService()
            print("Inside Create")
            if request.method == 'POST':
                # Createing a FeatureRequestApp class object with title, description, client, clientPriority, targetData and productArea as arguments
                featureRequestApp=FeatureRequestApp(request.json['title'],request.json['description'],request.json['client'],request.json['clientPriority'],request.json['targetDate'],request.json['productArea'])
                # Response from createFeatureRequestService is assigned to 'result'       
                result =featurerequestservice.createFeatureRequestService(featureRequestApp)
                # Returns a String response
                return result

    except Exception as e:
        print("Error Occured in createFeatureRequestManager",e)
        

    try:
        # retrieveFeatureRequest function is used to retrieve the Feaure Request records from Database
        @app.route('/retrieveFeatureRequest', methods=['GET'])
        def retrieveFeatureRequestManager():
            if request.method == 'GET':
                # Instance of FeatureRequestService class is created to accesss functions retrieveFeatureRequestService
                feature= featureRequestService.FeatureRequestService()
                print("inside rretri")
                # Response from retrieveFeatureRequestService is assigned to 'result'       
                output= feature.retrieveFeatureRequestService()
                # Returns a JSON response 
                return jsonify({'details': output})
                
    except Exception as e:
        print("Error Occured in createFeatureRequestManager",e)


