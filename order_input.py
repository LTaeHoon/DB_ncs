# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx

import mysql.connector
from mysql.connector import errorcode

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
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"주문 접수", pos = wx.DefaultPosition, size = wx.Size( 750,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        #self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
        
        m_radioBox1Choices = [ u"테이블1", u"테이블2", u"테이블3", u"테이블4",u"테이블5",u"테이블6", u"전체"]
        self.m_radioBox1 = wx.RadioBox( self.m_panel1, wx.ID_ANY, u"테이블 선택", wx.DefaultPosition, wx.DefaultSize, m_radioBox1Choices, 1, wx.RA_SPECIFY_ROWS )
        self.m_radioBox1.SetSelection( 0 )
        bSizer2.Add( self.m_radioBox1, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        self.m_panel1.SetSizer( bSizer2 )
        self.m_panel1.Layout()
        bSizer2.Fit( self.m_panel1 )
        bSizer1.Add( self.m_panel1, 1, wx.ALL|wx.EXPAND, 5 )
        
        self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer3 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_panel6 = wx.Panel( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_button1 = wx.Button( self.m_panel6, wx.ID_ANY, u"봉골레", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer5.Add( self.m_button1, 1, wx.ALL|wx.EXPAND, 5 )
        
        self.m_button3 = wx.Button( self.m_panel6, wx.ID_ANY, u"알리오 올리오", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer5.Add( self.m_button3, 1, wx.ALL|wx.EXPAND, 5 )
        
        self.m_button4 = wx.Button( self.m_panel6, wx.ID_ANY, u"투움바파스타", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer5.Add( self.m_button4, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        self.m_panel6.SetSizer( bSizer5 )
        self.m_panel6.Layout()
        bSizer5.Fit( self.m_panel6 )
        bSizer3.Add( self.m_panel6, 1, wx.EXPAND|wx.ALL, 5 )
        
        self.m_panel7 = wx.Panel( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
        
        m_choice1Choices = ['0','1','2','3','4','5','6','7','8','9','10']
        self.m_choice1 = wx.Choice( self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice1Choices, 0 )
        self.m_choice1.SetSelection( 0 )
        bSizer6.Add( self.m_choice1, 1, wx.ALL|wx.EXPAND, 5 )
        
        m_choice2Choices = ['0','1','2','3','4','5','6','7','8','9','10']
        self.m_choice2 = wx.Choice( self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice2Choices, 0 )
        self.m_choice2.SetSelection( 0 )
        bSizer6.Add( self.m_choice2, 1, wx.ALL|wx.EXPAND, 5 )
        
        m_choice3Choices = ['0','1','2','3','4','5','6','7','8','9','10']
        self.m_choice3 = wx.Choice( self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice3Choices, 0 )
        self.m_choice3.SetSelection( 0 )
        bSizer6.Add( self.m_choice3, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        self.m_panel7.SetSizer( bSizer6 )
        self.m_panel7.Layout()
        bSizer6.Fit( self.m_panel7 )
        bSizer3.Add( self.m_panel7, 1, wx.EXPAND |wx.ALL, 5 )
        
        
        self.m_panel2.SetSizer( bSizer3 )
        self.m_panel2.Layout()
        bSizer3.Fit( self.m_panel2 )
        bSizer1.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer4 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_panel9 = wx.Panel( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_button7 = wx.Button( self.m_panel9, wx.ID_ANY, u"고르곤졸라", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer7.Add( self.m_button7, 1, wx.ALL|wx.EXPAND, 5 )
        
        self.m_button8 = wx.Button( self.m_panel9, wx.ID_ANY, u"나폴리 피자", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer7.Add( self.m_button8, 1, wx.ALL|wx.EXPAND, 5 )
        
        self.m_button9 = wx.Button( self.m_panel9, wx.ID_ANY, u"루꼴라 피자", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer7.Add( self.m_button9, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        self.m_panel9.SetSizer( bSizer7 )
        self.m_panel9.Layout()
        bSizer7.Fit( self.m_panel9 )
        bSizer4.Add( self.m_panel9, 1, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel10 = wx.Panel( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
        
        m_choice4Choices = ['0','1','2','3','4','5','6','7','8','9','10']
        self.m_choice4 = wx.Choice( self.m_panel10, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice4Choices, 0 )
        self.m_choice4.SetSelection( 0 )
        bSizer8.Add( self.m_choice4, 1, wx.ALL|wx.EXPAND, 5 )
        
        m_choice5Choices = ['0','1','2','3','4','5','6','7','8','9','10']
        self.m_choice5 = wx.Choice( self.m_panel10, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice5Choices, 0 )
        self.m_choice5.SetSelection( 0 )
        bSizer8.Add( self.m_choice5, 1, wx.ALL|wx.EXPAND, 5 )
        
        m_choice6Choices = ['0','1','2','3','4','5','6','7','8','9','10']
        self.m_choice6 = wx.Choice( self.m_panel10, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice6Choices, 0 )
        self.m_choice6.SetSelection( 0 )
        bSizer8.Add( self.m_choice6, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        self.m_panel10.SetSizer( bSizer8 )
        self.m_panel10.Layout()
        bSizer8.Fit( self.m_panel10 )
        bSizer4.Add( self.m_panel10, 1, wx.EXPAND |wx.ALL, 5 )
        
        
        self.m_panel3.SetSizer( bSizer4 )
        self.m_panel3.Layout()
        bSizer4.Fit( self.m_panel3 )
        bSizer1.Add( self.m_panel3, 1, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel8 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_button12 = wx.Button( self.m_panel8, wx.ID_ANY, u"주문조회", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer9.Add( self.m_button12, 0, wx.ALIGN_LEFT|wx.ALL, 5 )
        
        self.m_button11 = wx.Button( self.m_panel8, wx.ID_ANY, u"주문접수", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer9.Add( self.m_button11, 0, wx.ALIGN_LEFT|wx.ALL, 5 )
        
        self.btn2 = wx.Button( self.m_panel8, wx.ID_ANY, u"삭제", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer9.Add( self.btn2, 0, wx.ALIGN_LEFT|wx.ALL, 5 )
        
        self.m_panel8.SetSizer( bSizer9 )
        self.m_panel8.Layout()
        bSizer9.Fit( self.m_panel8 )
        bSizer1.Add( self.m_panel8, 1, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel11 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer10 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.lstView = wx.ListCtrl( self.m_panel11, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
        bSizer10.Add( self.lstView, 1, wx.ALL, 5 )
        
        
        
        self.m_panel11.SetSizer( bSizer10 )
        self.m_panel11.Layout()
        bSizer10.Fit( self.m_panel11 )
        bSizer1.Add( self.m_panel11, 1, wx.EXPAND |wx.ALL, 5 )
        
        
        self.SetSizer( bSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        self.lstView.InsertColumn(0, '주문번호',width=70)  
        self.lstView.InsertColumn(1, '테이블번호',width=70)
        self.lstView.InsertColumn(2, '메뉴명',width=120)
        self.lstView.InsertColumn(3, '수량',width=70)
        self.lstView.InsertColumn(4, '단가',width=70)
        self.lstView.InsertColumn(5, '합계',width=70)
        self.lstView.InsertColumn(6, '계산여부',width=70)
        self.lstView.InsertColumn(7, '주문일시',width=150)
        
        self.InitDB()
        # Connect Events
        self.m_button1.Bind( wx.EVT_BUTTON, self.pasta1_clk )
        self.m_button3.Bind( wx.EVT_BUTTON, self.pasta2_clk )
        self.m_button4.Bind( wx.EVT_BUTTON, self.pasta3_clk )
        self.m_button7.Bind( wx.EVT_BUTTON, self.pizza1_clk )
        self.m_button8.Bind( wx.EVT_BUTTON, self.pizza2_clk )
        self.m_button9.Bind( wx.EVT_BUTTON, self.pizza3_clk )
        self.m_button11.Bind( wx.EVT_BUTTON, self.input_data )
        self.m_button12.Bind(wx.EVT_BUTTON,self.order_check)
        self.btn2.Bind( wx.EVT_BUTTON, self.onClickDel )
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    #DB 초기화 작업 함수 호출
    def InitDB(self):
        try:
            conn = mysql.connector.connect(**config)       
            cursor = conn.cursor()
            sql = "show tables"
            cursor.execute(sql)
            
            # 테이블 유무 검사 
            tables = cursor.fetchall()
            tables_num = 0
            #테이블이 전혀 없는 경우
            if len(tables) ==0:
                sql = "create or replace table order_table(order_no int auto_increment primary key, table_no int, menu varchar(30), su int, dan int, price int, pay_yn varchar(1),sdate DATETIME DEFAULT CURRENT_TIMESTAMP)"
                cursor.execute(sql)
                print('create order table')
            
            for i in tables:
                tables_num += 1    
                if i[0] == 'order_table':
                    print('order table exist')
                    break; # 테이블 있으면 반복 탈출 
                elif tables_num == len(tables): # 테이블이 없는 경우 
                    # code : 기본키, 자동1씩 증가
                    sql = "create or replace table order_table(order_no int auto_increment primary key, table_no int, menu varchar(30), su int, dan int, price int, pay_yn varchar(1),sdate DATETIME DEFAULT CURRENT_TIMESTAMP)"
                    cursor.execute(sql)
                    print('create order table')
                
            """ sql = "select * from order_table"
            cursor.execute(sql)
            datas = cursor.fetchall()
            
            if  len(datas) > 0:  
                for row in datas:     
                    i = self.lstView.InsertItem(7, 0)              
                    self.lstView.SetItem(i, 0, str(row[0]))
                    self.lstView.SetItem(i, 1, str(row[1]))                
                    self.lstView.SetItem(i, 2, row[2])
                    self.lstView.SetItem(i, 3, str(row[3]))
                    self.lstView.SetItem(i, 4, str(row[4]))
                    self.lstView.SetItem(i, 5, str(row[5]))
                    self.lstView.SetItem(i, 6, row[6])
                    #self.m_listCtrl1.SetItem(i, 7, str(int(row[2]) * int(row[3]))) # 칼럼 없음
                     """
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
    def pasta1_clk( self, event ):
        event.Skip()
    
    def pasta2_clk( self, event ):
        event.Skip()
    
    def pasta3_clk( self, event ):
        event.Skip()
    
    def pizza1_clk( self, event ):
        event.Skip()
    
    def pizza2_clk( self, event ):
        event.Skip()
    
    def pizza3_clk( self, event ):
        event.Skip()
    
    #주문조회버튼
    def order_check(self,event):
        tno = self.m_radioBox1.GetSelection()+1
        tnostr = self.m_radioBox1.GetStringSelection()
        print(tnostr)
        
        try:
            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()
            if tnostr !='전체':
                sql = "SELECT * FROM order_table where table_no='%s' ORDER BY order_no ASC"%tno
            else :
                sql ="select * from order_table order by order_no ASC"
            cursor.execute(sql)
            datas = cursor.fetchall()
            
            self.lstView.DeleteAllItems()
            if  len(datas) > 0:  
                for row in datas:  
                       
                    i = self.lstView.InsertItem(100, 0)              
                    print(i)
                    self.lstView.SetItem(i, 0, str(row[0]))
                    self.lstView.SetItem(i, 1, str(row[1]))                
                    self.lstView.SetItem(i, 2, row[2])
                    self.lstView.SetItem(i, 3, str(row[3]))
                    self.lstView.SetItem(i, 4, str(row[4]))
                    self.lstView.SetItem(i, 5, str(row[5]))
                    self.lstView.SetItem(i, 6, row[6])
                    self.lstView.SetItem(i, 7, str(row[7]))
                    #self.m_listCtrl1.SetItem(i, 7, str(int(row[2]) * int(row[3]))) # 칼럼 없음
            
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
                
    #주문접수
    def input_data( self, event ):
        tno=self.m_radioBox1.GetSelection()+1
        sus =[] # 수량 빈 리스트
        menus =[] #메뉴 빈 리스트
        dans =[]
        if int(self.m_choice1.GetStringSelection())>0 :
            sus.append(int(self.m_choice1.GetStringSelection()))
            menus.append(self.m_button1.GetLabel())
            dans.append(15000)
        if int(self.m_choice2.GetStringSelection())>0 :
            sus.append(int(self.m_choice2.GetStringSelection()))
            menus.append(self.m_button3.GetLabel())
            dans.append(12000)
        if int(self.m_choice3.GetStringSelection())>0 :
            sus.append(int(self.m_choice3.GetStringSelection()))
            menus.append(self.m_button4.GetLabel())
            dans.append(13000)
        if int(self.m_choice4.GetStringSelection())>0 :
            sus.append(int(self.m_choice4.GetStringSelection()))
            menus.append(self.m_button7.GetLabel())
            dans.append(18000)
        if int(self.m_choice5.GetStringSelection())>0 :
            sus.append(int(self.m_choice5.GetStringSelection()))
            menus.append(self.m_button8.GetLabel())
            dans.append(20000)
        if int(self.m_choice6.GetStringSelection())>0 :
            sus.append(int(self.m_choice6.GetStringSelection()))
            menus.append(self.m_button9.GetLabel())
            dans.append(25000)       
            
        print(sus)
        try:
            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()
            if self.m_radioBox1.GetStringSelection() !='전체' and len(sus)==0:
                wx.MessageBox('수량을 입력하세요.')
            if self.m_radioBox1.GetStringSelection() =='전체':
                wx.MessageBox('테이블 전체 선택시에는 주문접수가 안됩니다.')
            else :
                for i in range(len(sus)):      
                    print(i)
                    price = sus[i]*dans[i]
                    menu = menus[i]
                    su = sus[i]
                    dan = dans[i]
                    sdata=(tno,menu,su,dan,price,"n")
                    print(sdata)
                    sql = "insert into order_table(table_no, menu, su, dan, price, pay_yn) values(%s,%s,%s,%s,%s,%s)"
                    cursor.execute(sql, sdata)
                    conn.commit()
                    
            #수량 초기화 
            self.m_choice1.SetSelection(0)
            self.m_choice2.SetSelection(0)
            self.m_choice3.SetSelection(0)
            self.m_choice4.SetSelection(0)
            self.m_choice5.SetSelection(0)
            self.m_choice6.SetSelection(0)
            sql = "SELECT * FROM order_table where pay_yn='n' and table_no='%s' ORDER BY order_no ASC"%tno
            cursor.execute(sql)
            datas = cursor.fetchall()
            
            self.lstView.DeleteAllItems()
            if  len(datas) > 0:  
                for row in datas:  
                       
                    i = self.lstView.InsertItem(100, 0)              
                    print(i)
                    self.lstView.SetItem(i, 0, str(row[0]))
                    self.lstView.SetItem(i, 1, str(row[1]))                
                    self.lstView.SetItem(i, 2, row[2])
                    self.lstView.SetItem(i, 3, str(row[3]))
                    self.lstView.SetItem(i, 4, str(row[4]))
                    self.lstView.SetItem(i, 5, str(row[5]))
                    self.lstView.SetItem(i, 6, row[6])
                    self.lstView.SetItem(i, 7, str(row[7]))
                    #self.m_listCtrl1.SetItem(i, 7, str(int(row[2]) * int(row[3]))) # 칼럼 없음
            
            
        
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
            
    def onClickDel( self, event ):       
        # 선택된 항목 수  
        tno = self.m_radioBox1.GetSelection()+1
        select = self.lstView.GetSelectedItemCount()
        
        if select > 0 : # item을 한 개 이상 선택한 경우 
            idx = self.lstView.GetFirstSelected()  # 선택된 첫번째 항목
             
            del_code = self.lstView.GetItemText(idx, col=0)
            
            try:
                conn = mysql.connector.connect(**config)
                cursor = conn.cursor()
                            
                sql = "delete from order_table where order_no=" + str(del_code)
                cursor.execute(sql) # sql문 실행
                conn.commit()

                # 레코드 검색 
                sql = "select * from order_table where table_no="+str(tno)            
                cursor.execute(sql)
            
                # ListView 표시 
                self.lstView.DeleteAllItems()
                  
                for row in cursor:  
                       
                    i = self.lstView.InsertItem(100, 0)              
                    print(i)
                    self.lstView.SetItem(i, 0, str(row[0]))
                    self.lstView.SetItem(i, 1, str(row[1]))                
                    self.lstView.SetItem(i, 2, row[2])
                    self.lstView.SetItem(i, 3, str(row[3]))
                    self.lstView.SetItem(i, 4, str(row[4]))
                    self.lstView.SetItem(i, 5, str(row[5]))
                    self.lstView.SetItem(i, 6, row[6])
                    self.lstView.SetItem(i, 7, str(row[7]))
                    #self.m_listCtrl1.SetItem(i, 7, str(int(row[2]) * int(row[3]))) # 칼럼 없음
            
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                    print('id or password 오류')
                elif err.errno == errorcode.ER_BAD_DB_ERROR:
                    print('db 오류')
                else:
                    print('기타 에러 : ', err)
                    conn.rollback()
            finally:
                cursor.close(); conn.close()                 
        else :
            wx.MessageBox('선택 항목이 없습니다.')         
if __name__ == "__main__" : #Python 프로그램 시작점
    app = wx.App()#어플리케이션 생성
    frame = MyFrame1(None).Show()#프레임 생성
    app.MainLoop()#어플리케이션 실행


