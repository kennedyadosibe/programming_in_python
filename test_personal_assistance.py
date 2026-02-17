"""
Unit tests for Personal Info Summary Assistant.

Test coverage for all major functions and features.
"""

import unittest
import os
import json
import tempfile
import shutil
from unittest.mock import patch, MagicMock
from io import StringIO
import sys

# Import the module to test
import personal_assistance as pa


class TestPersonalAssistance(unittest.TestCase):
    """Test cases for Personal Info Summary Assistant."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.test_dir = tempfile.mkdtemp()
        self.original_dir = os.getcwd()
        os.chdir(self.test_dir)
        
        self.sample_responses = {
            'name': 'John Doe',
            'age': '25',
            'color': 'blue',
            'food': 'pizza',
            'city': 'New York'
        }
    
    def tearDown(self):
        """Clean up test fixtures."""
        os.chdir(self.original_dir)
        shutil.rmtree(self.test_dir)
    
    @patch('builtins.input')
    def test_get_user_data_valid_input(self, mock_input):
        """Test get_user_data with valid inputs."""
        # Mock inputs for required and some optional questions
        mock_input.side_effect = ['John Doe', '25', 'blue', 'pizza', 'New York']
        
        with patch('random.sample', return_value=[('color', ''), ('food', ''), ('city', '')]):
            responses = pa.get_user_data()
        
        self.assertEqual(responses['name'], 'John Doe')
        self.assertEqual(responses['age'], '25')
    
    @patch('builtins.input')
    def test_get_user_data_invalid_age(self, mock_input):
        """Test get_user_data with invalid age input."""
        # First invalid, then valid
        mock_input.side_effect = ['John', 'abc', '25', 'blue']
        
        with patch('random.sample', return_value=[('color', '')]):
            with patch('sys.stdout', new_callable=StringIO):
                responses = pa.get_user_data()
        
        self.assertEqual(responses['age'], '25')
    
    @patch('builtins.input')
    def test_get_user_data_empty_input(self, mock_input):
        """Test get_user_data rejects empty inputs."""
        # First empty, then valid
        mock_input.side_effect = ['', 'John', '25', 'blue']
        
        with patch('random.sample', return_value=[('color', '')]):
            with patch('sys.stdout', new_callable=StringIO):
                responses = pa.get_user_data()
        
        self.assertEqual(responses['name'], 'John')
    
    def test_display_summary(self):
        """Test display_summary outputs correctly."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            pa.display_summary(self.sample_responses)
            output = mock_stdout.getvalue()
            
            self.assertIn('John Doe', output)
            self.assertIn('25', output)
            self.assertIn('blue', output)
    
    def test_save_to_file(self):
        """Test save_to_file creates correct file."""
        with patch('sys.stdout', new_callable=StringIO):
            pa.save_to_file(self.sample_responses, 5)
        
        filename = 'John_Doe.txt'
        self.assertTrue(os.path.exists(filename))
        
        with open(filename, 'r') as f:
            content = f.read()
            self.assertIn('John Doe', content)
            self.assertIn('25', content)
            self.assertIn('Rating:', content)
    
    def test_save_to_json(self):
        """Test save_to_json creates correct JSON file."""
        with patch('sys.stdout', new_callable=StringIO):
            pa.save_to_json(self.sample_responses, 4)
        
        filename = 'John_Doe.json'
        self.assertTrue(os.path.exists(filename))
        
        with open(filename, 'r') as f:
            data = json.load(f)
            self.assertEqual(data['user_data']['name'], 'John Doe')
            self.assertEqual(data['rating'], 4)
            self.assertIn('timestamp', data)
    
    def test_view_saved_summaries_no_files(self):
        """Test view_saved_summaries with no saved files."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            pa.view_saved_summaries()
            output = mock_stdout.getvalue()
            self.assertIn('No saved summaries', output)
    
    def test_view_saved_summaries_with_files(self):
        """Test view_saved_summaries with existing files."""
        # Create test files
        open('test_user.txt', 'w').close()
        open('test_user.json', 'w').close()
        
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            pa.view_saved_summaries()
            output = mock_stdout.getvalue()
            self.assertIn('test_user.txt', output)
            self.assertIn('test_user.json', output)
    
    def test_display_statistics_no_data(self):
        """Test display_statistics with no data files."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            pa.display_statistics()
            output = mock_stdout.getvalue()
            self.assertIn('No data available', output)
    
    def test_display_statistics_with_data(self):
        """Test display_statistics with existing data."""
        # Create test JSON files
        test_data1 = {
            'timestamp': '2024-01-01T12:00:00',
            'user_data': {'name': 'User1', 'age': '20'},
            'rating': 5
        }
        test_data2 = {
            'timestamp': '2024-01-02T12:00:00',
            'user_data': {'name': 'User2', 'age': '30'},
            'rating': 4
        }
        
        with open('user1.json', 'w') as f:
            json.dump(test_data1, f)
        with open('user2.json', 'w') as f:
            json.dump(test_data2, f)
        
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            pa.display_statistics()
            output = mock_stdout.getvalue()
            self.assertIn('Total Users: 2', output)
            self.assertIn('Average Rating: 4.50', output)
            self.assertIn('Average Age: 25.0', output)
    
    @patch('builtins.input')
    def test_get_rating_valid(self, mock_input):
        """Test get_rating with valid input."""
        mock_input.return_value = '5'
        rating = pa.get_rating()
        self.assertEqual(rating, 5)
    
    @patch('builtins.input')
    def test_get_rating_invalid_then_valid(self, mock_input):
        """Test get_rating with invalid then valid input."""
        mock_input.side_effect = ['abc', '6', '4']
        
        with patch('sys.stdout', new_callable=StringIO):
            rating = pa.get_rating()
        
        self.assertEqual(rating, 4)
    
    @patch('builtins.input')
    def test_show_menu(self, mock_input):
        """Test show_menu displays and gets choice."""
        mock_input.return_value = '1'
        
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            choice = pa.show_menu()
            output = mock_stdout.getvalue()
            
            self.assertEqual(choice, '1')
            self.assertIn('Main Menu', output)
    
    def test_colors_class(self):
        """Test Colors class has expected attributes."""
        self.assertTrue(hasattr(pa.Colors, 'HEADER'))
        self.assertTrue(hasattr(pa.Colors, 'OKGREEN'))
        self.assertTrue(hasattr(pa.Colors, 'ENDC'))


class TestIntegration(unittest.TestCase):
    """Integration tests for complete workflows."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.test_dir = tempfile.mkdtemp()
        self.original_dir = os.getcwd()
        os.chdir(self.test_dir)
    
    def tearDown(self):
        """Clean up test fixtures."""
        os.chdir(self.original_dir)
        shutil.rmtree(self.test_dir)
    
    @patch('builtins.input')
    def test_complete_workflow_with_save(self, mock_input):
        """Test complete workflow: input -> display -> save."""
        mock_input.side_effect = ['Jane Smith', '30', 'red', 'sushi']
        
        with patch('random.sample', return_value=[('color', ''), ('food', '')]):
            with patch('sys.stdout', new_callable=StringIO):
                responses = pa.get_user_data()
                pa.display_summary(responses)
                pa.save_to_file(responses, 5)
                pa.save_to_json(responses, 5)
        
        # Check both files were created
        self.assertTrue(os.path.exists('Jane_Smith.txt'))
        self.assertTrue(os.path.exists('Jane_Smith.json'))
        
        # Verify content
        with open('Jane_Smith.json', 'r') as f:
            data = json.load(f)
            self.assertEqual(data['user_data']['name'], 'Jane Smith')
            self.assertEqual(data['rating'], 5)


if __name__ == '__main__':
    unittest.main()
