import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
# import openpyxl as xl
import stylesheet as style
import process as data
class getStartUI(QDialog):
    def __init__(self, parent=None):
        super().__init__()
        self.setWindowTitle("Vua Tiếng Việt")
        self.resize(1600, 900)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setStyleSheet(style.css)

        
        #background

        self.background = QWidget(self)
        self.background.setObjectName("background")
        self.background.setGeometry(QRect(
            0,
            40,
            self.width(),
            self.height()-40))
        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(10)
        self.shadow.setOffset(0, 0)
        self.shadow.setColor(QColor(0, 0, 0, 180))
        self.background.setGraphicsEffect(self.shadow)  

        #self.background.setStyleSheet("background-color: green")  
        

        #titlebar
        self.titlebar = QWidget(self)
        self.titlebar.setObjectName("titlebar")
        self.titlebar.setGeometry(QRect(
            self.background.x(), self.background.y(), self.background.width(), 40)) 
        self.titlebar_shadow = QGraphicsDropShadowEffect()
        self.titlebar_shadow.setBlurRadius(10)
        self.titlebar_shadow.setOffset(0)
        self.titlebar.setGraphicsEffect(self.titlebar_shadow)
        self.titlebar.setStyleSheet(style.basegui)
        #self.titlebar.setStyleSheet("background-color: black")

        self.exit_button = QPushButton(self.titlebar)
        self.exit_button.setObjectName("exit_button")
        self.exit_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.exit_button.setFixedSize(16, 16)
        self.exit_button.move(17, 12)
        self.exit_button.clicked.connect(self.closeDialog)

        self.minimize_button = QPushButton(self.titlebar)
        self.minimize_button.setObjectName("minimize_button")
        self.minimize_button.setCursor(self.exit_button.cursor())
        self.minimize_button.setFixedSize(16, 16)
        self.minimize_button.move(
            self.exit_button.x() + self.exit_button.width() + 10, 
            self.exit_button.y())
        self.minimize_button.clicked.connect(self.showMinimized)

        self.fullscreen_button = QPushButton(self.titlebar)
        self.fullscreen_button.setObjectName("fullscreen_button")
        self.fullscreen_button.setCursor(self.exit_button.cursor())
        self.fullscreen_button.setFixedSize(16, 16)
        self.fullscreen_button.move(
            self.minimize_button.x() + self.minimize_button.width() + 10, 
            self.minimize_button.y())



        #
        self.main_screen = QWidget(self.background)
        self.main_screen.setObjectName("main_screen")
        self.main_screen.setGeometry(QRect(
            0,
            self.titlebar.height(),
            self.width(),
           self.background.height()-self.titlebar.height()))

        #to check the logo_box pos
        #self.main_screen.setStyleSheet("background-color: red")

        #
        self.start_screen = QLabel(self.main_screen)
        self.start_screen.setObjectName("start_screen")   
        self.start_screen.setScaledContents(True)     
        self.start_screen.setPixmap(QPixmap("./image/gui/theme.png"))
        self.start_screen.resize(self.main_screen.size()) #not change
    
        #self.exit_button.setFixedSize(16, 16)

      
        self.start_button = QPushButton(self.start_screen)
        self.start_button.setObjectName("main_button")
        self.start_button.setDefault(True)
        self.start_button.setFixedSize(200, 50)
        self.start_button.move(230,self.start_screen.height()/2+200)
        self.start_button.setText("Bắt đầu")
        self.start_button.setFont(QFont("Arial Bold",30))
        self.start_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.start_button_shadow = QGraphicsDropShadowEffect()
        self.start_button_shadow.setBlurRadius(20)
        self.start_button_shadow.setOffset(1)
        #self.start_button.setGraphicsEffect(self.cstart_button_shadow)
        self.start_button.clicked.connect(self.gamePlayDialog)        

        #introduction button
        self.intro_button = QPushButton(self.start_screen)
        self.intro_button.setObjectName("main_button")
        self.intro_button.setDefault(True)
        self.intro_button.setFixedSize(200, 50)
        self.intro_button.move(self.start_button.x()+270,self.start_button.y())
        self.intro_button.setText("Luật chơi")
        self.intro_button.setFont(QFont("Arial Bold",30))
        self.intro_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.intro_button_shadow = QGraphicsDropShadowEffect()
        self.intro_button_shadow.setBlurRadius(20)
        self.intro_button_shadow.setOffset(1)
        self.intro_button.clicked.connect(self.introductionDialog)


        #
        self.intro_screen = QLabel(self.main_screen)
        self.intro_screen.setObjectName("intro_screen")   
        self.intro_screen.setScaledContents(True)     
        self.intro_screen.setPixmap(QPixmap("./image/gui/intro.png"))
        self.intro_screen.resize(self.main_screen.size()) #not change
        #self.exit_button.setFixedSize(16, 16)

        #
        #
        self.end_screen = QLabel(self.main_screen)
        self.end_screen.setObjectName("end_screen")   
        self.end_screen.setScaledContents(True)     
        self.end_screen.setPixmap(QPixmap("./image/gui/end_scr.png"))
        self.end_screen.resize(self.main_screen.size()) #not change
        #self.exit_button.setFixedSize(16, 16)

        #intro back
        self.intro_back = QPushButton(self.intro_screen)
        self.intro_back.setObjectName("sub_button")
        self.intro_back.setDefault(True)
        self.intro_back.setFixedSize(200, 50)
        self.intro_back.move(900,self.background.height()/2+50)
        self.intro_back.setText("Quay về")
        self.intro_back.setFont(QFont("Arial Bold",30))
        self.intro_back.setCursor(QCursor(Qt.PointingHandCursor))
        self.intro_back_shadow = QGraphicsDropShadowEffect()
        self.intro_back_shadow.setBlurRadius(15)
        self.intro_back_shadow.setOffset(0)
        self.intro_back.clicked.connect(self.mainScreenDialog)

        #
        self.game_play = QLabel(self.main_screen)
        self.game_play.setObjectName("game_play")   
        self.game_play.setScaledContents(True)     
        self.game_play.setPixmap(QPixmap("./image/gui/main_gp.png"))
        self.game_play.resize(self.main_screen.size()) #not change
        #self.exit_button.setFixedSize(16, 16)

        #show_ques

        self.show_ques=QLabel(self.game_play)
        self.show_ques.setObjectName("show_ques")  
        self.show_ques.setFixedSize(900, 120)
        self.show_ques.move(550,110)
        #self.show_ques.setStyleSheet("background-color: yellow")
        





        #
        self.clue_button = QPushButton(self.game_play)
        self.clue_button.setObjectName("sub_button")
        self.clue_button.setDefault(True)
        self.clue_button.setFixedSize(90, 60)
        self.clue_button.move(600,self.background.height()/2)
        self.clue_button.setText("Gợi ý")
        self.clue_button.setFont(QFont("Arial Bold",30))
        self.clue_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.clue_button.clicked.connect(self.showClue) 
        self.cntClue=0 
        

        #clue_box
        self.clue_box = QLabel(self.game_play)
        self.clue_box.setObjectName("show_clue")
        self.clue_box.setGeometry(QRect(self.show_ques.x(),self.show_ques.y()+self.show_ques.height(),900,150))
        
        #self.clue_box.move(self.clue_button.x()+600-10,self.clue_button.y())        
        self.clue_box.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        #self.clue_box.setStyleSheet("background-color: red")
        self.clue_box.setWordWrap(True)


        #result_box

        self.result_box = QLabel(self.game_play)
        self.result_box.setObjectName("result_box")
        
        self.result_box.setGeometry(QRect(self.clue_button.x()-40,self.clue_button.y()+80,880,200))
        #self.clue_box.move(self.clue_button.x()+600-10,self.clue_button.y())        
        #self.result_box.setStyleSheet("background-color: green")

        #result_noti
        self.result_noti=QLabel(self.result_box)
        self.result_noti.setObjectName("show_ques")
        self.result_noti.setFixedSize(self.result_box.width()-40, 50)
        self.result_noti.move(20,10)
        #self.result_noti.setStyleSheet("background-color: yellow")        
        self.result_noti.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.result_noti.setText("")
        self.result_noti.setWordWrap(True)

        #show_ans

        self.show_ans=QLabel(self.result_box)
        self.show_ans.setObjectName("show_clue")
        self.show_ans.setFixedSize(self.result_box.width()-40, self.result_box.height()-self.result_noti.height()-30)
        self.show_ans.move(20,self.result_noti.height()+20)
        #self.show_ans.setStyleSheet("background-color: pink")        
        self.show_ans.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)        
        self.show_ans.setText("")
        self.show_ans.setWordWrap(True)



        #next_button

        self.next_button = QPushButton(self.game_play)
        self.next_button.setObjectName("sub_button")
        self.next_button.setDefault(True)
        self.next_button.setFixedSize(210, 50)
        self.next_button.move(self.background.width()-300,self.background.height()-125)
        self.next_button.setText("Câu kế tiếp →")
        self.next_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.next_button.clicked.connect(self.gamePlayDialog)


        #next_button

        self.theEnd_button = QPushButton(self.game_play)
        self.theEnd_button.setObjectName("sub_button")
        self.theEnd_button.setDefault(True)
        self.theEnd_button.setFixedSize(210, 50)
        self.theEnd_button.move(self.background.width()-300,self.background.height()-125)
        self.theEnd_button.setText("Kết Thúc")
        self.theEnd_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.theEnd_button.clicked.connect(self.endDialog)




        
       
       #
        self.input_ans = QLineEdit(self.game_play)
        self.input_ans.setObjectName("input_ans")
        self.input_ans.setMaxLength(22)
        self.input_ans.setFocus()
        self.input_ans.setFixedSize(600, 60)
        self.input_ans.move(self.clue_button.x()+100,self.clue_button.y())        
        self.input_ans.setPlaceholderText("ĐÁP ÁN")
        self.input_ans.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.input_ans.returnPressed.connect(self.checkAns)
        

        #
        self.data=data.listQuestion("ques.txt")     
        self.currentQues=self.data[0]
        self.numQues=len(self.data)
        self.cnt=0


        #

        self.mainScreenDialog()
       
    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        #time.sleep(0.02)  # sleep for 20ms
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def closeDialog(self):
        sys.exit()

            
    #[ques,ans,keyAns,[clue1,clue2]]
   

    def mainScreenDialog(self):
        self.start_button.setDefault(True)        
        self.intro_button.setDefault(True)
        #self.intro_button.setDefault(True)
        self.start_screen.raise_() 

    
    def gamePlayDialog(self):
        self.currentQues=self.data[self.cnt]
        self.cntClue=0
        self.intro_screen.setHidden(True) 
        self.start_screen.setHidden(True)
        self.game_play.raise_() 
        self.clue_button.raise_()
        self.clue_button.setEnabled(True)
        self.clue_box.setHidden(True)
        self.theEnd_button.setVisible(False)
        self.next_button.setVisible(False)
        self.result_box.setVisible(False)
        self.showQues()       
                  


    def checkAns(self):
        currentAns=self.currentQues[2]
        playerAns=self.input_ans.text()
        self.input_ans.clear()
        if len(playerAns):
            if playerAns.lower()==currentAns.lower():
                noti=currentAns+" là câu trả lời chính xác!"
                ans=self.currentQues[1]
                self.cnt+=1
                self.correctAns()
            else:
                noti=playerAns+" là câu trả lời chưa chính xác!"
                ans=""
               
                
            self.showAns(noti,ans)
            


    def showAns(self,noti,ans):
        self.result_box.setVisible(True)    
        self.result_noti.setText(noti)
        self.show_ans.setText(ans)

    def correctAns(self):
        if self.cnt==self.numQues:
            self.theEnd_button.setVisible(True)
        else:
            self.next_button.setVisible(True)
        if self.clue_button.isEnabled():
            self.clue_button.setEnabled(False)
        
    def showClue(self):
        self.cntClue+=1
        self.clue_box.setHidden(False)
        if self.cntClue>1:
            self.clue_button.setEnabled(False)
            self.clue_box.setText(self.currentQues[3][self.cntClue-2]+self.currentQues[3][self.cntClue-1])
        else:
            self.clue_box.setText(self.currentQues[3][self.cntClue-1])
        
    def showQues(self):
        self.show_ques.setText(self.currentQues[0])
        self.show_ques.setWordWrap(True)
        self.show_ques.raise_()

    def introductionDialog(self):
        self.start_button.setDefault(False)        
        self.intro_button.setDefault(False)
        #self.intro_button.setDefault(True)
        self.intro_screen.raise_() 

    def endDialog(self):
        self.start_button.setDefault(False)        
        self.intro_button.setDefault(False)
        #self.intro_button.setDefault(True)
        self.end_screen.show()
        self.game_play.hide() 
 
        
        

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    QFontDatabase.addApplicationFont("./image/fonts/SanFranciscoDisplay-Regular.otf")
    QFontDatabase.addApplicationFont("./image/fonts/SanFranciscoDisplay-Bold.otf")
    QFontDatabase.addApplicationFont("./image/fonts/SanFranciscoDisplay-Medium.otf")
    QFontDatabase.addApplicationFont("./image/fonts/SanFranciscoDisplay-Thin.otf")
    # mainui = main.MainUI()
    # mainui.show()
    gstart=getStartUI()
    gstart.show()
    sys.exit(app.exec())



