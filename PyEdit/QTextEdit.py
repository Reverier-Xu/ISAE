#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtCore import (QFile, QFileInfo, QPoint, QRect, QSettings, QSize, Qt, QTextStream, QDir, QTranslator, QLocale, QLibraryInfo, QTime, QTimer)
from PyQt5.QtGui import QIcon, QKeySequence, QTextCursor, QClipboard
from PyQt5.QtWidgets import (QAction, QApplication, QFileDialog, QMainWindow, QMessageBox, QTextEdit, QPushButton, QLineEdit, QMenu, QInputDialog, QLCDNumber)
from PyQt5 import QtPrintSupport
import sys

class DigitalClock(QLCDNumber):

    def __init__(self, parent=None):
        super(DigitalClock, self).__init__(parent)
        self.setSegmentStyle(QLCDNumber.Flat)
        self.setDigitCount(8)
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        self.showTime()
        self.resize(120, 40)

    def showTime(self):
        time = QTime.currentTime()
        text = time.toString('hh:mm:ss')
        if (time.second() % 2) == 0:
            text = text[:2] + ' ' + text[3:5] + ' ' + text[6:]
        self.display(text)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        translator = QTranslator()
        print(QLocale.system().name())
        translator.load('qt_' + QLocale.system().name(), QLibraryInfo.location(QLibraryInfo.TranslationsPath))
        app.installTranslator(translator)

        self.setStyleSheet(myStyleSheet(self))
        self.MaxRecentFiles = 5
        self.windowList = []
        self.recentFileActs = []
        self.curFile = ''
        self.setAcceptDrops(True)
        self. settings = QSettings("QTextEdit", "QTextEdit")
        self.myeditor = QTextEdit()
        assert(self.locale().language() == QLocale.German)
        self.myeditor.setAcceptRichText(False)
        self.myeditor.setUndoRedoEnabled(True)
        self.myeditor.setStyleSheet(myStyleSheet(self))
        self.myeditor.setContextMenuPolicy(Qt.CustomContextMenu)
        self.myeditor.customContextMenuRequested.connect(self.contextMenuRequested)

        self.createActions()
        self.createToolBars()
        self.createMenus()
        self.createStatusBar()

        self.setWindowIcon(QIcon.fromTheme("gnome-documents"))

        self.readSettings()
        self.myeditor.document().contentsChanged.connect(self.documentWasModified)
        self.setCurrentFile('')
        self.setCentralWidget(self.myeditor)
        self.myeditor.setFocus()

    def closeEvent(self, event):
        if self.maybeSave():
            self.writeSettings()
            event.accept()
        else:
            event.ignore()

    def newFile(self):
        if self.maybeSave():
            self.myeditor.clear()
            self.setCurrentFile('')

    def open(self):
        if self.maybeSave():
            fileName, _ = QFileDialog.getOpenFileName(self, "Datei öffnen", QDir.homePath() + "/Dokumente", "Text Dateien (*.txt *.csv *.sh *.py) ;; alle Dateien (*.*)")
            if fileName:
                self.loadFile(fileName)
            else:
                self.statusBar().showMessage("abgebrochen", 3000)

    def save(self):
        if not self.myeditor.toPlainText() == "":
            if self.myeditor.document().isModified():
                if self.curFile:
                    return self.saveFile(self.curFile)
                    self.setCurrentFile(fileName)
                else:
                    return self.saveAs()
            else:
                self.statusBar().showMessage("Datei '" + self.curFile + "' bereits gespeichert", 3000)
        else:
            self.statusBar().showMessage("kein Text")

    def saveAs(self):
        if not self.myeditor.toPlainText() == "":
            if self.curFile:
                fileName, _ = QFileDialog.getSaveFileName(self, "Speichern als...", self.curFile, "Text Dateien (*.txt)")
            else:
                fileName, _ = QFileDialog.getSaveFileName(self, "Speichern als...", QDir.homePath() + "/Dokumente/Unbenannt.txt", "Text Dateien (*.txt)" )
            if fileName:
                return self.saveFile(fileName)

            return False
        else:
            self.statusBar().showMessage("kein Text")

    def contextMenuRequested(self, point):
        cmenu = QMenu()
        cmenu = self.myeditor.createStandardContextMenu()
        if not self.myeditor.textCursor().selectedText() == "":
            cmenu.addSeparator()
            cmenu.addAction(QIcon.fromTheme("edit-find-and-replace"),"alle Übereinstimmungen ersetzen", self.replaceThis)
        cmenu.exec_(self.myeditor.mapToGlobal(point))    

    def replaceThis(self):
        if not self.myeditor.textCursor().selectedText() == "":
            rtext = self.myeditor.textCursor().selectedText()
            dlg = QInputDialog(self, Qt.Dialog)
            dlg.setOkButtonText("Replace")
            text = dlg.getText(self, "Ersetzen","ersetze '" + rtext + "' durch:", QLineEdit.Normal, "")
            oldtext = self.myeditor.document().toPlainText()
            if not (text[0] == ""):
                newtext = oldtext.replace(rtext, text[0])
                self.myeditor.setPlainText(newtext)
                self.myeditor.document().setModified(True)

    def about(self):
        link = "<p><a title='Axel Schneider' href='http://goodoldsongs.jimdo.com' target='_blank'>Axel Schneider</a></p>"
        title = "über QTextEdit"
        message =  ("<span style='text-shadow: #2e3436 2px 2px 2px; color: #6169e1; font-size: 24pt;font-weight: bold;'><strong>QTextEdit 1.2</strong></span></p><br><br>created by<h2 >" + link + "</h2> with PyQt5" 
                    "<br><br>Copyright © 2018 The Qt Company Ltd and other contributors." 
                    "<br>Qt and the Qt logo are trademarks of The Qt Company Ltd.")
        msg = QMessageBox(QMessageBox.Information, title, message, QMessageBox.NoButton, self, Qt.Dialog|Qt.NoDropShadowWindowHint).show()

    def documentWasModified(self):
        self.setWindowModified(self.myeditor.document().isModified())

    def createActions(self):
        self.newAct = QAction(QIcon.fromTheme('document-new'), "&Neu", self,
                shortcut=QKeySequence.New, statusTip="neue Datei erstellen",
                triggered=self.newFile)

        self.openAct = QAction(QIcon.fromTheme('document-open'), "Öffnen.",
                self, shortcut=QKeySequence.Open,
                statusTip="Datei öffnen", triggered=self.open)

        self.saveAct = QAction(QIcon.fromTheme('document-save'), "Speichern", self,
                shortcut=QKeySequence.Save,
                statusTip="Dokument speichern", triggered=self.save)

        self.saveAsAct = QAction(QIcon.fromTheme('document-save-as'),"Speichern als...", self,
                shortcut=QKeySequence.SaveAs,
                statusTip="Dokument unter neuem Namen speichern",
                triggered=self.saveAs)

        self.exitAct = QAction(QIcon.fromTheme('application-exit'),"Beenden", self, shortcut="Ctrl+Q",
                statusTip="Programm beenden", triggered=self.close)

        self.cutAct = QAction(QIcon.fromTheme('edit-cut'), "Ausschneiden", self,
                shortcut=QKeySequence.Cut,
                statusTip="Ausschneiden",
                triggered=self.myeditor.cut)

        self.copyAct = QAction(QIcon.fromTheme('edit-copy'), "Kopieren", self,
                shortcut=QKeySequence.Copy,
                statusTip="Kopieren",
                triggered=self.myeditor.copy)

        self.pasteAct = QAction(QIcon.fromTheme('edit-paste'), "Einfügen",
                self, shortcut=QKeySequence.Paste,
                statusTip="Einfügen",
                triggered=self.myeditor.paste)

        self.undoAct = QAction(QIcon.fromTheme('edit-undo'), "Rückgängig",
                self, shortcut=QKeySequence.Undo,
                statusTip="Rückgängig",
                triggered=self.myeditor.undo)

        self.redoAct = QAction(QIcon.fromTheme('edit-redo'), "Wiederholen",
                self, shortcut=QKeySequence.Redo,
                statusTip="Wiederholen",
                triggered=self.myeditor.redo)

        self.aboutAct = QAction(QIcon.fromTheme('help-about'),"Info", self,
                statusTip="über QTextEdit",
                triggered=self.about)

        self.aboutQtAct = QAction(QIcon.fromTheme('help-about'),"über Qt", self,
                statusTip="über Qt",
                triggered=QApplication.instance().aboutQt)

        self.repAllAct = QPushButton("alles ersetzen") 
        self.repAllAct.setIcon(QIcon.fromTheme("edit-find-and-replace"))
        self.repAllAct.setStatusTip("alles ersetzen")
        self.repAllAct.clicked.connect(self.replaceAll)

        self.cutAct.setEnabled(False)
        self.copyAct.setEnabled(False)
        self.myeditor.copyAvailable.connect(self.cutAct.setEnabled)
        self.myeditor.copyAvailable.connect(self.copyAct.setEnabled)
        self.undoAct.setEnabled(False)
        self.redoAct.setEnabled(False)
        self.myeditor.undoAvailable.connect(self.undoAct.setEnabled)
        self.myeditor.redoAvailable.connect(self.redoAct.setEnabled)

        ### print preview
        self.printPreviewAct = QAction("Druckvorschau", self, shortcut=QKeySequence.Print,statusTip="Druckvorschau", triggered=self.handlePrintPreview)
        self.printPreviewAct.setIcon(QIcon.fromTheme("document-print-preview"))
        ### print
        self.printAct = QAction("Drucken", self, shortcut=QKeySequence.Print,statusTip="Dokument drucken", triggered=self.handlePrint)
        self.printAct.setIcon(QIcon.fromTheme("document-print"))

        for i in range(self.MaxRecentFiles):
            self.recentFileActs.append(
                   QAction(self, visible=False,
                            triggered=self.openRecentFile))

    def findText(self):
        word = self.findfield.text()
        if self.myeditor.find(word):
            self.statusBar().showMessage("'" + word + "' gefunden", 2000)
        else:
            self.myeditor.moveCursor(QTextCursor.Start)            
            if self.myeditor.find(word):
                return
            else:
                 self.statusBar().showMessage("nichts gefunden", 3000)

    def replaceAll(self):
        oldtext = self.findfield.text()
        newtext = self.replacefield.text()
        if not oldtext == "":
            h = self.myeditor.toHtml().replace(oldtext, newtext)
            self.myeditor.setText(h)
            self.setModified(True)
            self.statusBar().showMessage("alles ersetzt", 3000)
        else:
            self.statusBar().showMessage("nichts zu ersetzen", 3000)
        
    def replaceOne(self):
        oldtext = self.findfield.text()
        newtext = self.replacefield.text()
        if not oldtext == "":
            h = self.myeditor.toHtml().replace(oldtext, newtext, 1)
            self.myeditor.setText(h)
            self.setModified(True)
            self.statusBar().showMessage("1 ersetzt", 3000)
        else:
            self.statusBar().showMessage("nichts zu ersetzen", 3000)

    def openRecentFile(self):
        action = self.sender()
        if action:
            if (self.maybeSave()):
                self.loadFile(action.data())

    def createMenus(self):
        self.fileMenu = self.menuBar().addMenu("&Datei")
        self.separatorAct = self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.newAct)
        self.fileMenu.addAction(self.openAct)
        self.fileMenu.addAction(self.saveAct)
        self.fileMenu.addAction(self.saveAsAct)
        self.fileMenu.addSeparator()
        for i in range(self.MaxRecentFiles):
            self.fileMenu.addAction(self.recentFileActs[i])
        self.updateRecentFileActions()
        self.fileMenu.addSeparator()
        self.clearRecentAct = QAction("Liste löschen", self, triggered=self.clearRecentFiles)
        self.clearRecentAct.setIcon(QIcon.fromTheme("edit-clear"))
        self.fileMenu.addAction(self.clearRecentAct)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.exitAct)

        self.editMenu = self.menuBar().addMenu("&Bearbeiten")
        self.editMenu.addAction(self.undoAct)
        self.editMenu.addAction(self.redoAct)
        self.editMenu.addSeparator();
        self.editMenu.addAction(self.cutAct)
        self.editMenu.addAction(self.copyAct)
        self.editMenu.addAction(self.pasteAct)

        self.menuBar().addSeparator()

        self.helpMenu = self.menuBar().addMenu("&Hilfe")
        self.helpMenu.addAction(self.aboutAct)

    def createToolBars(self):
        self.fileToolBar = self.addToolBar("Datei")
        self.fileToolBar.setIconSize(QSize(16, 16))
        self.fileToolBar.addAction(self.newAct)
        self.fileToolBar.addAction(self.openAct)
        self.fileToolBar.addAction(self.saveAct)
        self.fileToolBar.addAction(self.saveAsAct)
        self.fileToolBar.addSeparator()
        self.fileToolBar.addAction(self.printPreviewAct)
        self.fileToolBar.addAction(self.printAct)
        self.fileToolBar.setStyleSheet("QToolBar { border: 0px }")
        self.fileToolBar.setMovable(False)
        self.setContextMenuPolicy(Qt.NoContextMenu)

        self.editToolBar = self.addToolBar("Bearbeiten")
        self.editToolBar.setIconSize(QSize(16, 16))
        self.editToolBar.addAction(self.undoAct)
        self.editToolBar.addAction(self.redoAct)
        self.editToolBar.addSeparator()
        self.editToolBar.addAction(self.cutAct)
        self.editToolBar.addAction(self.copyAct)
        self.editToolBar.addAction(self.pasteAct)
        self.editToolBar.setMovable(False)
        self.editToolBar.setStyleSheet("QToolBar { border: 0px }")

        ### find / replace toolbar
        self.addToolBarBreak()
        self.findToolBar = self.addToolBar("Suchen")
        self.findToolBar.setIconSize(QSize(16, 16))
        self.findfield = QLineEdit()
        self.findfield.addAction(QIcon.fromTheme("edit-find"), 0)
        self.findfield.setClearButtonEnabled(True)
        self.findfield.setFixedWidth(200)
        self.findfield.setPlaceholderText("suchen")
        self.findfield.setStatusTip("drücke RETURN zum suchen")
        self.findfield.setText("")
        self.findfield.returnPressed.connect(self.findText)
        self.findToolBar.addWidget(self.findfield)
        self.replacefield = QLineEdit()
        self.replacefield.addAction(QIcon.fromTheme("edit-find-replace"), 0)
        self.replacefield.setClearButtonEnabled(True)
        self.replacefield.setFixedWidth(200)
        self.replacefield.setPlaceholderText("ersetzen durch")
        self.replacefield.setStatusTip("drücke RETURN um das erste zu ersetzen")
        self.replacefield.returnPressed.connect(self.replaceOne)
        self.findToolBar.addSeparator() 
        self.findToolBar.addWidget(self.replacefield)
        self.findToolBar.addSeparator()
        self.findToolBar.addWidget(self.repAllAct)
        self.findToolBar.setMovable(False)
        self.findToolBar.setStyleSheet("QToolBar { border: 0px }")

    def createStatusBar(self):
        self.statusBar().setStyleSheet(myStyleSheet(self))
        self.statusBar().showMessage("Willkommen")
        self.DigitalClock = DigitalClock()
        self.DigitalClock.setStyleSheet("QLCDNumber {padding: 2px, 2px 2px 2px; border: 0px solid #2e3436; color: #3465a4; background-color: transparent }")
        self.statusBar().addPermanentWidget(self.DigitalClock)

    def readSettings(self):
        pos = self.settings.value("pos", QPoint(200, 200))
        size = self.settings.value("size", QSize(400, 400))
        self.resize(size)
        self.move(pos)

    def writeSettings(self):
        self.settings.setValue("pos", self.pos())
        self.settings.setValue("size", self.size())

    def maybeSave(self):
        if self.myeditor.document().isModified():
            ret = QMessageBox.warning(self, "QTextEdit Meldung",
                    "Das Dokument wurde geändert.\nSollen die Änderungen gespeichert werden?",
                    QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel, defaultButton = QMessageBox.Save)
            if ret == QMessageBox.Save:
                return self.save()
            if ret == QMessageBox.Cancel:
                return False
        return True

    def loadFile(self, fileName):
        file = QFile(fileName)
        if not file.open(QFile.ReadOnly | QFile.Text):
            QMessageBox.warning(self, "Meldung",
                    "Cannot read file %s:\n%s." % (fileName, file.errorString()))
            return

        infile = QTextStream(file)
        QApplication.setOverrideCursor(Qt.WaitCursor)
        self.myeditor.setPlainText(infile.readAll())
        QApplication.restoreOverrideCursor()

        self.setCurrentFile(fileName)
        self.statusBar().showMessage("Datei '" +  fileName + "' geladen", 3000)

    def saveFile(self, fileName):
        file = QFile(fileName)
        if not file.open(QFile.WriteOnly | QFile.Text):
            QMessageBox.warning(self, "Message",
                    "Cannot write file %s:\n%s." % (fileName, file.errorString()))
            return False

        outfile = QTextStream(file)
        QApplication.setOverrideCursor(Qt.WaitCursor)
        outfile << self.myeditor.toPlainText()
        QApplication.restoreOverrideCursor()

        self.setCurrentFile(fileName);
        self.statusBar().showMessage("Datei '" +  fileName + "' gespeichert", 3000)
        return True

    def setCurrentFile(self, fileName):
        self.curFile = fileName
        self.myeditor.document().setModified(False)
        self.setWindowModified(False)

        if self.curFile:
            self.setWindowTitle(self.strippedName(self.curFile) + "[*]")
        else:
            self.setWindowTitle('Unbenannt.txt' + "[*]")

        files = self.settings.value('recentFileList', [])
        if not files == "":
            try:
                files.remove(fileName)
            except ValueError:
                pass
    
            if fileName:
                files.insert(0, fileName)
                del files[self.MaxRecentFiles:]
    
                self.settings.setValue('recentFileList', files)
                self.updateRecentFileActions()

    def updateRecentFileActions(self):
        mytext = ""
        files = self.settings.value('recentFileList', [])
        numRecentFiles = min(len(files), self.MaxRecentFiles)
#        if not files == "":
        for i in range(numRecentFiles):
            text = "&%d %s" % (i + 1, self.strippedName(files[i]))
            self.recentFileActs[i].setText(text)
            self.recentFileActs[i].setData(files[i])
            self.recentFileActs[i].setVisible(True)
            self.recentFileActs[i].setIcon(QIcon.fromTheme("text-x-generic"))
        
        for j in range(numRecentFiles, self.MaxRecentFiles):
            self.recentFileActs[j].setVisible(False)

        self.separatorAct.setVisible((numRecentFiles > 0))
            
    def clearRecentFiles(self, fileName):
        self.settings.clear()
        self.updateRecentFileActions()

    def strippedName(self, fullFileName):
        return QFileInfo(fullFileName).fileName()

    def msgbox(self, message):
        QMessageBox.warning(self, "Message", message)

    def handlePrint(self):
        if self.myeditor.toPlainText() == "":
            self.statusBar().showMessage("kein Text zum Drucken")
            self.msgbox("kein Text zum Drucken")
        else:
            dialog = QtPrintSupport.QPrintDialog()
            if dialog.exec_() == QDialog.Accepted:
                self.handlePaintRequest(dialog.printer())
                self.statusBar().showMessage("Dokument gedruckt")
            
    def handlePrintPreview(self):
        if self.myeditor.toPlainText() == "":
            self.statusBar().showMessage("kein Text für Vorschau")
            self.msgbox("kein Text für Vorschau")
        else:
            dialog = QtPrintSupport.QPrintPreviewDialog()
            dialog.setGeometry(10, 0, self.width() - 60, self.height() - 60)
            dialog.paintRequested.connect(self.handlePaintRequest)
            dialog.exec_()
            self.statusBar().showMessage("Vorschau geschlossen")

    def handlePaintRequest(self, printer):
        printer.setDocName(self.curFile)
        document = self.myeditor.document()
        document.print_(printer)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        f = str(event.mimeData().urls()[0].toLocalFile())
        self.loadFile(f)

def myStyleSheet(self):
    return """
QTextEdit
{
background: #eeeeec;
color: #202020;
}
QStatusBar
{
     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                 stop: 0 #E1E1E1, stop: 0.4 #e5e5e5,
                                 stop: 0.5 #e9e9e9, stop: 1.0 #d2d2d2);
font-size: 8pt;
color: #555753;
}
QMenuBar
{
background: transparent;
border: 0px;
}
QToolBar
{
background: transparent;
border: 0px;
}
QMainWindow
{
     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,
                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);
}
QLineEdit
{
     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                 stop: 0 #E1E1E1, stop: 0.4 #e5e5e5,
                                 stop: 0.5 #e9e9e9, stop: 1.0 #d2d2d2);
}
QPushButton
{
background: #D8D8D8;
}
QLCDNumber
{
color: #204a87;
}
    """       

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
#    assert(mainWin.locale().language() == QLocale.German)
    mainWin.show()
    if len(sys.argv) > 1:
        print(sys.argv[1])
        mainWin.loadFile(sys.argv[1])
    sys.exit(app.exec_())
