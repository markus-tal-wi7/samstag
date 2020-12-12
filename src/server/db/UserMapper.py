class UserMapper:
# (Mapper)
    """Mapper-Klasse, die User-Objekte auf eine relationale
    Datenbank abbildet. Hierzu wird eine Reihe von Methoden zur Verfügung
    gestellt, mit deren Hilfe z.B. Objekte gesucht, erzeugt, modifiziert und
    gelöscht werden können. Das Mapping ist bidirektional. D.h., Objekte können
    in DB-Strukturen und DB-Strukturen in Objekte umgewandelt werden.
    """
    def __init__(self):
            super().__init__()
    def find_all(self):
        return ("User1", "User2", "User3") #Demo-Tuple
    def find_by_name(self, name):
        pass
    def find_by_key(self, key):
        pass
    def find_by_email(self, mail_address):
        pass

"""Zu Testzwecken können wir diese Datei bei Bedarf auch ausführen, 
um die grundsätzliche Funktion zu überprüfen.

Anmerkung: Nicht professionell aber hilfreich..."""
if (__name__ == "__main__"):
    # with UserMapper() as mapper:
        result = UserMapper.find_all(UserMapper) #arg temporary
        for user in result:
            print(user)