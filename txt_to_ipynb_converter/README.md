# txt_to_ipynb_converter

A simple Python utility for converting text files into Jupyter Notebook (IPYNB) format.

## Installation

You can install `txt_to_ipynb_converter` directly from the source code:


git clone https://github.com/yourusername/txt_to_ipynb_converter.git
cd txt_to_ipynb_converter
python setup.py install


## Usage

The package can be used as a command-line tool or imported into your Python scripts.

Command line

python -m txt_to_ipynb_converter <input_text_file> <output_ipynb_file>

In Python Scripts

from txt_to_ipynb_converter import txt_to_ipynb

txt_to_ipynb('path_to_input_file.txt', 'path_to_output_file.ipynb')

## Format of the Text File
The text file should use specific markers to indicate different cells:

Use # %% md to start a Markdown cell.
Use # %% code to start a code cell.

Example:

# %% md
# This is a markdown cell

# %% code
print("This is a code cell")

## Development
To contribute to this package, clone the repository, create a new branch for your feature or bug fix, and submit a pull request.

## Testing
Run the tests using the following command:

python -m unittest discover -s tests

## License

MIT License

## Contact

For any queries or contributions, please contact Prof Tim Hearn.