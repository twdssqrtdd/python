class 학생:
    이름 = ''
    번호 = 0
    키 = 0.0                                # 조건 추가가 필요할 때 
    def __init__(self, name, number, height):
        self.학생정보입력(self, name, number, height)
        

    def 학생정보보기(self):
        print('이름:', self.이름, ', 번호:', self.번호, ', 키:', self.키 )

    def 학생정보입력(self, 이름, 번호, 키):
        self.이름 = 이름
        self.번호 = 번호
        self.키 = 키

# 다른 사람들이 '학생'클래스 사용
# 클래스 업데이트 요청
# 상속 : 사람이 복붙을 하면 사람이 고쳐야 하기 때문에 컴퓨터가 복붙을 해서 컴퓨터가 고치게 한다.(상속은 = 클래스 복붙)
class 학생2(학생):
    def __del__(self):
        print('프로그램 종료')

a = 학생2('점수', 1, 177.7)
a.학생정보보기()

class 학생3(학생):
    def 학생정보보기(self):
        print('== 이름:', self.이름, ', 번호:', self.번호, ', 키:', self.키,'==' )
    # 원본 클래스가 '부모 클래스', 복붙받은 클래스는 '자식 클래스'
    # 부모 클래스와 자식 클래스의 매서드 명이 겹치면 자신의 매서드가 우선적으로 사용된다.
a = 학생3('점수', 1, 177.7)
a.학생정보보기()