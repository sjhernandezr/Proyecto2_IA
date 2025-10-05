hechos = [
    Predicado("Hombre", [Termino("Marco")]),
    Predicado("Pompeyano", [Termino("Marco")]),
    Predicado("Gobernante", [Termino("Cesar")]),
    Predicado("IntentaAsesinar", [Termino("Marco"), Termino("Cesar")]),
]
reglas = {
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
