class Client:
    def __init__(self, name, last_name, amount, run, mail, account_number):
        self.name = name
        self.last_name = last_name
        self.amount = amount
        self.run = run
        self.mail = mail
        self.account_number = account_number
        self.balance = 2000

    def deposit(self):
        print("Nombre:",self.name)
        print("Apellido:",self.last_name)
        print("Monto a realizar:",self.amount)
        print("RUN:",self.run)
        print("Correo:",self.mail)
        print("Numero de cuenta:",self.account_number)

    def money(self):
        if (int(self.amount) > 0):
            self.balance += int(self.amount)
            print("Su saldo es:",self.balance)
        elif (int(self.amount) <= 0):
            print("El valor ingresado es negativo o no corresponde")
        else:
            print("El valor es incorrecto,ingrese uno correcto")
