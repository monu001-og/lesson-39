class Employee:
    #Initializing(constructor)
    def __init__(self):
        print('Employee created')
        
    #deleting (destructor)
    def __del__(self):
        print('Destructor called,Employee deleted')
        
        
obj=Employee()
del obj
