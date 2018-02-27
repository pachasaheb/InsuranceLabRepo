import sys
sys.path.append('D://Projects//ProjectFeatureRequestApp//FeatureRequestVirtualEnvironment//')
# Import Unittest to create test cases, requests to post 
import unittest, requests, json
from mock import MagicMock
from config import Config
from app import featureRequestService, FeatureRequestApp

# TestCasesApp class inherits unittest.TestCase class and consists of different testcases to unittest featureapp
class TestCasesApp(unittest.TestCase):
    
    # test_app_FeatureRequestFormPage function tests routing url 'http://127.0.0.1:5000/' in routes.py
    def test_app_FeatureRequestFormPage(self):
        """Tests working condition of Feature Requests Form Page"""
        self.assertEqual((requests.get(Config.featureRequestFormPageURL)).status_code,200)   

    # test_app_FeatureRequestDeatailsPage function checks routing url 'http://127.0.0.1:5000/FeatureRequestDetails' irn routes.py        
    def test_app_FeatureRequestDeatailsPage(self):
        """Tests working condition of Feature Requests Details Page"""
        self.assertEqual((requests.get(Config.featureRequestDetailsPageURL)).status_code,200) 

    # test_app_featureRequestService_createFeatureRequestService tests createFeatureRequestService present in FeatureRequestService class in featureRequestService module using a mock session
    def test_app_featureRequestService_createFeatureRequestService(self):
        """Tests successful submission of values in Feature Requests Form Page"""
        # Create an instance of MagicMock class with specification Session Class which gives a 'mock'Session instance
        mock= MagicMock(Config.Session())
        print("inside Mock test Feature request service", mock)
        # Creating an instance of FeatureRequestService class
        frs= featureRequestService.FeatureRequestService()
        # setting a mock session using setSession function in FeatureRequestService class 
        frs.setSession(mock)
        print("mock set",frs.getSession())
        # Creating an instance of FeatureRequestApp model class with all required values
        fra = FeatureRequestApp('Titl5', 'descr','Client B', 1, 'Billing', '2018-02-01')
        result= frs.createFeatureRequestService(fra)
        self.assertEqual(result,'success')

    # test_app_featureRequestService_retrieveFeatureRequestService tests createFeatureRequestService present in FeatureRequestService class in featureRequestService module using a mock session
    def test_app_featureRequestService_retrieveFeatureRequestService(self):
        """Tests successful retrieval of values from database for Feature Request Details"""
        # Create an instance of MagicMock class with specification Session Class which gives a 'mock'Session instance
        mock= MagicMock(Config.Session())
        print("inside Mock test Feature request service", mock)
        # Creating an instance of FeatureRequestService class
        frs= featureRequestService.FeatureRequestService()
        # setting a mock session using setSession function in FeatureRequestService class 
        frs.setSession(mock)
        print("mock set",frs.getSession())
        # Creating an instance of FeatureRequestApp model class with all required values
        result= frs.retrieveFeatureRequestService()
        # Checking result of retrieveFeatureRequestService
        self.assertIsNotNone(result)

    # test_app_featureRequestService_createFeatureRequestService tests createFeatureRequestService present in FeatureRequestService class in featureRequestService module using a mock session
    def test_app_featureRequestService_createFeatureRequestService_failure(self):
        """Tests successful submission of values in Feature Requests Form Page"""
        # Create an instance of MagicMock class with specification Session Class which gives a 'mock'Session instance
        mock= MagicMock(Config.Session())
        print("inside Mock test Feature request service", mock)
        # Creating an instance of FeatureRequestService class
        frs= featureRequestService.FeatureRequestService()
        # setting a mock session using setSession function in FeatureRequestService class 
        frs.setSession(mock)
        print("mock set",frs.getSession())
        # Creating an instance of FeatureRequestApp model class with all required values
        fra = FeatureRequestApp('Titl5', 'descr','Client B', 'hfd', 'Billing', '2018-02-01')
        result= frs.createFeatureRequestService(fra)
        self.assertEqual(result,'Error Occured')

    

  

    
        
        

