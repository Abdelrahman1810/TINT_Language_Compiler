# LL(1) Parser for the Tiny Language
# Author: Abdelrahman Mohamed Ali
# Code: 2100347
# Date: 2022-02-15
# Faculy of Engineering Ain Shams University
# Computer and Systems Department
# Description: This is a scanner and parser for the Tiny Language, The parser uses the LL(1) parsing algorithm.
# some of the error are fixed using AI (cahtgpt, poe, blackbox)
# function(read_tokens_from_file) written by chatgpt just to reduce time

from Scanner import Scanner
from Tokens import TokenType
from Parser import LL1Parser
import grammer

def read_tokens_from_file(filename):
    """Read tokens from a file and return them as a list."""
    tokens = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                token = line.strip()
                if token:
                    tokens.append(token)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

    return tokens

def extract_tokens(Token_file):
    with open(Token_file, "w") as file_token:
        first_flag = 0
        tokens = []
        while True:
            token = scanner.get_next_token()
            if token == TokenType.ENDFILE:
                break
            a = scanner.get_token_name(token)
            tokens.append(a)
            if first_flag == 0:
                file_token.write(a)
                first_flag = 1
            else:
                file_token.write("\n" + a)
        print("Scan Success \n - output in " + Token_file)
    scanner.close()
    return tokens

File_Code = "Correct_Codes\Sum_Of_Odds_Tiny_Code.txt"
Token_file = "List_of_Tokens\List_of_Tokens_Sum_Of_Odds.txt"
scanner = Scanner(File_Code)
parser = LL1Parser(grammer.grammar, grammer.first, grammer.follow)

tokens = extract_tokens(Token_file)
result = parser.parse(tokens)
print(result + "\n")

File_Code = "Correct_Codes\isPrime_Tiny_Code.txt"
Token_file = "List_of_Tokens\List_of_Tokens_isPrime.txt"
scanner = Scanner(File_Code)
parser = LL1Parser(grammer.grammar, grammer.first, grammer.follow)

tokens = extract_tokens(Token_file)
result = parser.parse(tokens)
print(result + "\n")

n = 3
for i in range(1, n + 1):
    File_Code = f"Wrong_Codes\Wrong_Tiny_Code({i}).txt"
    Token_file = f"List_of_Tokens\List_of_Tokens_WrongCode({i}).txt"

    scanner = Scanner(File_Code)
    parser = LL1Parser(grammer.grammar, grammer.first, grammer.follow)

    tokens = extract_tokens(Token_file)
    result = parser.parse(tokens)
    print(result + "\n")
 
