class Students:
    cin:str
    nom:str
    prenom:str


    def __init__(self,cin,nom,prenom):
        self.cin=cin
        self.nom=nom
        self.prenom=prenom

    def __str__(self):
        return f"la cin {self.cin} d'étudiant {self.nom} {self.prenom}"
