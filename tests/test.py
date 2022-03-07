import unittest

from lambda_handler import *

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum from DynamoDB
        """
        response = 0
        count = response

        new_count = str(int(count)+1)
        ddbResponse = count+1

        event = 0
        
        for val in event:
            count += val
        return event

        result = sum(data)
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()