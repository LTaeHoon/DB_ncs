'''

1.로그인창 -첫화면

'''
import wx


###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"에이콘 식당", pos = wx.DefaultPosition, size = wx.Size( 400,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        #self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
        
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer3 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_bitmap1 = wx.StaticBitmap( self.m_panel1, wx.ID_ANY,wx.Bitmap( u"img.PNG", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.m_bitmap1, 1, wx.ALL|wx.EXPAND, 5 )
        

        
        
        self.m_panel1.SetSizer( bSizer3 )
        self.m_panel1.Layout()
        bSizer3.Fit( self.m_panel1 )
        bSizer1.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText1 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"아이디:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )
        bSizer2.Add( self.m_staticText1, 0, wx.ALL, 5 )
        
        self.m_textCtrl1 = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.m_textCtrl1, 0, wx.ALL, 5 )
        
        self.m_staticText2 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"비밀번호:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        bSizer2.Add( self.m_staticText2, 0, wx.ALL, 5 )
        
        self.m_textCtrl2 = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
        bSizer2.Add( self.m_textCtrl2, 0, wx.ALL, 5 )
        
        
        self.m_panel2.SetSizer( bSizer2 )
        self.m_panel2.Layout()
        bSizer2.Fit( self.m_panel2 )
        bSizer1.Add( self.m_panel2, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
        
        self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_button1 = wx.Button( self.m_panel3, wx.ID_ANY, u"로그인", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer4.Add( self.m_button1, 0, wx.ALL|wx.EXPAND, 5 )
        
 
        
        self.m_button2 = wx.Button( self.m_panel3, wx.ID_ANY, u"종료", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer4.Add( self.m_button2, 0, wx.ALL, 5 )
        
        
        self.m_panel3.SetSizer( bSizer4 )
        self.m_panel3.Layout()
        bSizer4.Fit( self.m_panel3 )
        bSizer1.Add( self.m_panel3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        
        self.SetSizer( bSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.m_button1.Bind( wx.EVT_BUTTON, self.onlogin )
        self.m_button2.Bind( wx.EVT_BUTTON, self.onlogout )
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def onlogin( self, event ):
        self.Close()
        
        from main import MyFrame2
        #from sql_team_work.main import MyFrame2
        app = wx.App()
        frame = MyFrame2(None)
        frame.Show()
        app.MainLoop()  
        
    
    def onlogout( self, event ):
        self.Close()
        
        
        
if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame1(None).Show()
    app.MainLoop()        
        
    