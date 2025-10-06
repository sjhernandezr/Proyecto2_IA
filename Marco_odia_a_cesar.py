from logic_types import Predicate, Term

facts = [
    Predicate("Hombre", [Term("Marco")]),
    Predicate("Pompeyano", [Term("Marco")]),
    Predicate("Gobernante", [Term("Cesar")]),
    Predicate("IntentaAsesinar", [Term("Marco"), Term("Cesar")]),
]

rules = {
    "pompeyano_es_romano": {
        "premisa": "Pompeyano(x)",
        "conclusion": "Romano(x)"
    },
    "romano_es_leal_o_odia": {
        "premisa": "Romano(x)",
        "conclusion": "Leal(x, Cesar) v Odia(x, Cesar)"   # indicar que la conclusión es disyuntiva
    },
    "intento_asesinar_implica_no_leal": {
        "premisa": "Hombre(x) ∧ Gobernante(y) ∧ IntentaAsesinar(x,y)",
        "conclusion": "¬Leal(x,y)"
    }
}
