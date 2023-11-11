class Car:

    def __init__(self, mark='', model='', year=0, probeg=0):
        self.mark = mark
        self.model = model
        self.year = year
        self.probeg = probeg

    def set_mark(self, mark):
        self.mark = mark


    def set_year(self, year):
        self.year = year


    def set_model(self, model):
        self.model = model


    def set_probeg(self, probeg):
        self.probeg = probeg


    def get_mark(self):
        print(f'mark - {self.mark}')


    def get_year(self):
        print(f'year - {self.year}')


    def get_model(self):
        print(f'model - {self.model}')


    def get_probeg(self):
        print(f'prpbeg - {self.probeg}')


car1 = Car()
car1.set_mark('Nisan')
car1.set_model('skyline')
car1.set_year(1957)
car1.set_probeg(100000)
car1.get_mark()
car1.get_model()
car1.get_year()
car1.get_probeg()