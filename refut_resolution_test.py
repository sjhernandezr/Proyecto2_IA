from Marco_odia_a_cesar import facts, rules
from refut_resolution import process, text_file_output, resolution_refutation
from logic_types import Predicate, Term

if __name__ == "__main__":
    
    objetivo = Predicate("Odia", [Term("Marco"), Term("Cesar")])
    
    process.append("Starting test: Does Marco hate Caesar?")
    process.append("======================================")
    
    resultado = resolution_refutation(facts, rules, objetivo)
    
    text_file_output([str(c) for c in []], process)
    
    if resultado:
        print("PROVEN: Marco hates Caesar")
        print("Check Resolution_Process.txt for the detailed steps")
    else:
        print("NOT PROVEN: Could not prove that Marco hates Caesar")
        print("Check Resolution_Process.txt for the detailed steps")