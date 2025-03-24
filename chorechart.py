

class ChoreChart:

    def __init__(self):
        self.chores = []
        self.family_members = {}
        self.load_chores()
        self.load_family_members()


    def load_chores(self,filename='chores.txt'):
        try:
            with open(filename,'r') as f:
                self.chores = [line.strip() for line in f.readlines()]

        execpt FileNotFoundError:
            print("No File Found, Please add a chores file!!)


    def load_family_members(self):
        pass
