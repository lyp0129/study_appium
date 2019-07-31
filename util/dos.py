import os


class Dos:
    def aa(self):
        fd = os.popen("lsof -i:4700")
        tempsn = fd.read()
        print(tempsn)

    def dos(self, dos):
        fd = os.popen(dos)
        tempsn = fd.read()
        fd.close()
        b = []
        b.append(tempsn)
        temp = tempsn.strip().split("\n")
        doslist = []
        for i in temp:
            if "List" not in i:
                sn = i.split("\t")[0]
                doslist.append(sn)
        return doslist


if __name__ == '__main__':
    test = Dos()
    a = test.dos("lsof -i tcp:4700")
    print(a)
