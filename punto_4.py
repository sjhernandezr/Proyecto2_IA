from logic_types import Term, Predicate
from refut_resolution import Clause, convert_to_clause, convert_rule_to_clauses, are_complementary, resolve_clauses, resolution_refutation, text_file_output, process

#Teorema Barbara
x = Term("x")
c = Term("c")
hechos = [Predicate("B", [c])]
reglas = {"r1": {"premisa": "B(x)", "conclusion": "M(x)"}, "r2": {"premisa": "M(x)", "conclusion": "P(x)"}}
objetivo = Predicate("P", [c])
resultado, clausulas_finales = resolution_refutation(hechos, reglas, objetivo)
print("Refutation success:", resultado)
for c_ in clausulas_finales:
    print(str(c_))
for p in process:
    print(p)
text_file_output(clausulas_finales, process)