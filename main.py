# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
# import wx.xrc

###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Acorn Restaurant", pos = wx.DefaultPosition, size = wx.Size( 465,490 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        # self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer2 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_bitmap1 = wx.StaticBitmap( self.m_panel1, wx.ID_ANY, wx.Bitmap( u"2.PNG", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.m_bitmap1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_bitmap2 = wx.StaticBitmap( self.m_panel1, wx.ID_ANY, wx.Bitmap( u"logo1.PNG", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.m_bitmap2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        
        self.m_panel1.SetSizer( bSizer2 )
        self.m_panel1.Layout()
        bSizer2.Fit( self.m_panel1 )
        bSizer1.Add( self.m_panel1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_button1 = wx.Button( self.m_panel2, wx.ID_ANY, u"주문입력", wx.DefaultPosition, wx.Size( 180,100 ), 0 )
        self.m_button1.SetMaxSize( wx.Size( 200,200 ) )
        
        bSizer3.Add( self.m_button1, 1, wx.ALL|wx.EXPAND, 5 )
        
        self.m_button2 = wx.Button( self.m_panel2, wx.ID_ANY, u"매출조회", wx.DefaultPosition, wx.Size( 180,100 ), 0 )
        self.m_button2.SetMaxSize( wx.Size( 200,200 ) )
        
        bSizer3.Add( self.m_button2, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        self.m_panel2.SetSizer( bSizer3 )
        self.m_panel2.Layout()
        bSizer3.Fit( self.m_panel2 )
        bSizer1.Add( self.m_panel2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_button3 = wx.Button( self.m_panel3, wx.ID_ANY, u"지점조회", wx.DefaultPosition, wx.Size( 180,100 ), 0 )
        self.m_button3.SetMaxSize( wx.Size( 200,200 ) )
        
        bSizer4.Add( self.m_button3, 0, wx.ALL, 5 )
        
        self.m_button4 = wx.Button( self.m_panel3, wx.ID_ANY, u"주문계산", wx.Point( -1,-1 ), wx.Size( 180,100 ), 0 )
        self.m_button4.SetMaxSize( wx.Size( 200,200 ) )
        
        bSizer4.Add( self.m_button4, 0, wx.ALL, 5 )
        
        
        self.m_panel3.SetSizer( bSizer4 )
        self.m_panel3.Layout()
        bSizer4.Fit( self.m_panel3 )
        bSizer1.Add( self.m_panel3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        
        self.SetSizer( bSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )
    
    
    # Connect Events
        self.m_button1.Bind( wx.EVT_BUTTON, self.onClickAdd1 )
        self.m_button2.Bind( wx.EVT_BUTTON, self.onClickAdd2 )
        self.m_button3.Bind( wx.EVT_BUTTON, self.onClickAdd3 )
        self.m_button4.Bind( wx.EVT_BUTTON, self.onClickAdd4 )
    
    
    def __del__( self ):
        pass
    
    
    
    # 주문 입력 버튼 클릭 
    def onClickAdd1( self, event ):
        import order_input                       # 수정: 모듈명
        app = wx.App()
        frame = order_input.MyFrame1(parent=None) # 수정: 모듈명.클래스명
        frame.Show()
        app.MainLoop()


    # 매출 조회 버튼 클릭 
    def onClickAdd2( self, event ):
        import search                      # 수정: 모듈명
        app = wx.App()
        frame = search.MyFrame2(parent=None) # 수정: 모듈명.클래스명
        frame.Show()
        app.MainLoop()
        
    # 지점 조회 버튼 클릭 
    def onClickAdd3( self, event ):
        import AR_loc# 수정: 모듈명
        app = wx.App()
        frame = AR_loc.MyFrame1(parent=None) # 수정: 모듈명.클래스명
        frame.Show()
        app.MainLoop()

    # 주문 계산 버튼 클릭 
    def onClickAdd4( self, event ):
        import paycheck                    # 수정: 모듈명
        app = wx.App()
        frame = paycheck.MyFrame1(parent=None) # 수정: 모듈명.클래스명
        frame.Show()
        app.MainLoop()       
        


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame2(None).Show()
    app.MainLoop() 
    
    
    