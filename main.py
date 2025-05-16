from excepty import Dataframe

def main():
    first=Dataframe()
    filename = input("Введите имя вашего файла: ")            
    first = Dataframe(filename)
    first.lol()

if __name__ == "__main__":
    main()