class TokenType:
    IF = "IF"
    THEN = "THEN"
    ELSE = "ELSE"
    END = "END"
    REPEAT = "REPEAT"
    UNTIL = "UNTIL"
    READ = "READ"
    WRITE = "WRITE"
    IDENTIFIER = "IDENTIFIER"
    NUMBER = "NUMBER"
    ASSIGN = "ASSIGN"
    EQUAL = "EQUAL"
    LESSTHAN = "LESSTHAN"
    PLUS = "PLUS"
    MINUS = "MINUS"
    MULT = "MULT"
    DIV = "DIV"
    SEMICOLON = "SEMICOLON"
    ENDFILE = "ENDFILE"
    OPENBRACKET = "OPENBRACKET"
    CLOSEDBRACKET = "CLOSEDBRACKET"
    ERROR = "ERROR"

token_names = {
    TokenType.IF: "IF",
    TokenType.THEN: "THEN",
    TokenType.ELSE: "ELSE",
    TokenType.END: "END",
    TokenType.REPEAT: "REPEAT",
    TokenType.UNTIL: "UNTIL",
    TokenType.READ: "READ",
    TokenType.WRITE: "WRITE",
    TokenType.IDENTIFIER: "IDENTIFIER",
    TokenType.NUMBER: "NUMBER",
    TokenType.ASSIGN: "ASSIGN",
    TokenType.EQUAL: "EQUAL",
    TokenType.LESSTHAN: "LESSTHAN",
    TokenType.PLUS: "PLUS",
    TokenType.MINUS: "MINUS",
    TokenType.MULT: "MULT",
    TokenType.DIV: "DIV",
    TokenType.SEMICOLON: "SEMICOLON",
    TokenType.ENDFILE: "ENDFILE",
    TokenType.OPENBRACKET: "OPENBRACKET",
    TokenType.CLOSEDBRACKET: "CLOSEDBRACKET",
    TokenType.ERROR: "ERROR"
}