# Singleton Design Pattern
class Champion:
    __instance = None

    def __new__(cls, name, age, nationality):
        #print(cls)
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        cls.__instance.name = name
        cls.__instance.age = age
        cls.__instance.nationality = nationality
        return cls.__instance
    
    def __call__(cls, *args, **kwargs):
        print(f"The current, champion is {cls.__instance.name} {cls.__instance.age} {cls.__instance.nationality}")
    
champ = Champion("A", 34, 'BD')
champ()

