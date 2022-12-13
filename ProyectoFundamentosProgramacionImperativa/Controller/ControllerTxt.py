import os

class ControllerText:

    def __init__(self):
        self.pathFile = os.getcwd() + "\\FileText\\"
        self.file = "Database.txt"

    def writeTextFile(self, parameters: str):
        with open(self.pathFile + self.file, 'a') as self.fileWriter:
            self.fileWriter.write(parameters + "\n")
            self.fileWriter.close()

    def readTextFile(self):
        self.listSplits = []
        with open(self.pathFile + self.file, 'r') as self.fileRead:
            i = 0
            for line in self.fileRead:
                linea = str(line).split('\n')
                self.listSplits.append(linea[0])
            return self.listSplits
    
if __name__ == '__main__':
    ControllerText().writeTextFile("Jannus Alejandro Largo Zafra")
    ControllerText().writeTextFile("Julian Escobar")
    ControllerText().writeTextFile("Osorio")

    lista = ControllerText().readTextFile()

    for i in range(len(lista)):
        linea = lista[i]
        if linea != '':
            print(str(i) + ": " +linea)
        else:
            print(i + ": " + linea)
