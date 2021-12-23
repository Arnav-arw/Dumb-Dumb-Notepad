import wx

class CreateMenu():
	def __init__(self,parent):
		self.menuBar=wx.MenuBar()
		self.file=wx.Menu()

        # File menu in menu bar
		self.open=self.file.Append(-1,'Open')
		self.save=self.file.Append(-1,'Save')
		self.file.AppendSeparator()
		self.close=self.file.Append(-1,'Close')
		self.menuBar.Append(self.file,'File')
		self.edit=wx.Menu()

        # Edit menu in menu bar
		self.undo=self.edit.Append(-1,'Undo')
		self.redo=self.edit.Append(-1,'Redo')
		self.edit.AppendSeparator()
		self.cut=self.edit.Append(-1,'Cut')
		self.copy=self.edit.Append(-1,'Copy')
		self.paste=self.edit.Append(-1,'Paste')
		self.edit.AppendSeparator()
		self.selectall=self.edit.Append(-1,'Select All')
		self.menuBar.Append(self.edit,'Edit')

		parent.SetMenuBar(self.menuBar)


class MyApp(wx.App):

	def OnInit(self):
		self.file=''

        # Window sizing and positioning
		self.frame=wx.Frame(parent=None,title='Pad Master',size=(800,600))
		self.panel=wx.Panel(self.frame,-1)
		self.menu=CreateMenu(self.frame)
		self.text=wx.TextCtrl(self.panel,-1,pos=(2,2),size=(795,580),style=wx.HSCROLL|wx.TE_MULTILINE)

        # Action list
		self.Bind(wx.EVT_MENU,self.OnOpen,self.menu.open)
		self.Bind(wx.EVT_MENU,self.OnSave,self.menu.save)
		self.Bind(wx.EVT_MENU,self.OnClose,self.menu.close)
		self.Bind(wx.EVT_MENU,self.OnUndo,self.menu.undo)
		self.Bind(wx.EVT_MENU,self.OnRedo,self.menu.redo)
		self.Bind(wx.EVT_MENU,self.OnCut,self.menu.cut)
		self.Bind(wx.EVT_MENU,self.OnCopy,self.menu.copy)
		self.Bind(wx.EVT_MENU,self.OnPaste,self.menu.paste)
		self.Bind(wx.EVT_MENU,self.OnSelectAll,self.menu.selectall)

		self.frame.Show()
		return True

    # Action implementation
	def OnOpen(self,event):
		dialog=wx.FileDialog(None,'Pad Master',style=wx.FD_OPEN)
		if dialog.ShowModal()==wx.ID_OK:
			self.file=dialog.GetPath()
			file=open(self.file)
			self.text.write(file.read())
			file.close()
		dialog.Destroy()

	def OnSave(self,event):
		if self.file=='':
			dialog=wx.FileDialog(None,'Pad Master',style=wx.FD_SAVE)
			if dialog.ShowModal()==wx.ID_OK:
				self.file=dialog.GetPath()
				self.text.SaveFile(self.file)
			dialog.Destroy()
		else:
			self.text.SaveFile(self.file)

	def OnClose(self,event):
		self.frame.Destroy()

	def OnUndo(self,event):
		self.text.Undo()

	def OnRedo(self,event):
		self.text.Redo()

	def OnCut(self,event):
		self.text.Cut()

	def OnCopy(self,event):
		self.text.Copy()

	def OnPaste(self,event):
		self.text.Paste()

	def OnSelectAll(self,event):
		self.text.SelectAll()

app=MyApp()
app.MainLoop()
