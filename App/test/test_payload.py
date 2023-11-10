import requests
import json
import unittest

class SolutionTestCase(unittest.TestCase):
    
    def setUp(self):
        """
        Initialize string for testing
        """
        review = "Star Wars the rise of skywalker was the biggest piece of trash ever brought to life in the franchise \
            I wish this movie never existed and that no one ever pays to see this movie in real life. Its was horrible \
            and ghastly. The acting was terrible, the story line awful, and there were so many plot holes \
            My one friend really loved it though..."
        self.headers =  {"Content-Type": "application/json"}
        self.payload = json.dumps({"review": review})

    def test_webService(self):
        """
        Testing our webService
        """
        response = requests.post("http://127.0.0.1:8000/predict/",
                         headers=self.headers,
                         data = self.payload
                        )
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['prediction'], "Negative")


    def tearDown(self):
        """
        Tear down run
        """
        pass

if __name__ == '__main__':
    unittest.main()