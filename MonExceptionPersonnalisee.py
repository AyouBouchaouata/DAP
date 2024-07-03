class MonExceptionPersonnalisee(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

try:
    raise MonExceptionPersonnalisee("Ceci est une exception personnalisée")
except MonExceptionPersonnalisee as e:
    print(e)






