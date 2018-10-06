import unittest
from com.zmcneilly.password import lambda_function


class TestLambdaFunctions(unittest.TestCase):
    """
    Tests Lambda event handler.
    """

    def test_get_lambda_function_lambda_handler(self):
        # Empty event
        resp = lambda_function.lambda_handler({}, None)
        self.assertEqual(resp['statusCode'], 200)
        self.assertIsInstance(resp['body'], str)
        self.assertNotEqual(len(resp['body']), 0)
