# 학생 클래스
# 속성 : 이름, 번호, 키
# 기능 : 학생정보보기, 학생정보입력

class 학생:
    이름 = ''
    번호 = 0
    키 = 0
    def __init__(self, 이름, 번호, 키):
        self.이름 = 이름
        self.번호 = 번호
        self.키 = 키
    
    def 학생정보보기(self):
        print('이름:', self.이름, ', 번호:', self.번호, ', 키:', self.키 )

    def 학생정보입력(self, 새이름, 새번호, 새키):
        self.이름 = 새이름
        self.번호 = 새번호
        self.키 = 새키        




철수 = 학생('철수', 1, 177.7)
영희 = 학생('영희', 2, 155.5)
짱구 = 학생('짱구', 3, 173.3)

철수.학생정보보기()
영희.학생정보보기()
짱구.학생정보보기()

짱구.학생정보입력('짱구', 4, 174.0)
짱구.학생정보보기()
짱구.학생정보입력('짱구', 5, 170.0)
짱구.학생정보보기()
짱구.학생정보입력('영희', 6, 160.0)
짱구.학생정보보기()