import nbformat as nbf
import argparse
import sys

def txt_to_ipynb(txt_file, ipynb_file):
    """
    Converts a TXT file to an IPython Notebook (IPYNB).

    Parameters:
    txt_file (str): The path to the input TXT file.
    ipynb_file (str): The path to the output IPYNB file.
    """
    try:
        nb = nbf.v4.new_notebook()
        current_cell = None

        with open(txt_file, 'r') as file:
            for line in file:
                if line.startswith('# %% md'):
                    if current_cell:
                        nb.cells.append(current_cell)
                    current_cell = nbf.v4.new_markdown_cell()
                elif line.startswith('# %% code'):
                    if current_cell:
                        nb.cells.append(current_cell)
                    current_cell = nbf.v4.new_code_cell()
                elif current_cell is not None:
                    current_cell.source += line

        if current_cell:
            nb.cells.append(current_cell)

        with open(ipynb_file, 'w') as file:
            nbf.write(nb, file)

    except Exception as e:
        sys.exit(f"Error: {e}")

def main():
    """
    Main function to parse command-line arguments and call the conversion function.
    """
    parser = argparse.ArgumentParser(description="Convert a TXT file to an IPython Notebook.")
    parser.add_argument('txt_file', type=str, help="Path to the input TXT file.")
    parser.add_argument('ipynb_file', type=str, help="Path to the output IPYNB file.")

    args = parser.parse_args()
    txt_to_ipynb(args.txt_file, args.ipynb_file)

if __name__ == "__main__":
    main()
