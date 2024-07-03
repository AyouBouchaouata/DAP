from Etudiant import Students
class Modules:
    nom:str
    notes:float
    coeficiant:int
    cpt=0
    cin: str
    def __init__(self,nom,notes,coeficient,cin):
        self.id=self.cpt+1
        self.nom=nom
        self.notes=notes
        self.coeficiant=coeficient
        self.cin = cin

    def __str__(self):
        return f" id {self.id} Nom du Modules {self.nom} Note : {self.notes} Coeficient : {self.coeficiant} la cin {self.cin}"

