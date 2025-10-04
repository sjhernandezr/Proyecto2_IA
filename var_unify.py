import logic_types

def unify_terms(term1, term2, sustitution = None):
    if sustitution is None:
        sustitution = {}
    
    if term1.is_variable and term2.name in sustitution:
        term1 = sustitution[term1.name]
    if term2.is_variable and term2.name in sustitution:
        term2 = sustitution[term2.name]
    
    if term1==term2:
        print("Son iguales")
        return sustitution
    
    if term1.is_variable:
        sustitution[term1.name] = term2
        
    if term2.is_variable:
        sustitution[term2.name] = term1
    
    print(f"No se pudo unificar {term1} y {term2}, son constantes diferentes")
    return None

def unify_predicates(pred1,pred2):
    if pred1.name != pred2.name:
        return None
    if len(pred1.args) != len(pred2.args):
        return None
    
    sustitution = {}
    
    for arg1, arg2 in zip(pred1.args, pred2.args):
        sustitution = unify_terms(arg1, arg2, sustitution)
        if sustitution is None:
            return None
    
    return sustitution