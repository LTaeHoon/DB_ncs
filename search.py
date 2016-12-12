# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import re
import mysql.connector
from mysql.connector import errorcode
from sre_parse import isdigit


config = {
  'user' : 'scott',
  'password' : 'tiger',
  'host' : '127.0.0.1',
  'database' : 'work',
  'port' : '3306'
}

###########################################################################
## Class MyFrame2
###########################################################################

aList = ['봉골레', '알리오 올리오', '투움바파스타', '고르곤졸라', '나폴리 피자', '루꼴라 피자']

class MyFrame2 ( wx.Frame ):
     
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title =u'매출조회', pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        #self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
        
        bSizer4 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel3.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
        
        bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText5 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"메뉴명", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )
        bSizer5.Add( self.m_staticText5, 1, wx.ALL|wx.EXPAND, 5 )
        ####################
        ####메뉴선택하는창#####
        ####################
        m_choice2Choices = []
        self.m_choice2 = wx.Choice( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice2Choices, 0 )
        self.m_choice2.SetSelection( 0 )
        bSizer5.Add( self.m_choice2, 1, wx.ALL|wx.EXPAND, 5 )
        
        #self.m_choice2 = wx.Choice(self.m_panle3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice2Choices, 0)
        for item in aList:
            self.m_choice2.Append(item)
        
        self.m_staticText6 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"날짜", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )
        bSizer5.Add( self.m_staticText6, 1, wx.ALL|wx.EXPAND, 5 )
        
        ####################
        ####날짜선택하는창#####
        ####################
        m_choice3Choices = []
        self.m_choice3 = wx.Choice( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice3Choices, 0 )
        self.m_choice3.SetSelection( 0 )
        bSizer5.Add( self.m_choice3, 1, wx.ALL|wx.EXPAND, 5 )
        sDate = ['2016-12-01', '2016-12-02', '2016-12-03', '2016-12-04', '2016-12-05', '2016-12-06',]
        
        for item in sDate:
            self.m_choice3.Append(item)
        
        self.m_button3 = wx.Button( self.m_panel3, wx.ID_ANY, u"조회", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer5.Add( self.m_button3, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        self.m_panel3.SetSizer( bSizer5 )
        self.m_panel3.Layout()
        bSizer5.Fit( self.m_panel3 )
        bSizer4.Add( self.m_panel3, 1, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.lstView = wx.ListCtrl( self.m_panel4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
        bSizer6.Add( self.lstView, 1, wx.ALL|wx.EXPAND, 5 )
        
        self.m_panel4.SetSizer( bSizer6 )
        self.m_panel4.Layout()
        bSizer6.Fit( self.m_panel4 )
        bSizer4.Add( self.m_panel4, 1, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel5 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_panel5.SetSizer( bSizer7 )
        self.m_panel5.Layout()
        bSizer7.Fit( self.m_panel5 )
        bSizer4.Add( self.m_panel5, 1, wx.ALIGN_RIGHT, 5 )
        
        self.m_staticText7 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"매출액", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )
        bSizer7.Add( self.m_staticText7, 0, wx.ALIGN_RIGHT, 5 )
        
        self.m_textCtrl7 = wx.TextCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer7.Add( self.m_textCtrl7, 0, wx.ALL, 5 )
        
        self.SetSizer( bSizer4 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        

        
        #조회창에 표시될 내용
        #리스트 컬럼 추가
        self.lstView.InsertColumn(0, '주문번호', width = 100)
        self.lstView.InsertColumn(1, '테이블번호', width = 100)
        self.lstView.InsertColumn(2, '메뉴이름', width = 100)
        self.lstView.InsertColumn(3, '수량', width = 100)
        self.lstView.InsertColumn(4, '단가', width = 100)
        self.lstView.InsertColumn(5, '금액', width = 150)
        self.lstView.InsertColumn(6, '계산여부', width = 100)
        self.lstView.InsertColumn(7, '날짜', width = 150)
        #self.lstView.InsertColumn(8, '매출', width = 150)
        
        
        # DB 초기화 작업 함수 호출 추가2  
        self.InitDB()
                                                            
        # Connect Events
        self.m_choice2.Bind( wx.EVT_CHOICE, self.Select_menu )
        
        self.m_choice3.Bind( wx.EVT_CHOICE, self.Select_date )
        
        self.m_button3.Bind( wx.EVT_BUTTON, self.search )
    
    
    
    def __del__( self ):
        pass
        # DB 초기화 작업 함수 호출 추가  
    def InitDB(self):
        try:
            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()
            sql = "show tables"
            cursor.execute(sql)
            
            # 테이블 유무 검사 
            tables = cursor.fetchall()
            tables_num = 0
            for i in tables:
                tables_num += 1 
                if i[0] == 'order_table':
                    print('order_table exist!!!!')
                    break; # 테이블 있으면 반복 탈출 
                elif tables_num == len(tables): # 테이블이 없는 경우 
                    print("Table doesn't exist!!!")
                    #OrderNumber(code) : 기본키, 자동1씩 증가
                    sql = "create or replace table order_table(order_no int auto_increment primary key, table_no int, menu varchar(30), su int, dan int, price int, pay_yn varchar(1), sdate DATETIME)"
                    #1. 주문번호, 2. 테이블번호, 3.메뉴이름, 4.수량, 5.단가, 6. 총액, 7.계산여부 8. 날짜
                    cursor.execute(sql)
                    #print('Drop Table Completed!!')
                    print('create order_table Completed!!')
            #테이블이 있을경우 실행되는 SQL 문

                    
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print('id or password 오류')
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print('db 오류')
            else:
                print('기타 에러 : ', err)
            conn.rollback()
        finally:
            cursor.close()
            conn.close()
    
    
    
    def Select_menu( self, event ):#메뉴클릭시
        pass
        
    def Select_date( self, event ):#날짜클릭시
        pass
    
    def search( self, event):#조회버튼클릭시
        print('조회버튼클릭됨')
        sMenu=self.m_choice2.GetStringSelection()
        print('선택된 메뉴',sMenu)
        
        try:
            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()
            #sMenu=self.m_choice2.GetStringSelection()
            print('선택된 메뉴',sMenu)
            sql = "select * from order_table where menu = '{}'".format(sMenu)
            cursor.execute(sql)
            # 리스트 컨트롤에 레코드 출력 
            self.lstView.DeleteAllItems()
            for row in cursor:
                    i = self.lstView.InsertItem(8, 0)    #7개의 칼럼          
                    self.lstView.SetItem(i, 0, str(row[0]))#주문번호
                    self.lstView.SetItem(i, 1, str(row[1]))     #테이블명
                    self.lstView.SetItem(i, 2, str(row[2]))#메뉴이름
                    self.lstView.SetItem(i, 3, str(row[3]))#수량
                    self.lstView.SetItem(i, 4, str(row[4]))#단가
                    self.lstView.SetItem(i, 5, str(row[3] * row[4]))#총액
                    self.lstView.SetItem(i, 6, str(row[6]))#계산여부
                    self.lstView.SetItem(i, 7, str(row[7]))#날짜
  
                    #1. 주문번호, 2. 테이블번호, 3.메뉴이름, 4.수량, 5.단가, 6. 총액, 7.계산여부 8. 날짜
            print("여기서 총액이 계산됨!")
            sql = "select sum(price) from order_table where pay_yn='Y' and menu = '{}'".format(sMenu)
            #cursor.execute(sql)  # 총합이 계산됨.
            #sql = "select sum(dan) from order_table"
            cursor.execute(sql)  # 총합이 계산됨.
            
            #datas = cursor.fetchall()
            result = cursor.fetchall()
            print(result)##[(Decimal('90000'),)]
            print(type(result)) ### Class<'list'>
            str1 = ' '.join(map(str, result))
            print("여기서 스트링")
            print(type(str1))### Class <'string'>
            print(str1) ####(Decimal('90000'),)

            s = int(re.search(r'\d+', str1).group())

            print(s)     
                
            
            self.m_textCtrl7.SetValue(str(s))
                    
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print('id or password 오류')
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print('db 오류')
            else:
                print('기타 에러 : ', err)
            conn.rollback()
        finally:
            cursor.close()
            conn.close()


#이 시점부터 프로그램을 시작함. 인터프리터에게 시작점을 알려주는 방법        
if __name__ == "__main__" : #Python 프로그램 시작점
    app = wx.App()#어플리케이션 생성
    frame = MyFrame2(None).Show()#프레임 생성
    app.MainLoop()#어플리케이션 실행