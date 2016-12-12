# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx 

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
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"지점 조회", pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        #self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText1 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"지점 : ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )
        bSizer2.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        m_choice1Choices = [ u"서울 강남 가로수길점", u"서울 강남 청담점", u"서울 서초 교대역점", u"서울 송파 석촌호수점", u"서울 용산 이태원점", u"서울 종로 삼청점", u"경기 성남 판교역점", u"경기 고양 백석역점", u"인천 송도 센트럴파크점", u"부산 마린시티점" ]
        self.m_choice1 = wx.Choice( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice1Choices, 0 )
        self.m_choice1.SetSelection( 4 )
        self.m_choice1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        
        bSizer2.Add( self.m_choice1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        self.m_panel1.SetSizer( bSizer2 )
        self.m_panel1.Layout()
        bSizer2.Fit( self.m_panel1 )
        bSizer1.Add( self.m_panel1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer3 = wx.BoxSizer( wx.VERTICAL )
        
        self.AR_loc = wx.ListCtrl( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,wx.LC_REPORT )
        bSizer3.Add( self.AR_loc, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
        
        
        self.m_panel2.SetSizer( bSizer3 )
        self.m_panel2.Layout()
        bSizer3.Fit( self.m_panel2 )
        bSizer1.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel5 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer5 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_bitmap2 = wx.StaticBitmap( self.m_panel5, wx.ID_ANY, wx.Bitmap(u"main_visual.jpg", wx.BITMAP_TYPE_ANY), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer5.Add( self.m_bitmap2, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
        
        
        self.m_panel5.SetSizer( bSizer5 )
        self.m_panel5.Layout()
        bSizer5.Fit( self.m_panel5 )
        bSizer1.Add( self.m_panel5, 1, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText2 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"지점수 : ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        bSizer4.Add( self.m_staticText2, 0, wx.ALL, 5 )
        
        self.m_staticText3 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"10", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )
        bSizer4.Add( self.m_staticText3, 0, wx.ALL, 5 )
        
        
        self.m_panel3.SetSizer( bSizer4 )
        self.m_panel3.Layout()
        bSizer4.Fit( self.m_panel3 )
        bSizer1.Add( self.m_panel3, 0, wx.EXPAND |wx.ALL, 5 )
        
        
        self.SetSizer( bSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # 리스트 컨트롤 칼럼 추가
        self.AR_loc.InsertColumn(0, 'Branch', width = 200)
        self.AR_loc.InsertColumn(1, 'Phone', width = 200)
        self.AR_loc.InsertColumn(2, 'Address', width = 300)
        
        # 리스트 내용
        Branch = ['서울 강남 가로수길점', '서울 강남 청담점', '서울 서초 교대점', '서울 종로 삼청점', '서울 용산 이태원점', '서울 송파 석촌호수점', '경기 성남 판교역점', '경기 고양 백석역점', '인천 송도 센트럴파크점']
        Phone = ['02-111-1111', '02-222-2222', '02-333-3333', '02-444-4444', '02-555-5555', '02-666-6666', '031-111-1111', '031-222-2222', '032-111-1111']
        Address = ['서울특별시 강남구 강남대로 ', '서울 강남구 청담동', '서울 서초구 서초대로', '서울 종로구 삼청동', '서울 용산구 이태원로', '서울 송파구 송파동' ,'경기도 성남시 분당구 판교동', '경기도 고양시 일산구 백석동', '인천 연수구 송도동']
        
        for i in range(len(Branch)) :
            c = self.AR_loc.InsertItem(3, 0)
            self.AR_loc.SetItem(c, 0, str(Branch[i]))
            self.AR_loc.SetItem(c, 1, str(Phone[i]))
            self.AR_loc.SetItem(c, 2, str(Address[i]))

        # Connect Events
        self.m_choice1.Bind( wx.EVT_CHOICE, self.OnChoice_loc )
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def OnChoice_loc( self, event ):
        #evnet.skip()
        choice = self.m_choice1.GetSelection()
        #지도 출력
        if choice == 0 :
            self.m_bitmap2.SetBitmap(wx.Bitmap('loc01.png'))
        elif choice == 1 :
            self.m_bitmap2.SetBitmap(wx.Bitmap('loc02.png'))
        elif choice == 2 :
            self.m_bitmap2.SetBitmap(wx.Bitmap('loc03.png'))
        elif choice == 3 :
            self.m_bitmap2.SetBitmap(wx.Bitmap('loc04.png'))
        elif choice == 4 :
            self.m_bitmap2.SetBitmap(wx.Bitmap('loc05.png'))
        
if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame1(None).Show()
    app.MainLoop()