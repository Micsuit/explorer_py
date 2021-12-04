import os, pathlib, sys

lista_commands = ["goto", "create", "deletefile", "deletefolder",
                "filfol"]

def tudo_junto(text):
    final_phrase = ""

    for letra in text:
        if letra != " ":
            final_phrase += letra
    return final_phrase

def goto(cmd_junt):
    if cmd_junt.lower() == "goto":
        print("Por favor especifique um ficheiro para onde quer ir.")
    elif cmd_junt.lower() == "gotoback":
        os.chdir("..")
    else:
        try:
            os.chdir(cmd_junt[4: len(cmd_junt)])
        except:
            print("O ficheiro \"{}\" não foi encontrado!".format(cmd_junt[4: len(cmd_junt)]))

def create(cmd_junt):
    if cmd_junt.lower() == "create":
        print("Por favor introduza o nome do ficheiro que quer criar.")
    else:
        try:
            os.mkdir(cmd_junt[6: len(cmd_junt)])
            print("Ficheiro criado com succeso!")
        except:
            print("Não foi possível criar o ficheiro \"{}\".".format(cmd_junt[6:len(cmd_junt)]))
        
def del_file(cmd_junt):
    if cmd_junt.lower() == "deletefile":
        print("Por favor especifique o arquivo que quer eliminar.")
    else:
        try:
            os.remove(cmd_junt[10: len(cmd_junt)])
            print("Arquivo eliminado com sucesso!")
        except:
            print("Não foi possível eliminar o arquivo \"{}\".".format(cmd_junt[10:len(cmd_junt)]))

def del_folder(cmd_junt):
    if cmd_junt.lower() == "deletefolder":
        print("Por favor especifique o ficheiro que quer eliminar.")
    else:
        try:
            os.rmdir(cmd_junt[12: len(cmd_junt)])
            print("Ficheiro eliminado com sucesso!")
        except:
            print("Não foi possível eliminar o ficheiro \"{}\".".format(cmd_junt[10:len(cmd_junt)]))

### Por melhorar 🠗🠗🠗

def files_in_folder():
    files_in_fol = os.listdir()

    print("Files in folder \"{}\":\n{}".format(pathlib.PurePath(os.getcwd()).name, files_in_fol))

### Por melhorar 🠕🠕🠕

def iden_commd(input_user):
    cmd_junto = tudo_junto(input_user)

    if cmd_junto[0: 4].lower() == lista_commands[0]: # user_input = goto ...
        goto(cmd_junto)
    elif cmd_junto[0: 6].lower() == lista_commands[1]: # user_input = create ...
        create(cmd_junto)
    elif cmd_junto[0: 10].lower() == lista_commands[2]: # user_input = deletefile ...
        del_file(cmd_junto)
    elif cmd_junto[0: 12].lower() == lista_commands[3]: # user_input = deletefolder ...
        del_folder(cmd_junto)
    elif cmd_junto[0: 6].lower() == lista_commands[4]: # user_input = filfol
        files_in_folder()


    elif cmd_junto.lower() == "quit":
        sys.exit()
    else:
        print("O commando \"" + input_user.split()[0] + "\" é desconhecido.")
        

def run(text):
    iden_commd(text)


