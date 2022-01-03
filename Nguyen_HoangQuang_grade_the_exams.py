answer_key = 'B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D'.split(',')
sV =[]
#------------
class Student:
    def __init__(self, id, answer):
        self.id = id
        self.answer = answer
    def getId(self):
        return self.id

    def getAnswer(self):
        return self.answer

    def getPoints(self):
        point=0
        list = self.answer
        for i in range(25):
            if list[i] == answer_key[i]:
                point = point+4
            elif list[i] == '':
                point = point+0
            elif list[i] != answer_key[i]:
                point = point -1
            i = i+1
        return point

    def __str__(self):
        return '{}, {}'.format(self.id, self.getPoints())
       
while(True):
    file = input('name file: ')
    try:
        with open(file+'.txt','r')  as filename:
            fileLines = filename.readlines()
    except:
        print('No such file name:')

    try:
        i, invalid = 0, 0
        for line in fileLines: 
            #rstrip xóa khoảng trắng khỏi phía “bên phải” của chuỗi.
            e = line.rstrip('\n').split(',')
            # print(e)
            if (e[0][0] == 'N' and len(e[0])==9 and e[0][1].isdecimal() and len(e) == 26): #isdecimal()
                sV.append(Student(e[0], e[1:]))
                # print(Student(e[0], e[1:]))
                i += 1 
            else:
                print('Data', e[0], ' dòng thứ', i+1, ' không hợp lệ')
                invalid += 1
        print('Tổng số dòng hợp lệ:', len(fileLines) - invalid)
        print('Tổng số dòng không hợp lệ:', invalid)
    except:
        print('Lỗi rồi ! ')

    sum = 0
    for i in sV:
        sum += i.getPoints()
    print('Điểm trung bình:', str(round((sum / len(sV)))))

    max = sV[0].getPoints()
    for i in sV:
        if(i.getPoints() > max):
            max = i.getPoints()
    print('Max: ', max)

    min = sV[0].getPoints()
    for i in sV:
        if(i.getPoints() < min):
            min = i.getPoints()
    print('Min: ', min)

    print('Miền giá trị:', max -min)

    for i in range(len(sV)):
        for j in range(len(sV)):
            if (sV[i].getPoints() < sV[j].getPoints()):
                a = [sV[i].getId(), sV[i].getAnswer()]
                b = [sV[j].getId(), sV[j].getAnswer()]
                sV[i]= Student(b[0], b[1])
                sV[j] = Student(a[0], a[1])
    if (len(sV) & 1 ==0):
        stt = int(len(sV)/2)
        a = sV[stt].getPoints() + sV[stt].getPoints()
        print('Giá trị trung vị:',str(round((a/2))))
    elif (len(sV) & 1==1):
        stt = int(round((len(sV)/2)))
        a = sV[stt].getPoints()
        print('Giá trị trung vị:',str(round((a))))

    if(file !=''):
        with open('grades/'+file+'_grades.txt','w') as f:
            for i in sV:
                f.write(str(i)+'\n')

