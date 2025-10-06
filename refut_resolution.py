from logic_types import Predicate, Term

process = []

class Clause:
    def __init__(self, literals):
        process.append("Creating new clause...")
        self.literals = literals
    
    def __str__(self):
        clause_str = []
        for is_positive, predicate in self.literals:
            if not is_positive:
                clause_str.append("¬")
            clause_str.append(str(predicate))
        return " ∨ ".join(clause_str)
    
    def is_empty(self):
        process.append("Checking if clause is empty...")
        return len(self.literals) == 0

def convert_to_clause(predicado, is_positive=True):
    process.append("Converting predicate to unitary clause...")
    if not is_positive:
        process.append(f"Negating predicate: ¬{str(predicado)}")
    else:
        process.append(f"Keeping positive predicate: {str(predicado)}")
    return Clause([(is_positive, predicado)])

def convert_rule_to_clauses(rule):
    process.append("Converting rules into implications in NCF...")

    premises = rule["premisa"].split(" ∧ ")
    
    conclusions = rule["conclusion"].split(" v ")
    
    all_clauses = []
    
    premise_literals = []
    for premisa in premises:
        if premisa.startswith("¬"):
            pred_name = premisa[1:].split("(")[0]
            terms = premisa.split("(")[1].rstrip(")").split(",")
            terms = [Term(t.strip()) for t in terms]
            premise_literals.append((True, Predicate(pred_name, terms)))
        else:
            pred_name = premisa.split("(")[0]
            terms = premisa.split("(")[1].rstrip(")").split(",")
            terms = [Term(t.strip()) for t in terms]
            premise_literals.append((False, Predicate(pred_name, terms)))
    
    for conclusion in conclusions:
        clause_literals = list(premise_literals) 
        
        if conclusion.startswith("¬"):
            pred_name = conclusion[1:].split("(")[0]
            terms = conclusion.split("(")[1].rstrip(")").split(",")
            terms = [Term(t.strip()) for t in terms]
            clause_literals.append((False, Predicate(pred_name, terms)))
        else:
            pred_name = conclusion.split("(")[0]
            terms = conclusion.split("(")[1].rstrip(")").split(",")
            terms = [Term(t.strip()) for t in terms]
            clause_literals.append((True, Predicate(pred_name, terms)))
        
        all_clauses.append(Clause(clause_literals))
    
    return all_clauses

def are_complementary(literal1, literal2):
    is_positive1, pred1 = literal1
    is_positive2, pred2 = literal2
    
    complementary = (is_positive1 != is_positive2) and pred1.name == pred2.name
    if complementary:
        process.append(f"Found complementary literals: {pred1.name}")
        process.append(f"One positive and one negative: {is_positive1} vs {is_positive2}")
    return complementary

def resolve_clauses(clause1, clause2):
    process.append("Searching for complementary literals between clauses...")
    
    for i, lit1 in enumerate(clause1.literals):
        for j, lit2 in enumerate(clause2.literals):
            if are_complementary(lit1, lit2):
                process.append("Complementary literals found! Generating resolvent...")
                new_literals = clause1.literals[:i] + clause1.literals[i+1:]
                new_literals += clause2.literals[:j] + clause2.literals[j+1:]
                if new_literals: 
                    process.append("Non-empty resolvent generated")
                    return Clause(new_literals)
                else:
                    process.append("Empty clause generated! (Contradiction found)")
                    return Clause([])
    
    process.append("No complementary literals found")
    return None

def resolution_refutation(hechos, reglas, objetivo):
    process.append("Starting refutation resolution algorithm...")
    
    clausulas = []
    process.append("Converting known facts to clauses...")
    for hecho in hechos:
        clausulas.append(convert_to_clause(hecho))
        process.append(f"Converted fact: {str(clausulas[-1])}")
    
    process.append("Converting rules to conjunctive normal form...")
    for nombre_regla, regla in reglas.items():
        process.append(f"Processing rule: {nombre_regla}")
        nuevas_clausulas = convert_rule_to_clauses(regla)
        clausulas.extend(nuevas_clausulas)
        for c in nuevas_clausulas:
            process.append(f"Generated clause: {str(c)}")
    
    process.append("Adding negation of goal for refutation...")
    clausulas.append(convert_to_clause(objetivo, False))
    process.append(f"Negated goal: {str(clausulas[-1])}")
    
    resueltas = set()
    process.append("Starting resolution process...")
    
    while True:
        nuevas_clausulas = []
        
        for i, clause1 in enumerate(clausulas):
            for clause2 in clausulas[i+1:]:
                process.append(f"Attempting to resolve clauses:")
                process.append(f"Clause 1: {str(clause1)}")
                process.append(f"Clause 2: {str(clause2)}")
                
                resolvente = resolve_clauses(clause1, clause2)
                if resolvente is not None:
                    if not resolvente.literals:
                        process.append("Empty clause found! Contradiction detected.")
                        return True
                    
                    str_resolvente = str(resolvente)
                    if str_resolvente not in resueltas:
                        process.append(f"New resolvent clause: {str_resolvente}")
                        resueltas.add(str_resolvente)
                        nuevas_clausulas.append(resolvente)
        
        if not nuevas_clausulas:
            process.append("No more clauses can be generated. No contradiction found.")
            return False

        process.append("Adding new clauses to the set...")
        clausulas.extend(nuevas_clausulas)

def text_file_output(clausulas, process):
    with open('Clauses and Process.txt', 'w' ) as t:
        for clausula in clausulas:
            t.write(clausula + '\n')
        t.write('\n')
        for proceso in process:
            t.write(proceso + '\n')





