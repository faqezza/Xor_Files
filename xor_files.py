from pwn import xor

def encrypt_file(filename, key):
    with open(filename, "rb") as file:
        file_data = file.read()
    encrypted_data = xor(file_data, key)
    with open(filename + ".encrypted", "wb") as file:
        file.write(encrypted_data)

def decrypt_file(filename, key):
    with open(filename, "rb") as file:
        file_data = file.read()
    decrypted_data = xor(file_data, key)
    with open(filename[:-10], "wb") as file:  # Remove a extensão ".encrypted" do nome do arquivo
        file.write(decrypted_data)

mode = input("Deseja criptografar (c) ou descriptografar (d) um arquivo? ")

if mode.lower() == "c":
    filename = input("Digite o nome do arquivo a ser criptografado: ")
    password = input("Digite sua senha: ").encode()
    encrypt_file(filename, password)
    print("Arquivo criptografado com sucesso!")
elif mode.lower() == "d":
    filename = input("Digite o nome do arquivo a ser descriptografado: ")
    password = input("Digite sua senha: ").encode()

    # Descriptografar o arquivo
    decrypt_file(filename, password)
    print("Arquivo descriptografado com sucesso!")
else:
    print("Opção inválida. Escolha 'c' para criptografar ou 'd' para descriptografar.")
