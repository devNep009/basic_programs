class Singleton(object):
    __instance = None

    def __init__(self):
        if not Singleton.__instance:
            print('Instance do not exists')
        else:
            print('Instance exists:', self.get_instance())

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance

sg_1 = Singleton()

print('Creating instance', Singleton.get_instance())

# All there will reference the same object, 
# because once it is created, all instances of this class will use the same object
sg_2 = Singleton()

sg_3 = Singleton()

