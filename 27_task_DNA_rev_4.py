class DNA:
    def __init__(self, db_filename):
        with open(db_filename, 'r') as file:
            ls = file.readline().strip().split(",")
            self.dict1 = {}
            for i in range(1, len(ls)):
                self.dict1[ls[i]] = 0
            self.dictDataBase = {}
            for line in file:
                line = line.strip()
                print(line)
                index = line.find(',')
                self.dictDataBase[line[index+1:]] = line[:index]
        print('self.dict1: ',self.dict1)
        print('self.dictDataBase: ',self.dictDataBase)

    def __calculate(self, seq):
        dict1 = self.dict1.copy()
        for key in dict1:
            l = len(key)
            i = 0
            while i < len(seq):
                count = 0
                if seq[i:i + l] == key:
                    while seq[i:i + l] == key:
                        i += l
                        count += 1
                    if dict1[key] < count:
                        dict1[key] = count
                i += 1
        return ",".join(map(str, dict1.values()))

    def __find(self, result):
        if result in self.dictDataBase:
            return self.dictDataBase[result]
        return "No match"

    def search(self, dna_file_name):
        with open(dna_file_name, newline='') as file:
            return self.__find(self.__calculate(file.read()))


db = DNA('D:/=PYTHON=/Python_individual_study/Home_Work/DNA/databases/large.csv')
for i in range(5, 21):
    print(db.search(f'D:/=PYTHON=/Python_individual_study/Home_Work/DNA/sequences/{i}.txt'))
