from collections import namedtuple
import fileinput

Rule = namedtuple('Rule', ['command', 'antecedents', 'consequence'])

def parse_arg(arg):
    try:
        return int(arg)
    except ValueError:
        return arg

def parse_rule(text):
    tokens = text.strip().split(' ')
    if tokens[0] == 'NOT':
        rule = Rule(command=tokens[0], antecedents=[parse_arg(tokens[1])], consequence=tokens[3])
    elif len(tokens) == 3:
        rule = Rule(command='ASSIGN', antecedents=[parse_arg(tokens[0])], consequence=tokens[2])
    else:
        rule = Rule(command=tokens[1], antecedents=[parse_arg(tokens[0]), parse_arg(tokens[2])], consequence=tokens[4])
    return rule

def rule_can_fire(rule, known_values):
    return all(isinstance(a, int) or a in known_values for a in rule.antecedents)

def get_value(arg, known_values):
    if arg in known_values:
        return known_values[arg]
    else:
        return arg

def fire_rule(rule, known_values):
    evaluated_args = [get_value(arg, known_values) for arg in rule.antecedents]
    if rule.command == 'ASSIGN':
        known_values[rule.consequence] = evaluated_args[0]
    elif rule.command == 'NOT':
        known_values[rule.consequence] = ~evaluated_args[0] % 65536
    elif rule.command == 'LSHIFT':
        known_values[rule.consequence] = (evaluated_args[0] << evaluated_args[1]) % 65536
    elif rule.command == 'RSHIFT':
        known_values[rule.consequence] = (evaluated_args[0] >> evaluated_args[1]) % 65536
    elif rule.command == 'AND':
        known_values[rule.consequence] = (evaluated_args[0] & evaluated_args[1]) % 65536
    elif rule.command == 'OR':
        known_values[rule.consequence] = (evaluated_args[0] | evaluated_args[1]) % 65536

rules = [parse_rule(r) for r in fileinput.input()]  

known = {}
while 'a' not in known:
    for r in rules:
        if rule_can_fire(r, known) and r.consequence not in known:
            fire_rule(r, known)
print(known['a'])
