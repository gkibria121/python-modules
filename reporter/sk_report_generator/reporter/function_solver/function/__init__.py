import regex as re


class Function:

    def __init__(self):
        self.data = None

    def set_data(self,data):
        self.data = data

    def update_data(self,data):
        self.data = data


    def sum(self,condition=None):
        if condition:
            pattern = r'\s*\((\w+)\)\s*=>\s*(.*)'
            match = re.search(pattern,condition)
            if match:

                self.data = eval(f"sum([{match[1]} for {match[1]} in self.data if {match[2]} ])")
        else:
            self.data = sum(self.data)

    def min(self,condition=None):
        if condition:
            pattern = r'\s*\((\w+)\)\s*=>\s*(.*)'
            match = re.search(pattern,condition)
            if match:

                self.data = eval(f"min([{match[1]} for {match[1]} in self.data if {match[2]} ])")
        else:
            self.data = min(self.data)

    def max(self,condition=None):
        if condition:
            pattern = r'\s*\((\w+)\)\s*=>\s*(.*)'
            match = re.search(pattern,condition)
            if match:

                self.data = eval(f"max([{match[1]} for {match[1]} in self.data if {match[2]} ])")
        else:
            self.data = max(self.data)

    def len(self,condition=None):
        if condition:
            pattern = r'\s*\((\w+)\)\s*=>\s*(.*)'
            match = re.search(pattern,condition)
            if match:

                self.data = eval(f"len([{match[1]} for {match[1]} in self.data if {match[2]} ])")
        else:
            self.data = len(self.data)

    def avg(self,condition=None):

        if condition:
            pattern = r'\s*\((\w+)\)\s*=>\s*(.*)'
            match = re.search(pattern,condition)
            if match:

                self.data = eval(f"sum([{match[1]} for {match[1]} in self.data if {match[2]} ])/len([{match[1]} for {match[1]} in self.data if {match[2]} ])")
        else:
            self.data = sum(self.data)/len(self.data)


    def count(self,args):

        if args:
            args = eval(args)
            self.data = self.data.count(args)
        else:
            self.data = 0

    def reverse(self, condition):
        if condition:
            pass
        else:
            self.data.reverse()

    def index(self,args):

        args = eval(args)
        self.data = self.data.index(args)

    def set(self, condition):
        if condition:
            pass
        else:

            self.data = set(self.data)

    def distinct(self,condition):
        if condition:
            pass
        else:
            self.data = list(set(self.data))

    def map(self,condition):


        if condition:
            pattern = r'\s*\(([\w\,]+)\)\s*=>\s*(.*)'
            match = re.search(pattern,condition)
            if match:
                if type(self.data) == list:
                    temp = []
                    for item in self.data:
                        exec(f"{match[1]} = {item}")
                        temp.append(eval(match[2]))

                    self.data= temp

                if type(self.data) == set:
                    temp = set()
                    for item in self.data:
                        exec(f"{match[1]} = {item}")
                        temp.add(eval(match[2]))

                    self.data= temp
