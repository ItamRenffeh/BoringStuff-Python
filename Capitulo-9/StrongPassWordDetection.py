import re
    
def es_seguro(contraseña):
    if len(contraseña)<8 : return False
    chequeo = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)')
    match = chequeo.search(contraseña)
    if match: return True
    else : return False
    


if es_seguro("Afslfdasfad9"): print("Es seguro")
else : print ("Es inseguro")
        
        
    