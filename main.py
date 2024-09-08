from time import sleep
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import pygame
import sys
from form import Ui_MainWindow
pygame.init()

GRAY = (180, 180, 180)
RED = (255, 0, 0)
YELLOW = (255, 255, 10)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
SPD = 25    #Cкорость в пикселях в минуту 





## -------------------------- Описание графики окна модели -----------------------------------





pygame.display.set_caption("Airfield Model")
pygame.display.set_icon(pygame.image.load("am.ico"))
sc = pygame.display.set_mode((800, 600))



def sc_update():

    sc.fill(BLACK)
    pygame.draw.rect(sc, GREEN, (125, 100, 50, 225), 5)
    pygame.draw.rect(sc, GREEN, (250, 100, 50, 225), 5)

    pygame.draw.rect(sc, (60, 60, 60), (125, 25, 175, 50))
    pygame.draw.rect(sc, GREEN, (125, 25, 175, 50), 5)


    f = pygame.font.SysFont('arial', 28)
    sc_text = f.render('АНГАР', 3, GREEN)
    pos_sc_text = sc_text.get_rect(center = (213, 50))
    sc.blit(sc_text, pos_sc_text)


    for i in range(4):
        pygame.draw.line(sc, GREEN, (150, 125 + i*50), (150, 150 + i*50), 4)
        pygame.draw.line(sc, GREEN, (275, 125 + i*50), (275, 150 + i*50), 4)
    pygame.display.update()



    
## -------------------------- Классы модели -----------------------------------




class Plane():
    def __init__(self, TTAA, name):
        self.flag = "detected"
        self.pos = {'x': 750, 'y': 500}
        self.name = str(name)
        self.time_to_airport_area = TTAA
        self.surf = pygame.Surface((50, 75))
        self.runtime = ""
        self.set_time = ""



    def fly_to_airport(self):
        if self.flag == "detected" and self.time_to_airport_area != 0:
            self.time_to_airport_area -= 1

        elif self.flag == "detected" and self.time_to_airport_area == 0:
            self.flag = "ready to appearance"

    def get_TTAA(self):
        return self.time_to_airport_area

    def appearance(self):
        if self.flag == "ready to appearance":
            self.plane_surf = pygame.image.load("plane.png")
            f = pygame.font.SysFont('arial', 22)
            self.name_surf = f.render(self.name, 2, GREEN)
            self.plane_surf = pygame.transform.rotate(self.plane_surf, 90)
            self.surf.blit(self.name_surf, (0, 0))
            self.surf.blit(self.plane_surf, (0, 25))

            self.flag = "fly to POC"
            pygame.display.update()



    def fly_to_POC(self):
        if self.flag == "fly to POC":
            if self.pos != {'x': 400, 'y': 500}:
                pygame.draw.rect(sc, BLACK, (self.pos['x']-25, self.pos['y']-50, 50, 75))
                pygame.display.update()
                self.pos['x'] -= SPD
            else: 
                self.flag = "stay in POC"
            sc.blit(self.surf, (self.pos['x']-25, self.pos['y']-50))
            pygame.display.update()



    def fly_to_F1(self, f1_stuff, f1_time, ttr):
        if (self.flag == "stay in POC" and f1_stuff == False) or self.flag == "fly to field 1":
            
            self.flag = "fly to field 1"

            if self.pos['x'] != 200 and self.pos['y'] == 500:
                pygame.draw.rect(sc, BLACK, (self.pos['x']-25, self.pos['y']-50, 50, 75))
                pygame.display.update()
                self.pos['x'] -= SPD

            elif self.pos == {'x': 200, 'y': 500}:
                pygame.draw.rect(sc, BLACK, (self.pos['x']-25, self.pos['y']-50, 50, 75))
                pygame.display.update()
                self.pos['x'] -= 35
                self.pos['y'] -= 20
                pygame.draw.rect(self.surf, BLACK, (0, 25, 50, 50))
                self.plane_surf = pygame.transform.rotate(self.plane_surf, -90)
                self.surf.blit(self.plane_surf, (0, 25))

            elif self.pos == {'x': 165, 'y': 480}:
                pygame.draw.rect(sc, BLACK, (self.pos['x']-25, self.pos['y']-50, 50, 75))
                pygame.display.update()
                self.pos = {'x': 150, 'y': 450}

            elif self.pos['x'] == 150 and self.pos['y'] != 375:
                pygame.draw.rect(sc, BLACK, (self.pos['x']-25, self.pos['y']-50, 50, 75))
                pygame.display.update()
                self.pos['y'] -= SPD

            elif self.pos == {'x': 150, 'y': 375}:
                self.flag = "run on airfield 1"
                self.runtime = int(f1_time)
                self.set_time = int(ttr)

            sc.blit(self.surf, (self.pos['x']-25, self.pos['y']-50))
            pygame.display.update()



    def fly_to_F2(self, f1_stuff, f2_stuff, f2_time, ttr):
        if (self.flag == "stay in POC" and f1_stuff == True and f2_stuff == False) or self.flag == "fly to field 2":

            self.flag = "fly to field 2"
            
            if self.pos['x'] != 325 and self.pos['y'] == 500:
                pygame.draw.rect(sc, BLACK, (self.pos['x']-25, self.pos['y']-50, 50, 75))
                pygame.display.update()
                self.pos['x'] -= SPD

            elif self.pos == {'x': 325, 'y': 500}:
                pygame.draw.rect(sc, BLACK, (self.pos['x']-25, self.pos['y']-50, 50, 75))
                pygame.display.update()
                self.pos['x'] -= 35
                self.pos['y'] -= 20
                pygame.draw.rect(self.surf, BLACK, (0, 25, 50, 50))
                self.plane_surf = pygame.transform.rotate(self.plane_surf, -90)
                self.surf.blit(self.plane_surf, (0, 25))

            elif self.pos == {'x': 290, 'y': 480}:
                pygame.draw.rect(sc, BLACK, (self.pos['x']-25, self.pos['y']-50, 50, 75))
                pygame.display.update()
                self.pos = {'x': 275, 'y': 450}

            elif self.pos['x'] == 275 and self.pos['y'] != 375:
                pygame.draw.rect(sc, BLACK, (self.pos['x']-25, self.pos['y']-50, 50, 75))
                pygame.display.update()
                self.pos['y'] -= SPD
            
            elif self.pos == {'x': 275, 'y': 375}:
                self.flag = "run on airfield 2"
                self.runtime = int(f2_time)
                self.set_time = int(ttr)

            sc.blit(self.surf, (self.pos['x']-25, self.pos['y']-50))
            pygame.display.update()



    def turn(self, f1_stuff, f2_stuff):
        if (self.flag == "stay in POC" and f1_stuff == True and f2_stuff == True) or self.flag == "turning":

            self.flag = "turning"

            if self.pos['x'] == 400 and self.pos['y'] != 300:
                if self.pos['x'] == 400 and self.pos['y'] == 500:
                    pygame.draw.rect(self.surf, BLACK, (0, 25, 50, 50))
                    self.plane_surf = pygame.transform.rotate(self.plane_surf, -90)
                    self.surf.blit(self.plane_surf, (0, 25))
                pygame.draw.rect(sc, BLACK, (self.pos['x']-25, self.pos['y']-50, 50, 75))
                pygame.display.update()
                self.pos['y'] -= SPD

            elif self.pos['x'] != 600 and self.pos['y'] == 300:
                if self.pos['x'] == 400 and self.pos['y'] == 300:
                    pygame.draw.rect(self.surf, BLACK, (0, 25, 50, 50))
                    self.plane_surf = pygame.transform.rotate(self.plane_surf, -90)
                    self.surf.blit(self.plane_surf, (0, 25))
                pygame.draw.rect(sc, BLACK, (self.pos['x']-25, self.pos['y']-50, 50, 75))
                pygame.display.update()
                self.pos['x'] += SPD

            elif self.pos['x'] == 600 and self.pos['y'] != 500:
                if self.pos['x'] == 600 and self.pos['y'] == 300:
                    pygame.draw.rect(self.surf, BLACK, (0, 25, 50, 50))
                    self.plane_surf = pygame.transform.rotate(self.plane_surf, -90)
                    self.surf.blit(self.plane_surf, (0, 25))
                pygame.draw.rect(sc, BLACK, (self.pos['x']-25, self.pos['y']-50, 50, 75))
                pygame.display.update()
                self.pos['y'] += SPD
            
            elif self.pos['x'] == 600 and self.pos['y'] == 500:
                pygame.draw.rect(self.surf, BLACK, (0, 25, 50, 50))
                self.plane_surf = pygame.transform.rotate(self.plane_surf, -90)
                self.surf.blit(self.plane_surf, (0, 25))
                pygame.display.update()
                self.flag = "fly to POC"

            sc.blit(self.surf, (self.pos['x']-25, self.pos['y']-50))
            pygame.display.update()

                

    def run_on_field(self):
        if self.flag == "run on airfield 2" or self.flag == "run on airfield 1":
            if self.runtime != 0:
                self.runtime -= 1
                self.set_time += 1
                

            elif self.runtime == 0:
                self.flag = "placed in hungar"
                self.surf.fill(BLACK)
                pygame.display.update()
            
            sc.blit(self.surf, (self.pos['x']-25, self.pos['y']-50))
            pygame.display.update()


    def get_flag(self):
        return self.flag

    def get_set_time(self):
        return self.set_time


class Field():
    def __init__(self, time):
        self.time_to_use = time
        self.stuff = False
        self.last_plane = ""

    def get_time(self):
        return self.time_to_use

    def set_stuff(self, stf, pl):
        self.stuff = stf
        self.last_plane = int(pl)

    def get_stuff(self):
        return self.stuff

    def clear_field(self, pl, flag):
        if self.last_plane == pl and flag == "placed in hungar":
            self.stuff = False




## -------------------------- Класс окна программы -----------------------------------




class MainWindow(QMainWindow, Ui_MainWindow, Plane, Field):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow
        self.setupUi(self)
        self.win_flag = "stopped"

        self.start_button.clicked.connect(self.start_am)
        self.stop_button.clicked.connect(self.stop_am)
        

    def stop_am(self):
        self.win_flag = "stopped"



    def start_am(self):

        names = self.planes_names_edit.text().split()
        time_to_airport_area = self.planes_time_edit.text().split()

        if (self.f1_time_edit.text() != '' and self.f2_time_edit.text() != '' and self.MS_cof_edit.text() != '' and
            self.planes_names_edit.text() != '' and self.planes_time_edit.text() != '' and len(names) == len(time_to_airport_area)):
        
            APS_TIME = 0    #В минутах
            
            self.win_flag = "running"
            f1 = Field(int(self.f1_time_edit.text()))
            f2 = Field(int(self.f2_time_edit.text()))
            MS_cof = int(self.MS_cof_edit.text())
            #print(names)
            #print(time_to_airport_area)

            p = []
            for i in range(len(names)):
                p.append(Plane(int(time_to_airport_area[i]), str(names[i])))

            sc_update()

            

            while self.win_flag == "running":
                
                s_out = ""

                for i in range(len(names)):
                    p[i].fly_to_airport()

                for i in range(len(names)):
                    p[i].appearance()

                for i in range(len(names)):
                    p[i].fly_to_POC()

                for i in range(len(names)):
                    p[i].fly_to_F1(f1.get_stuff(), f1.get_time(), APS_TIME)

                for i in range(len(names)):
                    p[i].fly_to_F2(f1.get_stuff(), f2.get_stuff(), f2.get_time(), APS_TIME)

                for i in range(len(names)):
                    p[i].turn(f1.get_stuff(), f2.get_stuff())

                for i in range(len(names)):
                    p[i].run_on_field()

                for i in range(len(names)):
                    if p[i].get_flag() == "fly to field 1" or p[i].get_flag() == "run on airfield 1":
                        f1.set_stuff(True, i)

                for i in range(len(names)):
                    if p[i].get_flag() == "fly to field 2" or p[i].get_flag() == "run on airfield 2":
                        f2.set_stuff(True, i)

                for i in range(len(names)):
                    f1.clear_field(i, p[i].get_flag())
                
                for i in range(len(names)):
                    f2.clear_field(i, p[i].get_flag())



                if f1.get_stuff() == True:
                    pygame.draw.rect(sc, RED, (125, 100, 50, 225), 5)
                    for i in range(4):
                        pygame.draw.line(sc, RED, (150, 125 + i*50), (150, 150 + i*50), 4)
                    pygame.display.update()
                else:
                    pygame.draw.rect(sc, GREEN, (125, 100, 50, 225), 5)
                    for i in range(4):
                        pygame.draw.line(sc, GREEN, (150, 125 + i*50), (150, 150 + i*50), 4)
                    pygame.display.update()

                if f2.get_stuff() == True:
                    pygame.draw.rect(sc, RED, (250, 100, 50, 225), 5)
                    for i in range(4):
                        pygame.draw.line(sc, RED, (275, 125 + i*50), (275, 150 + i*50), 4)
                    pygame.display.update()
                else:
                    pygame.draw.rect(sc, GREEN, (250, 100, 50, 225), 5)
                    for i in range(4):
                        pygame.draw.line(sc, GREEN, (275, 125 + i*50), (275, 150 + i*50), 4)
                    pygame.display.update()
                



                s_out = "Время отсчета в модели:  " + str(APS_TIME) + " мин." + "\n\n"

                for i in range(len(names)):
                    if p[i].get_flag() == "detected":
                        s_out += names[i] + ": " + "Вне ВП аэропорта еще " + str(p[i].get_TTAA()) + " мин." + "\n\n"

                    elif p[i].get_flag() == "fly to POC" or p[i].get_flag() == "stay in POC" or p[i].get_flag == "ready to appearance":
                        s_out += names[i] + ":  " + "Ожидает распределения на полосу" + "\n\n"

                    elif p[i].get_flag() == "turning":
                        s_out += names[i] + ":  " + "Выполняет маневр разворота" + "\n\n"

                    elif p[i].get_flag() == "fly to field 1":
                        s_out += names[i] + ":  " + "Летит к полосе номер 1" + "\n\n"

                    elif p[i].get_flag() == "run on airfield 1":
                        s_out += names[i] + ":  " + "Приземляется на полосу номер 1" + "\n\n"

                    elif p[i].get_flag() == "fly to field 2":
                        s_out += names[i] + ":  " + "Летит к полосе номер 2" + "\n\n"

                    elif p[i].get_flag() == "run on airfield 2":
                        s_out += names[i] + ":  " + "Приземляется на полосу номер 2" + "\n\n"

                    elif p[i].get_flag() == "placed in hungar":
                        s_out += names[i] + ":  " + "Разместился в ангаре в " + str(p[i].get_set_time()) + "мин." + "\n\n"

                self.status_out.setText(s_out)
                    
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()

                if self.win_flag == "running":
                    sleep(60/MS_cof)
                    APS_TIME += 1
            
            if self.win_flag == "stopped":
                APS_TIME = 0
                sc.fill(BLACK)
                self.MS_cof_edit.clear()
                self.f1_time_edit.clear()
                self.f2_time_edit.clear()
                self.planes_names_edit.clear()
                self.planes_time_edit.clear()
                pygame.display.update()
        
        else:
            self.status_out.setText("Ошибка ввода!")




## -------------------------- Тело программы -----------------------------------


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()   
    sys.exit(app.exec())