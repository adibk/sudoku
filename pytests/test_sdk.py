import unittest
import sys
import os
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from sdk import sdk
from sdk.sdk import Sdk
from sdk.sdk import Grid
from sdk import style as module_style
from sdk.style import Style

from examples.expls import SdkExples


class TestGrid(unittest.TestCase):
    def setUp(self):
        self.grid = Grid()
       
    def sub_test(self, input_text, expected_lines, size, length):
        self.assertEqual(self.grid.text, input_text)
        self.assertEqual(self.grid.lines, expected_lines)
        self.assertEqual(self.grid.size, size)
        self.assertEqual(self.grid.length, length)

    def test_simple_text(self):
        input_text = SdkExples.text['sdk_3x3_char_dot'][0]
        expected_lines = SdkExples.text['sdk_3x3_char_dot'][1]
        
        self.grid = Grid(input_text)
        self.sub_test(input_text, expected_lines, 3, 9)

    def test_text_setter_lines(self):
        expected_lines = SdkExples.text['sdk_2x2_char_0'][1]  
       
        self.grid = Grid(size=2)
        self.grid.lines = expected_lines
        self.sub_test(None, expected_lines, 2, 4)

    def test_text_setter_text(self):
        input_text = SdkExples.text['sdk_3x3_char_dot'][0]
        expected_lines = SdkExples.text['sdk_3x3_char_dot'][1]
        
        self.grid.text = input_text
        self.sub_test(input_text, expected_lines, 3, 9)

    def test_text_setter_emptylines(self):
        input_text = SdkExples.text['sdk_3x3_char_dot'][0]
        
        expected_lines = SdkExples.text['sdk_3x3_char_dot'][2]
        self.grid = Grid(input_text)
        self.grid.empty_lines = 0
        self.sub_test(input_text, expected_lines, 3, 9)

        expected_lines = SdkExples.text['sdk_3x3_char_dot'][3]
        self.grid = Grid(input_text)
        self.grid.empty_lines = '.'
        self.sub_test(input_text, expected_lines, 3, 9)
        
        expected_lines = SdkExples.text['sdk_3x3_char_dot'][4]
        self.grid = Grid(input_text)
        self.grid.empty_lines = '.1/0str0\\1.'
        print(self.grid.lines)
        self.sub_test(input_text, expected_lines, 3, 9)

    def test_lines_value_error(self):
        test_cases = [
            '5 5 5 5',
            '1 1',
            '1',
            '.'
        ]
        test_cases += list(SdkExples.text['wrong_format'])

        for case in test_cases:
            with self.subTest(input_value=case):
                with self.assertRaises(ValueError):
                    self.grid = Grid(case)
    
    def test_all(self):
        input_text = SdkExples.text['sdk_3x3_char_dot'][5]
        expected_lines = SdkExples.text['sdk_3x3_char_dot'][2]
        
        self.grid = Grid(input_text, '.', 3, '0')
        self.sub_test(input_text, expected_lines, 3, 9)
        
        
        

if __name__ == '__main__':
    unittest.main()