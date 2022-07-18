import time

a = ""
b = ""
def one():
    c = 0
    print("안녕 너의 이름은 뭐니?")
    time.sleep(1)
    a = input("이름: ")
    print(a      , "안녕! 만나서 반가워")
    time.sleep(2)
    two()

def two():
    print("혹시 너는 뭐를 좋아해?")
    time.sleep(2)
    b = input("딸기/바나나/초코")
    
    if b == "바나나":
        banana()
        
    elif b == "딸기":
        Strawberry()
        
    elif b == "초코":
        Chocolate()
        
    else:
        print("??다시 해줄래?")
        time.sleep(2)
        two()
                
def banana():
    time.sleep(2)
    print("아 너는 바나나를 좋아하는 구나!")
    time.sleep(3)
    print("그러면 바나나 케이크 로 정해야 겠어! 고마워")

def Strawberry():
    time.sleep(2)
    print("아 너는 딸기를 좋아하는 구나!")
    time.sleep(3)
    print("그러면 딸기 케이크 로 정해야 겠어! 고마워")

def Chocolate():
    time.sleep(2)
    print("아 너는 초코를 좋아하는 구나!")
    time.sleep(3)
    print("그러면 초코 케이크 로 정해야 겠어! 고마워")


one()