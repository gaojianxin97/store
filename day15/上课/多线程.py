
import threading
import time
class PCmanager(threading.Thread):
    def run(self) -> None:
        for i in range(100):
            time.sleep(0.5)
            print("电脑管家正在杀毒，已经杀了",i)

class Manager360(threading.Thread):
    def run(self) -> None:
        for i in range(100):
            time.sleep(0.5)
            print("360杀毒正在杀毒,已经杀了",i)

pc = PCmanager()
manager = Manager360()
#调用start方法完成 线程 的开启
pc.start()  #电脑管家开始杀毒
manager.start() #360开始杀毒