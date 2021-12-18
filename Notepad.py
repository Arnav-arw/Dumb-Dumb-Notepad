import wx

app = wx.App()
frm = wx.Frame(None, title="Simple Text Editor", size=(600,400))
bkg = wx.Panel(frm)

''''
def OnOpen(event):
    """

    Load a file into the textField.
    """
    dialog = wx.FileDialog(None,'Notepad',style = wx.OPEN)
    if dialog.ShowModal() == wx.ID_OK:
        filename.SetValue(dialog.GetPath())
        file = open(dialog.GetPath())
        contents.SetValue(file.read())
        file.close()
    dialog.Destroy()

def OnSave(event):
    """

    Save text into the orignal file.
    """
    if filename.GetValue() == '':
        dialog = wx.FileDialog(None,'Notepad',style = wx.SAVE)
        if dialog.ShowModal() == wx.ID_OK:
            filename.SetValue(dialog.GetPath())
            file = open(dialog.GetPath(), 'w')
            file.write(contents.GetValue())
            file.close()
        dialog.Destory()
    else:
        file = open(filename.GetValue(), 'w')
        file.write(contents.GetValue())
        file.close()

# Define a 'load' button and its label, bind to an button event with a function 'load'
loadButton = wx.Button(bkg, label='Open')
loadButton.Bind(wx.EVT_BUTTON, OnOpen)

# Define a 'save' button and its label, bind to an button event with a function 'save'
saveButton = wx.Button(bkg, label='Save')
saveButton.Bind(wx.EVT_BUTTON, OnSave)

# Use sizer to set relative position of the components.
# Horizontal layout
hbox = wx.BoxSizer()
hbox.Add(loadButton, proportion=0, flag=wx.LEFT, border=5)
hbox.Add(saveButton, proportion=0, flag=wx.LEFT, border=5)
'''

# Define a textBox for file contents.
contents = wx.TextCtrl(bkg, style=wx.TE_MULTILINE | wx.HSCROLL)


# Vertical layout
vbox = wx.BoxSizer(wx.VERTICAL)
#vbox.Add(hbox, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
vbox.Add(contents, proportion=1,flag=wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT, border=5)

bkg.SetSizer(vbox)

frm.Show()

app.MainLoop()
