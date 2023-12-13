import unittest
from unittest.mock import patch, MagicMock
from main import MyHandler

class MockEvent:
    def __init__(self, src_path):
        self.src_path = src_path

class TestMyHandler(unittest.TestCase):
    def setUp(self):
        self.handler = MyHandler()

    @patch('os.path.exists')
    @patch('os.makedirs')
    @patch('shutil.move')
    def test_on_created(self, mock_move, mock_makedirs, mock_exists):
        mock_event = MockEvent('/Users/Daniel/Downloads/test.mp3')
        mock_exists.return_value = False  # Simulate that the folder does not exist

        self.handler.on_created(mock_event)

        # Check if these functions are called with expected arguments
        mock_exists.assert_called()  # Check if os.path.exists is called
        mock_makedirs.assert_called()  # Check if os.makedirs is called
        mock_move.assert_called()  # Check if shutil.move is called

if __name__ == '__main__':
    unittest.main()
