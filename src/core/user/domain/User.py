class User:

    id = None

    def __init__(self, firstName: str = '', lastName: str = '', email: str = '', password: str = ''):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.password = password

    def setId(self, id: str) -> None:
        self.id = id
    
    def setFirstName(self, firstName: str) -> None:
        self.firstName = firstName
    
    def setLastName(self, lastName: str) -> None:
        self.lastName = lastName

    def setEmail(self, email: str) -> None:
        self.email = email

    def setPassword(self, password: str) -> None:
        self.password = password