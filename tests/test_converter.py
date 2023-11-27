import unittest
import nbformat
from txt_to_ipynb_converter.converter import txt_to_ipynb

class TestTxtToIpynbConverter(unittest.TestCase):

    def test_conversion(self):
        input_file = 'tests/test_data/test_input.txt'
        output_file = 'tests/test_data/test_output.ipynb'
        
        # Run the conversion
        txt_to_ipynb(input_file, output_file)
        
        # Open the generated IPYNB file and check its format
        with open(output_file, 'r') as f:
            nb = nbformat.read(f, as_version=4)
            
            # Example Assertions
            # Check if the notebook has the expected number of cells
            expected_number_of_cells = 5  # Update this based on your test data
            self.assertEqual(len(nb.cells), expected_number_of_cells)

            # Check the type of the first cell (e.g., markdown or code)
            expected_first_cell_type = 'markdown'  # or 'code'
            self.assertEqual(nb.cells[0].cell_type, expected_first_cell_type)

            # Check a specific content in a cell
            expected_content_in_cell = "Hello World!"  # Update this with actual content
            self.assertIn(expected_content_in_cell, nb.cells[0].source)

if __name__ == '__main__':
    unittest.main()
