################################################################################
#OpenShortcut MAIN FILE
################################################################################
#Copyright (c) 2018 Jonas Melander
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.
################################################################################
#Importing required modules
import tkinter, os, webbrowser, pyHook;
from PIL import ImageTk, Image;

#Declaring global Variables including Shortcut set variables
ConfigStat=0; ShortcutNum=6;
Shortcut01_Type=""; Shortcut01_Path=""; Shortcut01_KeyB="";
Shortcut02_Type=""; Shortcut02_Path=""; Shortcut02_KeyB="";
Shortcut03_Type=""; Shortcut03_Path=""; Shortcut03_KeyB="";
Shortcut04_Type=""; Shortcut04_Path=""; Shortcut04_KeyB="";
Shortcut05_Type=""; Shortcut05_Path=""; Shortcut05_KeyB="";
Shortcut06_Type=""; Shortcut06_Path=""; Shortcut06_KeyB="";

#Function used to resolve what keycode the user entered key should have.
def ResolveKey(Key):
    print("DEBUG: Attempting to resolve key.");
    #Check key and return result if we find a match.
    if  (Key=="backspace"):        return "8";
    elif(Key=="tab"):              return "9";
    elif(Key=="enter"):            return "13";
    elif(Key=="shift"):            return "16";
    elif(Key=="ctrl"):             return "17";
    elif(Key=="alt"):              return "18";
    elif(Key=="pause/break"):      return "19";
    elif(Key=="caps lock"):        return "20";
    elif(Key=="escape"):           return "27";
    elif(Key=="page up"):          return "33";
    elif(Key=="page down"):        return "34";
    elif(Key=="end"):              return "35";
    elif(Key=="home"):             return "36";
    elif(Key=="left arrow"):       return "37";
    elif(Key=="up arrow"):         return "38";
    elif(Key=="right arrow"):      return "39";
    elif(Key=="down arrow"):       return "40";
    elif(Key=="insert"):           return "45";
    elif(Key=="delete"):           return "46";
    elif(Key=="0"):                return "48";
    elif(Key=="1"):                return "49";
    elif(Key=="2"):                return "50";
    elif(Key=="3"):                return "51";
    elif(Key=="4"):                return "52";
    elif(Key=="5"):                return "53";
    elif(Key=="6"):                return "54";
    elif(Key=="7"):                return "55";
    elif(Key=="8"):                return "56";
    elif(Key=="9"):                return "57";
    elif(Key=="a"):                return "65";
    elif(Key=="b"):                return "66";
    elif(Key=="c"):                return "67";
    elif(Key=="d"):                return "68";
    elif(Key=="e"):                return "69";
    elif(Key=="f"):                return "70";
    elif(Key=="g"):                return "71";
    elif(Key=="h"):                return "72";
    elif(Key=="i"):                return "73";
    elif(Key=="j"):                return "74";
    elif(Key=="k"):                return "75";
    elif(Key=="l"):                return "76";
    elif(Key=="m"):                return "77";
    elif(Key=="n"):                return "78";
    elif(Key=="o"):                return "79";
    elif(Key=="p"):                return "80";
    elif(Key=="q"):                return "81";
    elif(Key=="r"):                return "82";
    elif(Key=="s"):                return "83";
    elif(Key=="t"):                return "84";
    elif(Key=="u"):                return "85";
    elif(Key=="v"):                return "86";
    elif(Key=="w"):                return "87";
    elif(Key=="x"):                return "88";
    elif(Key=="y"):                return "89";
    elif(Key=="z"):                return "90";
    elif(Key=="left window key"):  return "91";
    elif(Key=="right window key"): return "92";
    elif(Key=="select key"):       return "93";
    elif(Key=="numpad 0"):         return "96";
    elif(Key=="numpad 1"):         return "97";
    elif(Key=="numpad 2"):         return "98";
    elif(Key=="numpad 3"):         return "99";
    elif(Key=="numpad 4"):         return "100";
    elif(Key=="numpad 5"):         return "101";
    elif(Key=="numpad 6"):         return "102";
    elif(Key=="numpad 7"):         return "103";
    elif(Key=="numpad 8"):         return "104";
    elif(Key=="numpad 9"):         return "105";
    elif(Key=="multiply"):         return "106";
    elif(Key=="add"):              return "107";
    elif(Key=="subtract"):         return "109";
    elif(Key=="decimal point"):    return "110";
    elif(Key=="divide"):           return "111";
    elif(Key=="F1"):               return "112";
    elif(Key=="F2"):               return "113";
    elif(Key=="F3"):               return "114";
    elif(Key=="F4"):               return "115";
    elif(Key=="F5"):               return "116";
    elif(Key=="F6"):               return "117";
    elif(Key=="F7"):               return "118";
    elif(Key=="F8"):               return "119";
    elif(Key=="F9"):               return "120";
    elif(Key=="F10"):              return "121";
    elif(Key=="F11"):              return "122";
    elif(Key=="F12"):              return "123";
    elif(Key=="num lock"):         return "144";
    elif(Key=="scroll lock"):      return "145";
    elif(Key=="semi-colon"):       return "186";
    elif(Key=="equal sign"):       return "187";
    elif(Key=="comma"):            return "188";
    elif(Key=="dash"):             return "189";
    elif(Key=="period"):           return "190";
    elif(Key=="forward slash"):    return "191";
    elif(Key=="grave accent"):     return "192";
    elif(Key=="open bracket"):     return "219";
    elif(Key=="back slash"):       return "220";
    elif(Key=="close braket"):     return "221";
    elif(Key=="single quote"):     return "222";

#Function used to reverse the keycode to text, used when populating from data file.
def ReverseKey(Key):
    print("DEBUG: Attempting to reverse key.");
    #Check key and return result if we find a match.
    if  (Key=="8"):   return "backspace";
    elif(Key=="9"):   return "tab";
    elif(Key=="13"):  return "enter";
    elif(Key=="16"):  return "shift";
    elif(Key=="17"):  return "ctrl";
    elif(Key=="18"):  return "alt";
    elif(Key=="19"):  return "pause/break";
    elif(Key=="20"):  return "caps lock";
    elif(Key=="27"):  return "escape";
    elif(Key=="33"):  return "page up";
    elif(Key=="34"):  return "page down";
    elif(Key=="35"):  return "end";
    elif(Key=="36"):  return "home";
    elif(Key=="37"):  return "left arrow";
    elif(Key=="38"):  return "up arrow";
    elif(Key=="39"):  return "right arrow";
    elif(Key=="40"):  return "down arrow";
    elif(Key=="45"):  return "insert";
    elif(Key=="46"):  return "delete";
    elif(Key=="48"):  return "0";
    elif(Key=="49"):  return "1";
    elif(Key=="50"):  return "2";
    elif(Key=="51"):  return "3";
    elif(Key=="52"):  return "4";
    elif(Key=="53"):  return "5";
    elif(Key=="54"):  return "6";
    elif(Key=="55"):  return "7";
    elif(Key=="56"):  return "8";
    elif(Key=="57"):  return "9";
    elif(Key=="65"):  return "a";
    elif(Key=="66"):  return "b";
    elif(Key=="67"):  return "c";
    elif(Key=="68"):  return "d";
    elif(Key=="69"):  return "e";
    elif(Key=="70"):  return "f";
    elif(Key=="71"):  return "g";
    elif(Key=="72"):  return "h";
    elif(Key=="73"):  return "i";
    elif(Key=="74"):  return "j";
    elif(Key=="75"):  return "k";
    elif(Key=="76"):  return "l";
    elif(Key=="77"):  return "m";
    elif(Key=="78"):  return "n";
    elif(Key=="79"):  return "o";
    elif(Key=="80"):  return "p";
    elif(Key=="81"):  return "q";
    elif(Key=="82"):  return "r";
    elif(Key=="83"):  return "s";
    elif(Key=="84"):  return "t";
    elif(Key=="85"):  return "u";
    elif(Key=="86"):  return "v";
    elif(Key=="87"):  return "w";
    elif(Key=="88"):  return "x";
    elif(Key=="89"):  return "y";
    elif(Key=="90"):  return "z";
    elif(Key=="91"):  return "left window key";
    elif(Key=="92"):  return "right window key";
    elif(Key=="93"):  return "select key";
    elif(Key=="96"):  return "numpad 0";
    elif(Key=="97"):  return "numpad 1";
    elif(Key=="98"):  return "numpad 2";
    elif(Key=="99"):  return "numpad 3";
    elif(Key=="100"): return "numpad 4";
    elif(Key=="101"): return "numpad 5";
    elif(Key=="102"): return "numpad 6";
    elif(Key=="103"): return "numpad 7";
    elif(Key=="104"): return "numpad 8";
    elif(Key=="105"): return "numpad 9";
    elif(Key=="106"): return "multiply";
    elif(Key=="107"): return "add";
    elif(Key=="109"): return "subtract";
    elif(Key=="110"): return "decimal point";
    elif(Key=="111"): return "divide";
    elif(Key=="112"): return "F1";
    elif(Key=="113"): return "F2";
    elif(Key=="114"): return "F3";
    elif(Key=="115"): return "F4";
    elif(Key=="116"): return "F5";
    elif(Key=="117"): return "F6";
    elif(Key=="118"): return "F7";
    elif(Key=="119"): return "F8";
    elif(Key=="120"): return "F9";
    elif(Key=="121"): return "F10";
    elif(Key=="122"): return "F11";
    elif(Key=="123"): return "F12";
    elif(Key=="144"): return "num lock";
    elif(Key=="145"): return "scroll lock";
    elif(Key=="186"): return "semi-colon";
    elif(Key=="187"): return "equal sign";
    elif(Key=="188"): return "comma";
    elif(Key=="189"): return "dash";
    elif(Key=="190"): return "period";
    elif(Key=="191"): return "forward slash";
    elif(Key=="192"): return "grave accent";
    elif(Key=="219"): return "open bracket";
    elif(Key=="220"): return "back slash";
    elif(Key=="221"): return "close braket";
    elif(Key=="222"): return "single quote";

#Function that is called once a keyboard event is detected.
def OpenShortcut_KeyboardEvent(event):
    print("DEBUG: Button with "+str(event.KeyID)+" as ID pressed.");
    #Load global Shortcut variables.
    global Shortcut01_Type; global Shortcut01_Path; global Shortcut01_KeyB;
    global Shortcut02_Type; global Shortcut02_Path; global Shortcut02_KeyB;
    global Shortcut03_Type; global Shortcut03_Path; global Shortcut03_KeyB;
    global Shortcut04_Type; global Shortcut04_Path; global Shortcut04_KeyB;
    global Shortcut05_Type; global Shortcut05_Path; global Shortcut05_KeyB;
    global Shortcut06_Type; global Shortcut06_Path; global Shortcut06_KeyB;
    #Check key press against Shortcut keys.
    if  (Shortcut01_KeyB==str(event.KeyID)): Type=Shortcut01_Type; Path=Shortcut01_Path;
    elif(Shortcut02_KeyB==str(event.KeyID)): Type=Shortcut02_Type; Path=Shortcut02_Path;
    elif(Shortcut03_KeyB==str(event.KeyID)): Type=Shortcut03_Type; Path=Shortcut03_Path;
    elif(Shortcut04_KeyB==str(event.KeyID)): Type=Shortcut04_Type; Path=Shortcut04_Path;
    elif(Shortcut05_KeyB==str(event.KeyID)): Type=Shortcut05_Type; Path=Shortcut05_Path;
    elif(Shortcut06_KeyB==str(event.KeyID)): Type=Shortcut06_Type; Path=Shortcut06_Path;
    else: Type="NULL";
    #Conduct keybound action if we have a match.
    if  (Type=="Type: Open Folder"):   os.startfile(Path);
    elif(Type=="Type: Open File"):     os.startfile(Path);
    elif(Type=="Type: Start Program"): os.startfile(Path);
    elif(Type=="Type: Open Website"):  webbrowser.open(Path);

#Hook the keyboard and subscribe(sets function) to key ups.
Hook=pyHook.HookManager(); Hook.SubscribeKeyUp(OpenShortcut_KeyboardEvent); Hook.HookKeyboard();

#Function used to handle the closing of the application.
def OpenShortcut_Exit():
    print("DEBUG: Exiting application.");
    #Disconnect so we dont get an error and then unhook keyboard.
    Hook.disconnect(0,0); Hook.UnhookKeyboard();
    #Finally close the application.
    root.destroy();

#The main tkinter GUI class used for the application.
class OpenShortcut_GUI(tkinter.Frame):
    #Function used to initialize the gui.
    def __init__(self,master=None):
        print("DEBUG: __init__.");
        tkinter.Frame.__init__(self,master);
        #Building the GUI elements and loading data from memory.
        self.OpenShortcut_BuildGUI(); self.OpenShortcut_LoadData();
        #Setting window sizing.
        master.minsize(width=399,height=112); master.maxsize(width=399,height=112);
        #Setting the default logic for windows closing of application so we can make sure that we close everything correctly.
        root.protocol("WM_DELETE_WINDOW",OpenShortcut_Exit);

    #Load data function used for loading in the users pre-defined Shortcut settings such as file paths and key codes.
    def OpenShortcut_LoadData(self):
        print("DEBUG: Loading data.");
        #Global variable declarations.
        global ShortcutNum;
        global Shortcut01_Type; global Shortcut01_Path; global Shortcut01_KeyB;
        global Shortcut02_Type; global Shortcut02_Path; global Shortcut02_KeyB;
        global Shortcut03_Type; global Shortcut03_Path; global Shortcut03_KeyB;
        global Shortcut04_Type; global Shortcut04_Path; global Shortcut04_KeyB;
        global Shortcut05_Type; global Shortcut05_Path; global Shortcut05_KeyB;
        global Shortcut06_Type; global Shortcut06_Path; global Shortcut06_KeyB;
        #Open data files and extract data to variables, images and text objects.
        r=0;
        while(r != ShortcutNum):
            r=r+1;
            with open("Data/Shortcut0"+str(r)) as f:
                for i, line in enumerate(f):
                    if  (i==0): line=line.rstrip(); Type=line;
                    elif(i==1): line=line.rstrip(); Path=line;
                    elif(i==2): line=line.rstrip(); KeyB=line;
            #Determine what image to assign.
            if  (Type=="Type: Open Folder"):   ShortcutIco=self.Type_Folder;
            elif(Type=="Type: Open File"):     ShortcutIco=self.Type_File;
            elif(Type=="Type: Start Program"): ShortcutIco=self.Type_Software;
            elif(Type=="Type: Open Website"):  ShortcutIco=self.Type_Website;
            elif(Type=="Type: None"):          ShortcutIco=self.Type_None;
            #Conduct Shortcut number specific operations.
            if  (r==1): Shortcut01_Type=Type; Shortcut01_Path=Path; Shortcut01_KeyB=KeyB; self.Shortcut01_Ico.config(i=ShortcutIco); self.Shortcut01_Txt.config(text="Key: "+str(ReverseKey(KeyB)));
            elif(r==2): Shortcut02_Type=Type; Shortcut02_Path=Path; Shortcut02_KeyB=KeyB; self.Shortcut02_Ico.config(i=ShortcutIco); self.Shortcut02_Txt.config(text="Key: "+str(ReverseKey(KeyB)));
            elif(r==3): Shortcut03_Type=Type; Shortcut03_Path=Path; Shortcut03_KeyB=KeyB; self.Shortcut03_Ico.config(i=ShortcutIco); self.Shortcut03_Txt.config(text="Key: "+str(ReverseKey(KeyB)));
            elif(r==4): Shortcut04_Type=Type; Shortcut04_Path=Path; Shortcut04_KeyB=KeyB; self.Shortcut04_Ico.config(i=ShortcutIco); self.Shortcut04_Txt.config(text="Key: "+str(ReverseKey(KeyB)));
            elif(r==5): Shortcut05_Type=Type; Shortcut05_Path=Path; Shortcut05_KeyB=KeyB; self.Shortcut05_Ico.config(i=ShortcutIco); self.Shortcut05_Txt.config(text="Key: "+str(ReverseKey(KeyB)));
            elif(r==6): Shortcut06_Type=Type; Shortcut06_Path=Path; Shortcut06_KeyB=KeyB; self.Shortcut06_Ico.config(i=ShortcutIco); self.Shortcut06_Txt.config(text="Key: "+str(ReverseKey(KeyB)));

    #Config function, used to display the config shortcut gui and assign data to shortcut files.
    def OpenShortcut_Config(self,Shortcut):
        #Global variable declarations.
        global ConfigStat; print("----------");
        global Shortcut01_Type; global Shortcut01_Path; global Shortcut01_KeyB;
        global Shortcut02_Type; global Shortcut02_Path; global Shortcut02_KeyB;
        global Shortcut03_Type; global Shortcut03_Path; global Shortcut03_KeyB;
        global Shortcut04_Type; global Shortcut04_Path; global Shortcut04_KeyB;
        global Shortcut05_Type; global Shortcut05_Path; global Shortcut05_KeyB;
        global Shortcut06_Type; global Shortcut06_Path; global Shortcut06_KeyB;
        #If ConfigStat is 0 config gui is closed so lets open it.
        if(ConfigStat==0):
            print("DEBUG: Displaying config panel.");
            #Reverse the ConfigStat value.
            ConfigStat=1;
            #Assign values used for text based on input value.
            if  (Shortcut=="1"): Type=Shortcut01_Type; Path=Shortcut01_Path; KeyB=str(ReverseKey(Shortcut01_KeyB));
            elif(Shortcut=="2"): Type=Shortcut02_Type; Path=Shortcut02_Path; KeyB=str(ReverseKey(Shortcut02_KeyB));
            elif(Shortcut=="3"): Type=Shortcut03_Type; Path=Shortcut03_Path; KeyB=str(ReverseKey(Shortcut03_KeyB));
            elif(Shortcut=="4"): Type=Shortcut04_Type; Path=Shortcut04_Path; KeyB=str(ReverseKey(Shortcut04_KeyB));
            elif(Shortcut=="5"): Type=Shortcut05_Type; Path=Shortcut05_Path; KeyB=str(ReverseKey(Shortcut05_KeyB));
            elif(Shortcut=="6"): Type=Shortcut06_Type; Path=Shortcut06_Path; KeyB=str(ReverseKey(Shortcut06_KeyB));
            #Add z.
            Shortcut=Shortcut+"z";
            #Config GUI size.
            root.minsize(width=399,height=232); root.maxsize(width=399,height=232);
            #Draw our labels.
            self.Config_Line =tkinter.Label(relief=tkinter.GROOVE);
            self.Config_Title=tkinter.Label(relief=tkinter.GROOVE,fg="#333d53",text="Configuring Shortcut #"+Shortcut[:1]);
            self.Config_Line.place (w=841,h=2,x=0,y=112);
            self.Config_Title.place(w=394,h=22,x=3,y=116);
            #Add the type selection dropdown menu.
            self.Type=tkinter.StringVar(); self.Type.set(Type);
            self.Config_Type=tkinter.OptionMenu(root,self.Type,"Type: Start Program","Type: Open File","Type: Open Folder","Type: Open Website");
            self.Config_Type.config(relief=tkinter.GROOVE,fg="#333d53",indicatoron=0);
            self.Config_Type.place(w=398,h=26,x=1,y=138);
            #Add the entry fields and the done button.
            self.Config_Path=tkinter.Entry (relief=tkinter.GROOVE,fg="#333d53",border=2);
            self.Config_KeyB=tkinter.Entry (relief=tkinter.GROOVE,fg="#333d53",border=2);
            self.Config_Done=tkinter.Button(relief=tkinter.GROOVE,fg="#333d53",font=("Helvetica 8"),text="Done",command=lambda:self.OpenShortcut_Config(Shortcut));
            self.Config_Path.place(w=394,h=24,x=3,y=160); self.Config_Path.insert(tkinter.END,Path);
            self.Config_KeyB.place(w=394,h=24,x=3,y=182); self.Config_KeyB.insert(tkinter.END,KeyB);
            self.Config_Done.place(w=394,h=22,x=3,y=208);
        #If ConfigStat is 1 we know config is open so lets close it.
        elif(ConfigStat==1):
            print("DEBUG: Hiding config panel.");
            #Reverse the ConfigStat value.
            ConfigStat=0;
            #Config GUI size.
            root.minsize(width=399,height=112); root.maxsize(width=399,height=112);
            #Redundancy measure to avoid having to set button states(cx_Freeze'd files tend to not like that).
            if(Shortcut=="1" or Shortcut=="2" or Shortcut=="3" or Shortcut=="4" or Shortcut=="5" or Shortcut=="6"):
                print("DEBUG: Done was not pressed, blocking action");
            else:
                #Remove z.
                Shortcut=Shortcut[:1];
                #Fetch the data the user added to the fields.
                Type=self.Type.get(); Path=self.Config_Path.get(); KeyB=self.Config_KeyB.get();
                #Determine what image to assign.
                if  (Type=="Type: Open Folder"):   ShortcutIco=self.Type_Folder;
                elif(Type=="Type: Open File"):     ShortcutIco=self.Type_File;
                elif(Type=="Type: Start Program"): ShortcutIco=self.Type_Software;
                elif(Type=="Type: Open Website"):  ShortcutIco=self.Type_Website;
                elif(Type=="Type: None"):          ShortcutIco=self.Type_None;
                #Write to Shortcut data file.
                f=open("Data/Shortcut0"+Shortcut,"w"); f.write(str(Type+'\n')); f.write(str(Path+'\n')); f.write(str(ResolveKey(KeyB))); f.close();
                #Conduct Shortcut number specific operations.
                if  (Shortcut=="1"): Shortcut01_Type=Type; Shortcut01_Path=Path; Shortcut01_KeyB=ResolveKey(KeyB); self.Shortcut01_Txt.config(text="Key: "+KeyB); self.Shortcut01_Ico.config(i=ShortcutIco);
                elif(Shortcut=="2"): Shortcut02_Type=Type; Shortcut02_Path=Path; Shortcut02_KeyB=ResolveKey(KeyB); self.Shortcut02_Txt.config(text="Key: "+KeyB); self.Shortcut02_Ico.config(i=ShortcutIco);
                elif(Shortcut=="3"): Shortcut03_Type=Type; Shortcut03_Path=Path; Shortcut03_KeyB=ResolveKey(KeyB); self.Shortcut03_Txt.config(text="Key: "+KeyB); self.Shortcut03_Ico.config(i=ShortcutIco);
                elif(Shortcut=="4"): Shortcut04_Type=Type; Shortcut04_Path=Path; Shortcut04_KeyB=ResolveKey(KeyB); self.Shortcut04_Txt.config(text="Key: "+KeyB); self.Shortcut04_Ico.config(i=ShortcutIco);
                elif(Shortcut=="5"): Shortcut05_Type=Type; Shortcut05_Path=Path; Shortcut05_KeyB=ResolveKey(KeyB); self.Shortcut05_Txt.config(text="Key: "+KeyB); self.Shortcut05_Ico.config(i=ShortcutIco);
                elif(Shortcut=="6"): Shortcut06_Type=Type; Shortcut06_Path=Path; Shortcut06_KeyB=ResolveKey(KeyB); self.Shortcut06_Txt.config(text="Key: "+KeyB); self.Shortcut06_Ico.config(i=ShortcutIco);

    #GUI Build function, function that builds the initial gui seen when starting the program.
    def OpenShortcut_BuildGUI(self):
        print("DEBUG: Building GUI.");
        #X=width | Y=height <<< Friendly reminder of the up & down and all around variety.
        #Load Shortcut icon images for later use.
        self.Type_None    =ImageTk.PhotoImage(Image.open("Images/None.png"));
        self.Type_Folder  =ImageTk.PhotoImage(Image.open("Images/Folder.png"));
        self.Type_File    =ImageTk.PhotoImage(Image.open("Images/File.png"));
        self.Type_Software=ImageTk.PhotoImage(Image.open("Images/Software.png"));
        self.Type_Website =ImageTk.PhotoImage(Image.open("Images/Website.png"));
        #Build the GUI elements to the screen.
        #Topbar line.
        self.TopLine=tkinter.Label(relief=tkinter.GROOVE);
        self.TopLine.place(w=841,h=2,x=0,y=0);
        #Shortcut01.
        self.Shortcut01_Ico=tkinter.Label (relief=tkinter.GROOVE);
        self.Shortcut01_Txt=tkinter.Label (relief=tkinter.GROOVE,fg="#333d53",font=("Helvetica 8"));
        self.Shortcut01_Btn=tkinter.Button(relief=tkinter.GROOVE,fg="#333d53",font=("Helvetica 8"),text="Config",command=lambda:self.OpenShortcut_Config("1"));
        self.Shortcut01_Ico.place(w=64,h=64,x=3,y=4);
        self.Shortcut01_Txt.place(w=64,h=19,x=3,y=70);
        self.Shortcut01_Btn.place(w=64,h=19,x=3,y=91);
        #Shortcut02.
        self.Shortcut02_Ico=tkinter.Label (relief=tkinter.GROOVE);
        self.Shortcut02_Txt=tkinter.Label (relief=tkinter.GROOVE,fg="#333d53",font=("Helvetica 8"));
        self.Shortcut02_Btn=tkinter.Button(relief=tkinter.GROOVE,fg="#333d53",font=("Helvetica 8"),text="Config",command=lambda:self.OpenShortcut_Config("2"));
        self.Shortcut02_Ico.place(w=64,h=64,x=69,y=4);
        self.Shortcut02_Txt.place(w=64,h=19,x=69,y=70);
        self.Shortcut02_Btn.place(w=64,h=19,x=69,y=91);
        #Shortcut03.
        self.Shortcut03_Ico=tkinter.Label (relief=tkinter.GROOVE);
        self.Shortcut03_Txt=tkinter.Label (relief=tkinter.GROOVE,fg="#333d53",font=("Helvetica 8"));
        self.Shortcut03_Btn=tkinter.Button(relief=tkinter.GROOVE,fg="#333d53",font=("Helvetica 8"),text="Config",command=lambda:self.OpenShortcut_Config("3"));
        self.Shortcut03_Ico.place(w=64,h=64,x=135,y=4);
        self.Shortcut03_Txt.place(w=64,h=19,x=135,y=70);
        self.Shortcut03_Btn.place(w=64,h=19,x=135,y=91);
        #Shortcut04.
        self.Shortcut04_Ico=tkinter.Label (relief=tkinter.GROOVE);
        self.Shortcut04_Txt=tkinter.Label (relief=tkinter.GROOVE,fg="#333d53",font=("Helvetica 8"));
        self.Shortcut04_Btn=tkinter.Button(relief=tkinter.GROOVE,fg="#333d53",font=("Helvetica 8"),text="Config",command=lambda:self.OpenShortcut_Config("4"));
        self.Shortcut04_Ico.place(w=64,h=64,x=201,y=4);
        self.Shortcut04_Txt.place(w=64,h=19,x=201,y=70);
        self.Shortcut04_Btn.place(w=64,h=19,x=201,y=91);
        #Shortcut05.
        self.Shortcut05_Ico=tkinter.Label (relief=tkinter.GROOVE);
        self.Shortcut05_Txt=tkinter.Label (relief=tkinter.GROOVE,fg="#333d53",font=("Helvetica 8"));
        self.Shortcut05_Btn=tkinter.Button(relief=tkinter.GROOVE,fg="#333d53",font=("Helvetica 8"),text="Config",command=lambda:self.OpenShortcut_Config("5"));
        self.Shortcut05_Ico.place(w=64,h=64,x=267,y=4);
        self.Shortcut05_Txt.place(w=64,h=19,x=267,y=70);
        self.Shortcut05_Btn.place(w=64,h=19,x=267,y=91);
        #Shortcut06.
        self.Shortcut06_Ico=tkinter.Label (relief=tkinter.GROOVE);
        self.Shortcut06_Txt=tkinter.Label (relief=tkinter.GROOVE,fg="#333d53",font=("Helvetica 8"));
        self.Shortcut06_Btn=tkinter.Button(relief=tkinter.GROOVE,fg="#333d53",font=("Helvetica 8"),text="Config",command=lambda:self.OpenShortcut_Config("6"));
        self.Shortcut06_Ico.place(w=64,h=64,x=333,y=4);
        self.Shortcut06_Txt.place(w=64,h=19,x=333,y=70);
        self.Shortcut06_Btn.place(w=64,h=19,x=333,y=91);

#Assign tkinter to root.
root=tkinter.Tk();
#Set application title.
root.title("OpenShortcut 1.0.0");
#Set the .ico bitmap used by windows.
root.iconbitmap('Images\OpenShortcut.ico');
#Configure the background color of our window.
root.configure(background="#e3e3e3");
#Assign our tkinter class to the application handle.
Application=OpenShortcut_GUI(master=root);
#Start the mainloop.
Application.mainloop();
