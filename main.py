from profile import Client

def main():
    name=input("ingrese su nombre:\n")
    last_name=input("ingrese su apellido:\n")
    amount=input("ingrese el monto a realizar:\n")
    run=input("ingrese su RUN sin digito verificador:\n")
    mail=input("ingrese su correo:\n")
    account_number=input("ingrese su numero de cuenta:\n")

    password = input("Ingrese su contraseña:")
    password_2 = input("Confirme su contraseña:")

    if (password == password_2):
        print("Su contraseña es correcta")
        user = Client(name,last_name,amount,run,mail,account_number)

        user.deposit()
        user.money()
    else:
        print("Su contraseña es incorrecta")

if __name__ == "__main__":
    main()
