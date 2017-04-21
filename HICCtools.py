#coding: utf-8
import wx, os, shutil, os.path,glob
from datetime import datetime
from subprocess import call
tiempo=datetime.now()
calendario=('XD','Enero!','Febrero!','Marzo!','Abril!','Mayo!','Junio!','Julio!','Agosto!','Septiembre!','Obtubre!','Nobiembre!','Diciembre!')
calendar= (calendario[tiempo.month])
if (tiempo.hour > 12):
    Hora= (str(tiempo.hour-12)+":0"+str(tiempo.minute)+(': PM'))
else:
    Hora=(str(tiempo.hour)+":0"+str(tiempo.minute)+(': AM'))
comando2="hostname"
tubo = os.popen(comando2)
datos = tubo.readlines()
nombre_pc = datos[0].split(" ")[-1].split("\n")[0]
class Vt1(wx.Frame):#definicion de clase
    #comando1= "osk"
    #tubo = os.popen(comando1)
    def __init__(self, parent):#inizializador
        wx.Frame.__init__(self, parent=parent,title="Login HICC TS",size=(270,200))
        self.CreateStatusBar()
        #szh = wx.FlexGridSizer(rows=3, cols=3, hgap=5, vgap=1)
        #self.Center()#centrar la ventana
        self.panel = wx.Panel(self)#
        self.sizer = wx.GridBagSizer(3,2)#tamaño de acomodo
        self.textoU =wx.StaticText(self.panel, label="Usuario:")#etiqueta / texto estatico
        self.textoU.SetForegroundColour('blue')
        self.sizer.Add(self.textoU,pos=(0,0),flag=wx.TOP|wx.LEFT|wx.BOTTOM,border=1)


        self.textoP = wx.StaticText(self.panel, label="Password:")
        self.textoP.SetForegroundColour('blue')
        self.sizer.Add(self.textoP,pos=(1,0),flag=wx.TOP|wx.LEFT|wx.BOTTOM,border=1)

        self.textoR = wx.StaticText(self.panel, label="Respuesta")
        self.textoR.SetForegroundColour('blue')
        self.sizer.Add(self.textoR,pos=(2,0),flag=wx.TOP|wx.LEFT|wx.BOTTOM,border=1)

        self.textoFecha = wx.StaticText(self.panel, label=(str(tiempo.day)+'/'+str(tiempo.month)+'/'+str(tiempo.year)+" "+calendar))
        self.sizer.Add(self.textoFecha,pos=(4,0),flag=wx.TOP|wx.LEFT|wx.BOTTOM,border=1)
        self.textoFecha.SetForegroundColour('blue')

        self.textoFec = wx.StaticText(self.panel, label=str(Hora))
        self.sizer.Add(self.textoFec,pos=(5,0),flag=wx.TOP|wx.LEFT|wx.BOTTOM,border=1)
        self.textoFec.SetForegroundColour('blue')

        self.textoeditU = wx.TextCtrl(self.panel,style=wx.TE_CENTER)
        self.sizer.Add(self.textoeditU,pos=(0,1), span= (1,3), flag=wx.EXPAND|wx.RIGHT,)
        self.textoeditU.SetForegroundColour('#269839')

        self.textoeditP = wx.TextCtrl(self.panel,style=wx.TE_PASSWORD|wx.TE_CENTER)
        self.sizer.Add(self.textoeditP,pos =(1,1), span=(1,3), flag=wx.EXPAND|wx.RIGHT,)
        self.textoeditP.SetForegroundColour('#269839')

        self.boton = wx.Button(self.panel,label= 'Entrar',size =(50,25))
        self.sizer.Add(self.boton,pos =(3,3), flag=wx.RIGHT|wx.BOTTOM)

        self.panel.Bind(wx.EVT_BUTTON,self.Validar,self.boton)
        self.panel.SetSizerAndFit(self.sizer)
    def Validar (self, event):
        usuario=self.textoeditU.GetValue()
        password=self.textoeditP.GetValue()
        if (usuario == '' and password == ''):
            self.textoR.SetForegroundColour("#1F903D")
            self.textoR.SetLabel('(PASS)')
            dlg = wx.MessageDialog(None, u'¿Desea continuar?',u'HCC', wx.YES_NO|wx.ICON_QUESTION)
            dialogo = dlg.ShowModal()
            if(dialogo == wx.ID_YES ):
                self.Close(True)
                nv = Vt2(None)
                nv.Centre()
                nv.Show()
            else:
                dlg.Destroy()
        else:
            self.textoR.SetLabel(u'( *****Usuario y/o Contraseña incorrecta!***** )')
            self.textoR.SetForegroundColour("#FF0000")
            self.Refresh()

tubo = os.popen('hostname')
datos = tubo.readlines()
nombre_pc = datos[0].split(" ")[-1].split("\n")[0]
#crea el Bat para llamar ActivationWizardDotNet
def CrearArchivoA():
    archivo=open('ActivationWizardDotNet.bat','w')
    archivo.close()
def EscribeArchivoA():
    archivo=open('ActivationWizardDotNet.bat','a')
    archivo.write('@echo off\n')
    archivo.write('C:\n')
    archivo.write('cd C:\Program Files\Neurotechnology \n')
    archivo.write('ActivationWizardDotNet.exe\n')
    archivo.write('exit\n')
    archivo.close()
    
#crea el BAT EnableAll.bat
def CrearArchivoE():
    archivo=open('EnableAll.bat','w')
    archivo.close()
def EscribeArchivoE():
    archivo=open('EnableAll.bat','a')
    archivo.write('@ECHO OFF\n')
    archivo.write('SET registryExecutable=reg\n')
    archivo.write('SET registryKey=HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\n')
    archivo.write('SET registryValue=Shell\n')
    archivo.write('SET registryType=REG_sz\n')
    archivo.write('SET registryData=explorer.exe\n')
    archivo.write('%registryExecutable% add "%registryKey%" /v "%registryValue%" /t %registryType% /d %registryData% /f \n')
    archivo.write('@echo off\n')
    archivo.write('reg delete "HKEY_CURRENT_USER\Software\Microsoft\CTF\LangBar" /v /f ShowStatus\n')
    archivo.write('@echo off\n')
    archivo.write('reg delete "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Keyboard Layout" /f\n')
    archivo.write('shutdown -r -t 1\n')
    archivo.write('exit')
    archivo.close()
#crea el BAT DisableAll.bat
def CrearArchivoD():
    archivo=open('DisableAll.bat','w')
    archivo.close()
def EscribeArchivoD():
    archivo=open('DisableAll.bat','a')
    archivo.write('@ECHO OFF\n')
    archivo.write('SET registryExecutable=reg\n')
    archivo.write('SET registryKey=HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\n')
    archivo.write('SET registryValue=Shell\n')
    archivo.write('SET registryType=REG_sz\n')
    archivo.write('SET registryData="C:\Program Files (x86)\HiSoft\Shell\DeviceShell.exe"\n')
    archivo.write('%registryExecutable% add "%registryKey%" /v "%registryValue%" /t %registryType% /d %registryData% /f \n')
    archivo.write('@echo off\n')
    archivo.write('reg add "HKEY_CURRENT_USER\Software\Microsoft\CTF\LangBar" /v ShowStatus /t REG_DWORD /d 3 /f\n')
    archivo.write('@ECHO OFF\n')
    archivo.write('SET registryExecutable=reg\n')
    archivo.write('SET registryKey=HKLM\SYSTEM\CurrentControlSet\Control\Keyboard Layout\n')
    archivo.write('SET registryValue=Scancode Map\n')
    archivo.write('SET registryType=REG_BINARY\n')
    archivo.write('SET registryData=00000000000000000900000000005be000005ce000005de00000440000001d000000380000001de0000038e000000000\n')
    archivo.write('%registryExecutable% add "%registryKey%" /v "%registryValue%" /t %registryType% /d %registryData% /f \n')
    archivo.write('shutdown -r -t 1\n')
    archivo.write('exit')
    archivo.close()

class Vt2(wx.Frame):
    def __init__(self, parent):
        #Crear barra de menu
        barra_menu = wx.MenuBar()
        #menu archivo
        menu_Archivo = wx.Menu()
        m_Abrir = menu_Archivo.Append(-1,"&Explorer\tE-R","Explorador de Archivos")
        m_Salir = menu_Archivo.Append(-1, "&Salir\tQ-W","Salir del Programas")
        m_Acerca = menu_Archivo.Append(-1, "&Acerca de ","Info")

        #agregando el menu principal
        barra_menu.Append(menu_Archivo,"Archivo")
        wx.Frame.__init__(self, parent,title =(nombre_pc) ,size=(520,220))
        #szh = wx.BoxSizer(wx.VERTICAL)
        szh = wx.FlexGridSizer(rows=3, cols=3, hgap=5, vgap=1)
        #creando botones
        boton1 = wx.Button(self,-1,u"         Crear Carpeta        ")
        szh.Add(boton1,1,wx.ALL,10)
        boton2 =wx.Button(self,-1,u"      Respaldar (LIC)       ")
        szh.Add(boton2,1,wx.ALL,10)
        boton3 =wx.Button(self,-1,u"     Neuro tecnology    ")
        szh.Add(boton3, 1,wx.ALL,10)
        boton4 =wx.Button(self,-1,u"Administrador de tareas")
        szh.Add(boton4,1,wx.ALL,10)
        boton5 =wx.Button(self,-1,u"Desbloqueo escritorio ")
        szh.Add(boton5,1,wx.EXPAND|wx.ALL,10)
        boton6 =wx.Button(self,-1,u"Bloqueo del escritorio ")
        szh.Add(boton6,1,wx.EXPAND|wx.ALL,10)
        boton7 =wx.Button(self,-1,u"       Reiniciar             ")
        szh.Add(boton7,1,wx.EXPAND|wx.ALL,10)
        boton8 =wx.Button(self,-1,u"           Apagar          ")
        szh.Add(boton8,1,wx.EXPAND|wx.ALL,10)
        boton9 =wx.Button(self,-1,u"Respaldo Rapido")
        szh.Add(boton9,1,wx.EXPAND|wx.ALL,10)

        #aplicar los cambios
        self.CreateStatusBar()
        self.SetMenuBar(barra_menu)
        self.SetSizer(szh)




        #captuta evento de botones
        self.Bind(wx.EVT_BUTTON, self.onClickButton1,boton1)#crea carpeta------->listo
        self.Bind(wx.EVT_BUTTON, self.onClickButton2,boton2)#respalda lic--------->listo
        self.Bind(wx.EVT_BUTTON, self.onClickButton3,boton3)#llama neuro tecnolog------->listo
        self.Bind(wx.EVT_BUTTON, self.onClickButton4,boton4)#Administrador de tareas----->listo
        self.Bind(wx.EVT_BUTTON, self.onClickButton5,boton5)#bloqueo de escritorio------->listo
        self.Bind(wx.EVT_BUTTON, self.onClickButton6,boton6)#desbloque----->listo
        self.Bind(wx.EVT_BUTTON, self.onClickButton7,boton7)#reiniciar ----->listo
        self.Bind(wx.EVT_BUTTON, self.onClickButton8,boton8)#apagar------->listo
        self.Bind(wx.EVT_BUTTON, self.onClickButton9,boton9) #Respaldo rapido------>listo
        #captura evento menu

        self.Bind(wx.EVT_MENU,self.salir, m_Salir)
        self.Bind(wx.EVT_MENU,self.OnOpen,m_Abrir)
        self.Bind(wx.EVT_MENU,self.info,m_Acerca)






       #funciones del menu despues de capturarel menu
    def OnOpen(self,event):
        tubo = os.popen('explorer.exe')
    def info(self,event):
        wx.MessageBox(u"SSAS departemento de tecnologia CASA ")
        wx.MessageBox(u"Autor Luis Gabriel Liscano Lovera ccidbcomputacion12@gmail.com ")
    def salir(self,event):
        self.Close(True)



        #funciones de los botones
    def onClickButton1(self,event):
        try:
            ruta = os.getcwd()+"\\"
            carpeta = (nombre_pc)
            "Crear carpeta"
            os.mkdir(ruta+carpeta)
            wx.MessageBox(u"La carpeta a sido creada con el nombre del equipo")
            #shutil.copytree('nombre_pc','D:/')
        except (WindowsError):
            wx.MessageBox(u"La carpeta ya ¡Existe!")
    def onClickButton2(self,event):
        existe = os.path.exists(nombre_pc)
        print (existe)
        if existe == True:
            files = glob.iglob(os.path.join('C:/Program Files/Neurotechnology/', "*.lic"))
            for file in files:
                if os.path.isfile(file):
                    shutil.copy2(file, 'D:/'+nombre_pc)
                    wx.MessageBox(u"Respaldo Exitoso!")
        else:
            wx.MessageBox(u"La carpeta No ¡Existe!")
    def onClickButton3(self,event):
        CrearArchivoA()
        EscribeArchivoA()       
        print ("PASS")
        call('ActivationWizardDotNet.bat')
        os.remove("EnableAll.bat")
    def onClickButton4(self,event):
        comandoA = ("taskmgr")
        tubo = os.popen(comandoA)
    def onClickButton5(self,event):
        dlg = wx.MessageDialog(None, u'¿Desbloquear el Dispositivo?',u'Atencion!', wx.YES_NO|wx.ICON_QUESTION)
        dialogo = dlg.ShowModal()
        if(dialogo == wx.ID_YES):
            CrearArchivoE()
            EscribeArchivoE()
            call("EnableAll.bat")
            os.remove("EnableAll.bat")
            wx.MessageBox(u"Desbloque Exitoso!")
        else:
            dlg.Destroy()
    def onClickButton6(self,event):
        dlg = wx.MessageDialog(None, u'¿Bloquear el Dispositivo?',u'Atencion!', wx.YES_NO|wx.ICON_QUESTION)
        dialogo = dlg.ShowModal()
        if(dialogo == wx.ID_YES):
            CrearArchivoD()
            EscribeArchivoD()
            call("DisableAll.bat")
            os.remove("DisableAll.bat")
            wx.MessageBox(u"Bloqueo ¡Exitoso!")
        else:
            dlg.Destroy()
    def onClickButton7(self,event):
        dlg = wx.MessageDialog(None, u'¿Reiniciar el Dispositivo?',u'Atencion!', wx.YES_NO|wx.ICON_QUESTION)
        dialogo = dlg.ShowModal()
        if(dialogo == wx.ID_YES):
             wx.MessageBox("Reiniciando Sistema")
             comandoR = ("shutdown -r -t 3")
             tubo = os.popen(comandoR)
        else:
             dlg.Destroy()
    def onClickButton8(self,event):
        dlg = wx.MessageDialog(None,u'¿Apagar el Dispositivo?','Atencion', wx.YES_NO|wx.ICON_QUESTION)
        dialogo = dlg.ShowModal()
        if (dialogo ==wx.ID_YES):
            wx.MessageBox("Apagando Sistema")
            comandoA = ("shutdown -s -t 3")
            tubo = os.popen(comandoA)
        else:
            dlg.Destroy()
    def onClickButton9(self,event):
        wx.MessageBox("Ten en cuenta que el dispositivo al finalizar el respaldo rapido reiniciara!")
        dlg = wx.MessageDialog(None, u'Proceder al Respaldo rapido?',u'Respaldo Rapido', wx.YES_NO|wx.ICON_QUESTION)
        dialogo = dlg.ShowModal()
        if(dialogo == wx.ID_YES ):
            try:
                ruta = os.getcwd()+"\\"
                carpeta = (nombre_pc)
                "Crear carpeta"
                os.mkdir(ruta+carpeta)
                wx.MessageBox(u"La carpeta a sido creada con el nombre del equipo")
                existe = os.path.exists(nombre_pc)
                if existe == True:
                    files = glob.iglob(os.path.join('C:/Program Files/Neurotechnology/', "*.lic"))
                    for file in files:
                        if os.path.isfile(file):
                            shutil.copy2(file, 'D:/'+nombre_pc)
                            wx.MessageBox(u"Respaldo Exitoso! Reiniciando.......")
                            comandoR = ("shutdown -r -t 4")
                            tubo = os.popen(comandoR)
                else:
                    wx.MessageBox(u"La carpeta No ¡Existe!")
            except (WindowsError):
                wx.MessageBox(u"La carpeta ya ¡Existe!")
        else:
            dlg.Destroy()

app = wx.App(False)
frame = Vt1(None)
frame.Show()
app.MainLoop()

