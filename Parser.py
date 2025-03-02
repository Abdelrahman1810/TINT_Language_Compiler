class LL1Parser:
    def __init__(self, grammar, first, follow):
        self.grammar = grammar
        self.first = first
        self.follow = follow
        self.table = self.construct_parsing_table()

    def construct_parsing_table(self):
        """Construct the LL(1) parsing table."""
        table = {}
        for non_terminal, productions in self.grammar.items():
            table[non_terminal] = {}
            for production in productions:
                first_set = self.get_first(production)
                for terminal in first_set - {"epsilon"}:
                    table[non_terminal][terminal] = production
                if "epsilon" in first_set:
                    for terminal in self.follow[non_terminal]:
                        table[non_terminal][terminal] = production
        return table

    def get_first(self, production):
        """Calculate the First set for a production."""
        first_set = set()
        for symbol in production:
            if symbol in self.first:
                first_set |= self.first[symbol] - {"epsilon"}
                if "epsilon" not in self.first[symbol]:
                    break
            else:
                first_set.add(symbol)
                break
        else:
            first_set.add("epsilon")
        return first_set

    def parse(self, tokens):
        """Parse a list of tokens using the LL(1) parsing table."""
        stack = ["$"]
        stack.append(list(self.grammar.keys())[0])
        tokens.append("$")

        i = 0
        while stack:
            top = stack.pop()
            current_token = tokens[i]
            # print(top, ", ", current_token)

            if top == current_token == "$":
                return "Parse Success"

            if top in self.grammar:  # Non-terminal
                if current_token in self.table[top]:
                    production = self.table[top][current_token]
                    if production != ["epsilon"]:
                        stack.extend(reversed(production))
                else:
                    return f"Parse Failure: Unexpected token '{current_token}'"
            elif top == current_token:
                i += 1
            else:
                return f"Parse Failure: Expected '{top}', got '{current_token}'"
