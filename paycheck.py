# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

import mysql.connector
from mysql.connector import errorcode
from _overlapped import NULL

config = {
        'user' : 'scott',
        'password' : 'tiger',
        'host' : '127.0.0.1',
        'database' : 'work',
        'port' : '3306'
    }

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"계산", pos = wx.DefaultPosition, size = wx.Size( 697,451 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        #self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        bSizer5 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_panel7 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer7 = wx.BoxSizer( wx.VERTICAL )
        
        sel_radioChoices = [ u"1번", u"2번", u"3번", u"4번", u"5번", u"6번" ]
        self.sel_radio = wx.RadioBox( self.m_panel7, wx.ID_ANY, u"계산", wx.DefaultPosition, wx.DefaultSize, sel_radioChoices, 6, wx.RA_SPECIFY_COLS )
        self.sel_radio.SetSelection( 0 )
        self.sel_radio.SetFont( wx.Font( 18, 75, 90, 90, False, "굴림" ) )
        
        bSizer7.Add( self.sel_radio, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        self.m_panel7.SetSizer( bSizer7 )
        self.m_panel7.Layout()
        bSizer7.Fit( self.m_panel7 )
        bSizer5.Add( self.m_panel7, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.m_panel8 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer9 = wx.BoxSizer( wx.VERTICAL )
        
        self.orderList = wx.ListCtrl( self.m_panel8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
        bSizer9.Add( self.orderList, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        self.m_panel8.SetSizer( bSizer9 )
        self.m_panel8.Layout()
        bSizer9.Fit( self.m_panel8 )
        bSizer5.Add( self.m_panel8, 1, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel9 = wx.Panel( self, wx.ID_ANY, wx.Point( -1,-1 ), wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer8 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_button2 = wx.Button( self.m_panel9, wx.ID_ANY, u"계산하기", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
        bSizer8.Add( self.m_button2, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
        
        
        self.m_panel9.SetSizer( bSizer8 )
        self.m_panel9.Layout()
        bSizer8.Fit( self.m_panel9 )
        bSizer5.Add( self.m_panel9, 0, wx.ALL|wx.EXPAND, 5 )
        
        
        self.SetSizer( bSizer5 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        
        
        
        
        # 리스트 컨트롤 칼럼 추가1 
        self.orderList.InsertColumn(0, '주문번호', width = 80)
        self.orderList.InsertColumn(1, 'Table 이름', width = 100)
        self.orderList.InsertColumn(2, '메뉴', width = 120)
        self.orderList.InsertColumn(3, '수량', width = 100)
        self.orderList.InsertColumn(4, '단가', width = 100)
        self.orderList.InsertColumn(5, '합계', width = 80)
        self.orderList.InsertColumn(6, '계산여부', width = 100)
        
        # DB 초기화 작업 함수 호출 추가2  
        self.InitDB()
        
        # Connect Events
        self.sel_radio.Bind( wx.EVT_RADIOBOX, self.radiEvent )
        self.m_button2.Bind( wx.EVT_BUTTON, self.onClick_Pay )
        
    def __del__( self ):
        pass
    
    
    # DB 초기화 작업 함수 호출 추가5
    def InitDB(self):
        try : 
            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()
            sql = 'show tables'
            cursor.execute(sql)
            
            # 테이블 유무 검사
            tables = cursor.fetchall()
            tables_num = 0
            
            for i in tables :
                tables_num += 1
                if i[0] == 'order_table' :
                    print('order_table table exist')
                    break;
                elif tables_num == len(tables): 
                    print('테이블이 없습니다')
                    '''
                    # 나중에 수정할 것
                    sql = "create table order_table(주문번호 integer auto_increment primary key, Table이름 integer, 메뉴 text, 수량 integer, 단가 integer, 계산여부 text, 합계 integer)"
                    sql2 = "insert into order_table (Table이름, 메뉴, 수량, 단가, 계산여부, 합계) values(1, '스파게티', 3, 10000, 'N', 30000)"
                    sql3 = "insert into order_table (Table이름, 메뉴, 수량, 단가, 계산여부, 합계) values(2, '콜라', 3, 10000, 'N', 30000)"
                    sql4 = "insert into order_table (Table이름, 메뉴, 수량, 단가, 계산여부, 합계) values(3, '리조또', 3, 10000, 'N', 30000)"
                    sql5 = "insert into order_table (Table이름, 메뉴, 수량, 단가, 계산여부, 합계) values(4, '피자', 3, 10000, 'N', 30000)"
                    sql6 = "insert into order_table (Table이름, 메뉴, 수량, 단가, 계산여부, 합계) values(5, '감자피자', 3, 10000, 'N', 30000)"
                    sql7 = "insert into order_table (Table이름, 메뉴, 수량, 단가, 계산여부, 합계) values(6, '사이다', 3, 10000, 'N', 30000)"
                    sql8 = "insert into order_table (Table이름, 메뉴, 수량, 단가, 계산여부, 합계) values(2, '햄버거', 3, 10000, 'N', 30000)"
                    sql9 = "insert into order_table (Table이름, 메뉴, 수량, 단가, 계산여부, 합계) values(5, '스테이크', 3, 10000, 'N', 30000)"
                    
                    cursor.execute(sql)
                    cursor.execute(sql2)
                    cursor.execute(sql3)
                    cursor.execute(sql4)
                    cursor.execute(sql5)
                    cursor.execute(sql6)
                    cursor.execute(sql7)
                    cursor.execute(sql8)
                    cursor.execute(sql9)
                    
                    conn.commit()
                    '''
            
            # radio 박스로 테이블 선택 적용
            sel = self.sel_radio.GetSelection()
            sql = "select * from order_table where table_no = '%s'"%sel
            sql = 'select * from order_table'
            cursor.execute(sql)
            datas = cursor.fetchall()
            
            # 리스트 컨트롤에 레코드 출력
            if len(datas) > 0 : 
                for row in datas :
                    i = self.orderList.InsertItem(7, 0)
                    self.orderList.SetItem(i, 0, str(row[0]))
                    self.orderList.SetItem(i, 1, str(row[1]))
                    self.orderList.SetItem(i, 2, row[2])
                    self.orderList.SetItem(i, 3, str(row[3]))
                    self.orderList.SetItem(i, 4, str(row[4]))
                    self.orderList.SetItem(i, 5, str(row[5]))
                    self.orderList.SetItem(i, 6, str(row[6]))
            
            
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print('id or password 오류')
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print('db 오류')
            else:
                print('기타 에러 : ', err)
            conn.rollback()
        finally:
            #cursor.execute('drop table order_table')
            cursor.close()
            conn.close()

    
    # Virtual event handlers, overide them in your derived class
    def radiEvent( self, event ):
        # radio 박스로 테이블 선택 적용
        #self.orderList.ClearAll()
        self.orderList.DeleteAllItems()
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        
        sel_temp = self.sel_radio.GetSelection()
        sel = sel_temp + 1
        sql = "select * from order_table where table_no = '%s' and pay_yn='n'"%sel
        cursor.execute(sql)
        datas = cursor.fetchall()
            
        # 리스트 컨트롤에 레코드 출력
        
        if len(datas) > 0 : 
            i = 0
            for row in datas :
                i = self.orderList.InsertItem(7, 0)
                self.orderList.SetItem(i, 0, str(row[0]))
                self.orderList.SetItem(i, 1, str(row[1]))
                self.orderList.SetItem(i, 2, row[2])
                self.orderList.SetItem(i, 3, str(row[3]))
                self.orderList.SetItem(i, 4, str(row[4]))
                self.orderList.SetItem(i, 5, str(row[5]))
                self.orderList.SetItem(i, 6, str(row[6]))
                
    
    def onClick_Pay( self, event ):
        #event.Skip()
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        
        sel_temp = self.sel_radio.GetSelection()
        sel = sel_temp + 1
        sql = "update order_table set pay_yn = 'Y' where table_no = '%s'"%sel
        cursor.execute(sql)
        
        conn.commit()
        
        sql = "select * from order_table where table_no= '%s'"%sel
        cursor.execute(sql)
        datas = cursor.fetchall()
        
        # 리스트 컨트롤에 레코드 출력
        self.orderList.DeleteAllItems()

        if len(datas) > 0 : 
            for row in datas :
                i = self.orderList.InsertItem(7, 0)
                self.orderList.SetItem(i, 0, str(row[0]))
                self.orderList.SetItem(i, 1, str(row[1]))
                self.orderList.SetItem(i, 2, row[2])
                self.orderList.SetItem(i, 3, str(row[3]))
                self.orderList.SetItem(i, 4, str(row[4]))
                self.orderList.SetItem(i, 5, str(row[5]))
                self.orderList.SetItem(i, 6, str(row[6]))
 
 
if __name__ == "__main__" : # python 프로그램 시작점을 지정하는 문구(앞의 코드를 무시하고 여기서부터 시작함)
    app = wx.App() # 1. 애플리케이션 생성
    frame = MyFrame1(parent = None) # 2. 프레임 생성
    frame.Show() # 3. 프레임 보이기
    app.MainLoop() # 4. 애플리케이션 실행