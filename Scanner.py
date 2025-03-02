from Tokens import token_names
from Tokens import TokenType

class Scanner:
    def __init__(self, filename):
        try:
            self.in_file = open(filename, "r")
        except FileNotFoundError:
            print("Error opening file.")
            self.in_file = None

        self.current_char = None
        self.end_of_file = False
        if self.in_file:
            self.get_next_char()

    def get_next_char(self):
        self.current_char = self.in_file.read(1)
        if self.current_char == "":
            self.end_of_file = True

    def skip_whitespace(self):
        while not self.end_of_file and self.current_char.isspace():
            self.get_next_char()

    def skip_comment(self):
        if self.current_char == "{":
            while not self.end_of_file and self.current_char != "}":
                self.get_next_char()
            self.get_next_char()  # Skip the closing '}'

    def get_next_token(self):
        self.skip_whitespace()

        while not self.end_of_file and self.current_char == "{":
            self.skip_comment()
            self.skip_whitespace()

        if self.end_of_file:
            return TokenType.ENDFILE

        if self.current_char.isalpha():
            lexeme = ""
            while not self.end_of_file and (self.current_char.isalnum()):
                lexeme += self.current_char
                self.get_next_char()

            if lexeme == "if":
                return TokenType.IF
            if lexeme == "then":
                return TokenType.THEN
            if lexeme == "else":
                return TokenType.ELSE
            if lexeme == "end":
                return TokenType.END
            if lexeme == "repeat":
                return TokenType.REPEAT
            if lexeme == "until":
                return TokenType.UNTIL
            if lexeme == "read":
                return TokenType.READ
            if lexeme == "write":
                return TokenType.WRITE
            return TokenType.IDENTIFIER

        elif self.current_char.isdigit():
            lexeme = ""
            while not self.end_of_file and self.current_char.isdigit():
                lexeme += self.current_char
                self.get_next_char()
            return TokenType.NUMBER

        elif self.current_char == ":":
            self.get_next_char()
            if self.current_char == "=":
                self.get_next_char()
                return TokenType.ASSIGN
            return TokenType.ERROR

        elif self.current_char == "+":
            self.get_next_char()
            return TokenType.PLUS

        elif self.current_char == "-":
            self.get_next_char()
            return TokenType.MINUS

        elif self.current_char == "*":
            self.get_next_char()
            return TokenType.MULT

        elif self.current_char == "/":
            self.get_next_char()
            return TokenType.DIV

        elif self.current_char == "=":
            self.get_next_char()
            return TokenType.EQUAL

        elif self.current_char == "<":
            self.get_next_char()
            return TokenType.LESSTHAN

        elif self.current_char == ";":
            self.get_next_char()
            return TokenType.SEMICOLON

        elif self.current_char == "(":
            self.get_next_char()
            return TokenType.OPENBRACKET

        elif self.current_char == ")":
            self.get_next_char()
            return TokenType.CLOSEDBRACKET

        self.get_next_char()
        return TokenType.ERROR

    def get_token_name(self, token):
        return token_names.get(token, "UNKNOWN")

    def close(self):
        if self.in_file:
            self.in_file.close()

    