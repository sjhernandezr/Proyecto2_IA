from logic_types import Term, Predicate
from refut_resolution import Clause, convert_to_clause, convert_rule_to_clauses

def parse_predicate_string(pred_str):
    pred_str = pred_str.strip()
    is_positive = True
    if pred_str.startswith('¬') or pred_str.startswith('~'):
        is_positive = False
        pred_str = pred_str[1:].strip()
    name, args = pred_str.split('(')
    args = args.rstrip(')').split(',')
    args = [Term(a.strip()) for a in args]
    return is_positive, Predicate(name.strip(), args)

def convert_sentences_to_cnf_clauses(sentences):
    clauses = []
    for rule in sentences:
        generated = convert_rule_to_clauses(rule)
        clauses.extend(generated)
    return clauses