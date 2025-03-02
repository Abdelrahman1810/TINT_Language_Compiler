# Grammar for the Tiny Language
grammar = {
    "program": [["stmt_sequence"]],

    "stmt_sequence": [["statement", "stmt_sequence`"]],
    "stmt_sequence`": [
        ["SEMICOLON", "statement", "stmt_sequence`"],
        ["epsilon"]
    ],
    
    "statement": [
        ["if_stmt"],
        ["repeat_stmt"],
        ["assign_stmt"],
        ["read_stmt"],
        ["write_stmt"]
    ],

    "if_stmt": [["IF", "exp", "THEN", "stmt_sequence", "else_part", "END"]],
    "else_part": [
        ["ELSE", "stmt_sequence"],
        ["epsilon"]    
    ],

    "repeat_stmt": [["REPEAT", "stmt_sequence", "UNTIL", "exp"]],
    "assign_stmt": [["IDENTIFIER", "ASSIGN", "exp"]],
    "read_stmt": [["READ", "IDENTIFIER"]],
    "write_stmt": [["WRITE", "exp"]],

    "exp": [["simple_exp", "exp`"]],
    "exp`": [["comparison_op", "simple_exp"], ["epsilon"]],

    "comparison_op": [["LESSTHAN"], ["EQUAL"]],

    "simple_exp": [["term", "simple_exp`"]],
    "simple_exp`": [
        ["add_op", "term", "simple_exp`"],
        ["epsilon"]
    ],
    
    "add_op": [["PLUS"], ["MINUS"]],

    "term": [["factor", "term`"]],
    "term`": [
        ["mul_op", "factor", "term`"],
        ["epsilon"]
    ],
    
    "mul_op": [["MULT"], ["DIV"]],
    "factor": [
        ["OPENBRACKET", "exp", "CLOSEDBRACKET"],
        ["NUMBER"],
        ["IDENTIFIER"]
    ],
}

# First and Follow sets
first = {
    "program": {"IF", "REPEAT", "IDENTIFIER", "READ", "WRITE"},
    "stmt_sequence": {"IF", "REPEAT", "IDENTIFIER", "READ", "WRITE"},
    "stmt_sequence`": {"SEMICOLON", "epsilon"},
    "statement": {"IF", "REPEAT", "IDENTIFIER", "READ", "WRITE"},
    
    "if_stmt": {"IF"},
    "else_part": {"ELSE", "epsilon"},

    "repeat_stmt": {"REPEAT"},
    "assign_stmt": {"IDENTIFIER"},
    "read_stmt": {"READ"},
    "write_stmt": {"WRITE"},
    
    "exp": {"OPENBRACKET", "NUMBER", "IDENTIFIER"},
    "exp`": {"LESSTHAN", "EQUAL", "epsilon"},

    "comparison_op": {"LESSTHAN", "EQUAL"},

    "simple_exp": {"OPENBRACKET", "NUMBER", "IDENTIFIER"},
    "simple_exp`": {"PLUS", "MINUS", "epsilon"},
    
    "add_op": {"PLUS", "MINUS"},

    "term": {"OPENBRACKET", "NUMBER", "IDENTIFIER"},
    "term`": {"MULT", "DIV", "epsilon"},
    
    "mul_op": {"MULT", "DIV"},
    "factor": {"OPENBRACKET", "NUMBER", "IDENTIFIER"},
}

follow = {
    "program": {"$"},
    "stmt_sequence": {"END", "ELSE", "UNTIL", "$"},
    "stmt_sequence`": {"END", "ELSE", "UNTIL", "$"},
    
    "statement": {"SEMICOLON", "END", "ELSE", "UNTIL", "$"},

    "if_stmt": {"SEMICOLON", "END", "ELSE", "UNTIL", "$"},
    "else_part": {"END"},

    "repeat_stmt": {"SEMICOLON", "END", "ELSE", "UNTIL", "$"},
    "assign_stmt": {"SEMICOLON", "END", "ELSE", "UNTIL", "$"},
    "read_stmt": {"SEMICOLON", "END", "ELSE", "UNTIL", "$"},
    "write_stmt": {"SEMICOLON", "END", "ELSE", "UNTIL", "$"},

    "exp": {"SEMICOLON", "END", "ELSE", "UNTIL", "$", "CLOSEDBRACKET", "THEN"},
    "exp`": {"SEMICOLON", "END", "ELSE", "UNTIL", "$", "CLOSEDBRACKET", "THEN"},
    
    "comparison_op": {"OPENBRACKET", "NUMBER", "IDENTIFIER", "SEMICOLON", "END", "ELSE", "UNTIL", "$", "CLOSEDBRACKET"},
    
    "simple_exp": {"LESSTHAN", "EQUAL", "SEMICOLON", "END", "ELSE", "UNTIL", "$", "CLOSEDBRACKET", "THEN"},
    "simple_exp`": {"LESSTHAN", "EQUAL", "SEMICOLON", "END", "ELSE", "UNTIL", "$", "CLOSEDBRACKET", "THEN"},
    
    "add_op": {"OPENBRACKET", "NUMBER", "IDENTIFIER"},
    
    "term": {"PLUS", "MINUS", "LESSTHAN", "EQUAL", "SEMICOLON", "END", "ELSE", "UNTIL", "$", "CLOSEDBRACKET", "THEN"},
    "term`": {"PLUS", "MINUS", "LESSTHAN", "EQUAL", "SEMICOLON", "END", "ELSE", "UNTIL", "$", "CLOSEDBRACKET", "THEN"},
    
    "mul_op": {"OPENBRACKET", "NUMBER", "IDENTIFIER"},
    "factor": {"SEMICOLON", "END", "ELSE", "UNTIL", "$", "LESSTHAN", "EQUAL", "CLOSEDBRACKET", "PLUS", "MINUS", "MULT", "DIV"},
}
