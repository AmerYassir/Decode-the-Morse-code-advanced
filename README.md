# Decode the Morse code, advanced — Solution

This repository contains a personal of Amer Abduljalil solution to the Codewars kata "Decode the Morse code, advanced".  
Kata: https://www.codewars.com/kata/54b72c16cd7f5154e9000457

profile : https://www.codewars.com/users/AmerYasser

## Problem (brief)
Decode a string of Morse code into readable text. The "advanced" variant requires handling extra spacing between letters and words (variable numbers of spaces), trimming leading/trailing spaces, and properly reconstructing words and letters.

## Solution approach
- Trim input.
- Split into words by runs of 3 or more spaces (or by the logic required by the chosen implementation).
- Split each word into letters by single spaces.
- Map each Morse letter to its corresponding character using a Morse table.
- Rejoin letters into words and words into the final sentence.


## Files
- solution.py: implementation file 
- README.md: this file.

## Usage
- Python 3.11: python3 solution.py

The program can be invoked with direct input or by running included tests if any.

## Notes
- This repo is a single-kata solution intended for learning and reference.
- For complete verification, submit the solution to Codewars where the full test suite runs.

## License
This repository is provided for educational purposes. No license declared.