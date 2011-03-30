import unittest

from connector import *


class ConnectorObjectCreationTest(unittest.TestCase):
    url = "testurl"
    
    def setUp(self):
       self.connector = Connector(self.url) 
    
    def testAttributes(self):
        """
        __init__ should store supplied attributes and initialize all properties
        """
        self.assertEqual(self.url, self.connector.url)

    def testNotConnected(self):
        """
        __init__ should set isconnected to False upon object creation
        """
        self.assertFalse(self.connector.isconnected)
        
        
#class ConnectorConnectTest(unittest.TestCase):


#class ConnectorDisconnectTest(unittest.TestCase):


#class ConnectorOpenTest(unittest.TestCase):
    

if __name__ == "__main__":
    unittest.main()   
