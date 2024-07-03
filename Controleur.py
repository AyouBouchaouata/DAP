from Etudiant import Students
from Module import Modules
class Verification():
    mo = []
    st = []
    t = []
    def ajoutmodule(self):
        nom=input("taper le nom de module: \n")
        note=input("taper la note: \n")
        coeficient=input("taper le coeficient: \n")
        cin = input("tapez la cin d'étudiant : \n")
        v=Modules(nom,note,coeficient,cin)
        self.mo.append(v)
    def ajoutetudiant(self):
        cin = input("tapez la cin d'étudiant : \n")
        nom = input("tapez le nom d'étudiant : \n")
        prenom = input("tapez le prénom d'étudiant : \n")
        s=Students(cin,nom,prenom)
        self.st.append(s)
    def afficher(self):
        for i in range(len(self.st)):
            print(self.st[i])
        for i in range(len(self.mo)):
            print(self.mo[i])

    def chercherEtudiant(self, cin):
        for i in range(len(self.st)):
            if (cin == self.st[i].cin):
                return i
        return -1
    def chercherModule(self, cin):
        for i in range(len(self.mo)):
            if (cin == self.mo[i].cin):
                return i
        return -1
    def chercherStudentModule(self):
        cin = input("enter le cin a chercher: \n")
        trouve = self.chercherEtudiant(cin)
        if (trouve == -1):
            print("Etudiant n'existe pas")
        else:
            trouve1 = self.chercherModule(cin)
            if (trouve1 == -1):
                print(self.st[trouve])
            else:
                calcul=(float(self.mo[trouve1].notes) * int(self.mo[trouve1].coeficiant))
                print(self.mo[trouve1].id,self.mo[trouve1].nom,self.mo[trouve1].notes,self.mo[trouve1].coeficiant,calcul,self.st[trouve].cin,self.st[trouve].nom,self.st[trouve].prenom)



















