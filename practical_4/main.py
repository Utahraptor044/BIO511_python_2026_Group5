#!/usr/bin/env python3
from premade_script import codons, exercise_function
import argparse
import os

def existing_file(file_path):
    """This function checks if the provided file path exists and is a file."""
    if not os.path.isfile(file_path):
        raise argparse.ArgumentTypeError(f"'{file_path}' is not a valid file")
    return file_path


def main():
    # First we capture the input arguments from the command line
    parser = argparse.ArgumentParser(description="Split the sequences in a FASTA file into codons.")
    parser.add_argument('-s', '--sequence', type=existing_file, required=True, help='Path to the input FASTA file')
    args = parser.parse_args()
    
    # We first call the function from the script, and use the input file path as an argument
    sequence_codons = codons(args.sequence)
    
    # Here you need to check the output of the function
    print(sequence_codons)

    # Here you need to call the exercise_function from premade_script.py

    # And check the output of that function
    for header, codon_list in sequence_codons.items():
        exercise_out = exercise_function(codon_list)
        print(header, exercise_out)

if __name__ == "__main__":
    main()