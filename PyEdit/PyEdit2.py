#!/usr/bin/python3
# -- coding: utf-8 --
import sys

from PyQt5.QtWidgets import QPlainTextEdit, QWidget, QVBoxLayout, QApplication, QFileDialog, QMessageBox, QHBoxLayout, \
    QTextEdit, QToolBar, QComboBox, QAction, QLineEdit, QDialog, \
    QToolButton, QMenu, QMainWindow, QInputDialog, QColorDialog, QStatusBar, QSystemTrayIcon, QSplitter
from PyQt5.QtGui import QIcon, QPainter, QTextFormat, QColor, QTextCursor, QKeySequence, QClipboard, QTextDocument, \
    QTextCharFormat, QFont
from PyQt5.QtCore import Qt, QVariant, QRect, QDir, QFile, QDirIterator, QFileInfo, QTextStream, QSettings, QProcess, \
    QPoint, QByteArray
from PyQt5 import QtPrintSupport, QtCore
import PyEdit.syntax_py as syntax_py
from os import path, pardir, system as shell
from sys import argv
import base64

from ui_Widgets import uni_Widget

lineBarColor = QColor("#303030")
lineHighlightColor = QColor("#282828")
tab = chr(9)
eof = "\n"


class NumberBar(QWidget):
    def __init__(self, parent=None):
        super(NumberBar, self).__init__(parent)
        self.editor = parent
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.editor.blockCountChanged.connect(self.update_width)
        self.editor.updateRequest.connect(self.update_on_scroll)
        self.update_width('1')

    def update_on_scroll(self, rect, scroll):
        if self.isVisible():
            if scroll:
                self.scroll(0, scroll)
            else:
                self.update()

    def update_width(self, string):
        width = (len(str(string)) + 1) * 14
        if self.width() != width:
            self.setFixedWidth(width)

    def paintEvent(self, event):
        if self.isVisible():
            block = self.editor.firstVisibleBlock()
            height = 24
            number = block.blockNumber()
            painter = QPainter(self)
            painter.fillRect(event.rect(), lineBarColor)
            painter.drawRect(-1, -1, event.rect().width() +
                             1, event.rect().height()+1)
            font = QFont()
            font.setFamily('文泉驿等宽微米黑')
            font.setPixelSize(24)

            current_block = self.editor.textCursor().block().blockNumber() + 1

            condition = True
            while block.isValid() and condition:
                block_geometry = self.editor.blockBoundingGeometry(block)
                offset = self.editor.contentOffset()
                block_top = block_geometry.translated(offset).top()
                number += 1

                rect = QRect(0, block_top, self.width() - 5, height)

                if number == current_block:
                    font.setBold(True)
                else:
                    font.setBold(False)

                painter.setFont(font)
                painter.drawText(rect, Qt.AlignRight, '%i' % number)

                if block_top > event.rect().bottom():
                    condition = False

                block = block.next()

            painter.end()


class EditorPanel(QMainWindow):
    def __init__(self, parent=None):
        super(EditorPanel, self).__init__(parent)
        self.appfolder = path.abspath("./") + "/PyEdit"
        #        shell("cd " + self.appfolder)
        self.statusBar().showMessage(self.appfolder)
        self.MaxRecentFiles = 10
        self.windowList = []
        self.recentFileActs = []
        self.settings = QSettings("PyEdit", "PyEdit")
        self.dirpath = QDir.homePath() + "/Documents/python_files/"
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setWindowIcon(QIcon(self.appfolder + "icons/python2.png"))
        # Editor Widget ...
        QIcon.setThemeName('Faenza-Dark')
        self.editor = QPlainTextEdit()
        font = QFont()
        font.setFamily('文泉驿等宽微米黑')
        font.setPixelSize(24)
        self.editor.setFont(font)
        self.editor.setStyleSheet(stylesheet2(self))
        self.editor.setTabStopWidth(20)
        self.extra_selections = []
        self.mainText = "#!/usr/bin/python3\n# -*- coding: utf-8 -*-\n"
        self.fname = ""
        self.filename = ""
        self.mypython = "2"
        self.mylabel = QTextEdit()
        font.setPixelSize(16)
        self.mylabel.setFont(font)
        self.mylabel.setTextInteractionFlags(Qt.TextSelectableByMouse)
        # Line Numbers ...
        self.numbers = NumberBar(self.editor)
        self.createActions()
        # Syntax Highlighter ...
        self.highlighter = syntax_py.Highlighter(self.editor.document())
        # Laying out...
        layoutH = QHBoxLayout()
        layoutH.setSpacing(1.5)
        layoutH.addWidget(self.numbers)
        layoutH.addWidget(self.editor)
        # statusbar
        self.statusBar()
        self.statusBar().setStyleSheet(stylesheet2(self))
        #        self.statusBar().showMessage('Welcome')
        # begin toolbar
        tb = QToolBar(self)
        tb.setMovable(True)
        tb.setAllowedAreas(Qt.AllToolBarAreas)
        tb.setFloatable(True)
        tb.setWindowTitle("File Toolbar")
        # file buttons
        self.newAct = QAction("&New", self, shortcut=QKeySequence.New,
                              toolTip="new file", triggered=self.newFile)
        self.newAct.setIcon(QIcon(self.appfolder + "/icons/new24"))
        tb.addAction(self.newAct)

        self.openAct = QAction("&Open", self, shortcut=QKeySequence.Open,
                               toolTip="open file", triggered=self.openFile)
        self.openAct.setIcon(QIcon(self.appfolder + "/icons/open24"))
        tb.addAction(self.openAct)

        self.saveAct = QAction("&Save", self, shortcut=QKeySequence.Save,
                               toolTip="save file", triggered=self.fileSave)
        self.saveAct.setIcon(QIcon(self.appfolder + "/icons/floppy24"))
        tb.addAction(self.saveAct)

        self.saveAsAct = QAction("&Save as ...", self, shortcut=QKeySequence.SaveAs,
                                 toolTip="save file as ...", triggered=self.fileSaveAs)
        self.saveAsAct.setIcon(QIcon(self.appfolder + "/icons/floppy25"))
        tb.addAction(self.saveAsAct)

        self.jumpToAct = QAction("go to Definition", self, shortcut="F12",
                                 toolTip="go to def", triggered=self.gotoBookmarkFromMenu)
        self.jumpToAct.setIcon(QIcon.fromTheme("go-next"))

        # comment buttons
        tb.addSeparator()
        self.commentAct = QAction("#comment Line", self, shortcut="F2",
                                  toolTip="comment Line (F2)", triggered=self.commentLine)
        self.commentAct.setIcon(QIcon(self.appfolder + "/icons/comment.png"))
        tb.addAction(self.commentAct)

        self.uncommentAct = QAction("uncomment Line", self, shortcut="F3",
                                    toolTip="uncomment Line (F3)", triggered=self.uncommentLine)
        self.uncommentAct.setIcon(
            QIcon(self.appfolder + "/icons/uncomment.png"))
        tb.addAction(self.uncommentAct)

        self.commentBlockAct = QAction("comment Block", self, shortcut="F6",
                                       toolTip="comment selected block (F6)", triggered=self.commentBlock)
        self.commentBlockAct.setIcon(
            QIcon(self.appfolder + "/icons/commentBlock.png"))
        tb.addAction(self.commentBlockAct)

        self.uncommentBlockAct = QAction("uncomment Block (F7)", self, shortcut="F7",
                                         toolTip="uncomment selected block (F7)", triggered=self.uncommentBlock)
        self.uncommentBlockAct.setIcon(
            QIcon(self.appfolder + "/icons/uncommentBlock.png"))
        tb.addAction(self.uncommentBlockAct)
        # color chooser
        tb.addSeparator()
        tb.addAction(QIcon(self.appfolder + "/icons/color2"),
                     "insert Color", self.insertColor)
        tb.addSeparator()
        tb.addAction(QIcon(self.appfolder + "/icons/color1"),
                     "change Color", self.changeColor)
        # insert templates
        tb.addSeparator()
        self.templates = QComboBox()
        self.templates.setFixedWidth(200)
        self.templates.setToolTip("insert template")
        self.templates.activated[str].connect(self.insertTemplate)
        tb.addWidget(self.templates)
        # run python buttons
        tb.addSeparator()
        self.py2Act = QAction("run in Python 2 (F4)", self, shortcut="F4",
                              toolTip="run in Python 2 (F4)", triggered=self.runPy2)
        self.py2Act.setIcon(QIcon(self.appfolder + "/icons/python2"))
        tb.addAction(self.py2Act)
        self.py3Act = QAction("run in Python 3 (F5)", self, shortcut="F5",
                              toolTip="run in Python 3 (F5)", triggered=self.runPy3)
        self.py3Act.setIcon(QIcon(self.appfolder + "/icons/python3"))
        tb.addAction(self.py3Act)

        # about buttons
        tb.addSeparator()
        tb.addAction(QIcon(self.appfolder + "/icons/info"),
                     "&About PyEdit", self.about)
        tb.addSeparator()
        tb.addAction(QIcon(self.appfolder + "/icons/info2"),
                     "About &PyQT", QApplication.instance().aboutQt)
        tb.addSeparator()
        tb.addAction(QIcon.fromTheme("edit-clear"),
                     "clear Output Label", self.clearLabel)
        tb.addSeparator()
        # print preview
        self.printPreviewAct = QAction("preview", self, shortcut=QKeySequence.Print,
                                       toolTip="Preview Document", triggered=self.handlePrintPreview)
        self.printPreviewAct.setIcon(QIcon.fromTheme("document-print-preview"))
        tb.addAction(self.printPreviewAct)
        # print
        self.printAct = QAction("print", self, shortcut=QKeySequence.Print,
                                toolTip="Print Document", triggered=self.handlePrint)
        self.printAct.setIcon(QIcon.fromTheme("document-print"))
        tb.addAction(self.printAct)
        # end toolbar
        self.indentAct = QAction(QIcon.fromTheme("format-indent-more"), "indent more", self, triggered=self.indentLine,
                                 shortcut="F8")
        self.indentLessAct = QAction(QIcon.fromTheme("format-indent-less"), "indent less", self,
                                     triggered=self.indentLessLine, shortcut="F9")
        # find / replace toolbar
        tbf = QToolBar(self)
        tbf.setWindowTitle("Find Toolbar")
        self.findfield = QLineEdit()
        self.findfield.addAction(QIcon.fromTheme(
            "edit-find"), QLineEdit.LeadingPosition)
        self.findfield.setClearButtonEnabled(True)
        self.findfield.setFixedWidth(150)
        self.findfield.setPlaceholderText("查找")
        self.findfield.setToolTip("回车查找")
        self.findfield.setText("")
        ft = self.findfield.text()
        self.findfield.returnPressed.connect(self.findText)
        tbf.addWidget(self.findfield)
        self.replacefield = QLineEdit()
        self.replacefield.addAction(QIcon.fromTheme(
            "edit-find-and-replace"), QLineEdit.LeadingPosition)
        self.replacefield.setClearButtonEnabled(True)
        self.replacefield.setFixedWidth(150)
        self.replacefield.setPlaceholderText("替换..")
        self.replacefield.setToolTip("回车来替换第一个")
        self.replacefield.returnPressed.connect(self.replaceOne)
        tbf.addSeparator()
        tbf.addWidget(self.replacefield)
        tbf.addSeparator()

        tbf.addAction("替换所有", self.replaceAll)
        tbf.addSeparator()
        tbf.addAction(self.indentAct)
        tbf.addAction(self.indentLessAct)
        tbf.addSeparator()
        self.gotofield = QLineEdit()
        self.gotofield.addAction(QIcon.fromTheme(
            "next"), QLineEdit.LeadingPosition)
        self.gotofield.setClearButtonEnabled(True)
        self.gotofield.setFixedWidth(120)
        self.gotofield.setPlaceholderText("跳转到")
        self.gotofield.setToolTip("回车跳转")
        self.gotofield.returnPressed.connect(self.gotoLine)
        tbf.addWidget(self.gotofield)

        tbf.addSeparator()
        self.bookmarks = QComboBox()
        self.bookmarks.setFixedWidth(200)
        self.bookmarks.setToolTip("跳转到书签")
        self.bookmarks.activated[str].connect(self.gotoBookmark)
        tbf.addWidget(self.bookmarks)

        self.bookAct = QAction("添加书签", self,
                               toolTip="添加书签", triggered=self.addBookmark)
        self.bookAct.setIcon(QIcon.fromTheme("previous"))
        tbf.addAction(self.bookAct)

        tbf.addSeparator()
        self.bookrefresh = QAction("update Bookmarks", self,
                                   toolTip="update Bookmarks", triggered=self.findBookmarks)
        self.bookrefresh.setIcon(QIcon.fromTheme("view-refresh"))
        tbf.addAction(self.bookrefresh)
        tbf.addAction(QAction(QIcon.fromTheme("document-properties"), "check && reindent Text", self,
                              triggered=self.reindentText))
        tbf.addAction(QAction(QIcon.fromTheme("ok"),
                              "测试按钮", self, triggered=self.Test))
        layoutV = uni_Widget.ICTFESplitter(QtCore.Qt.Vertical)
        layoutV.setContentsMargins(0, 0, 0, 0)

        bar = self.menuBar()
        self.filemenu = bar.addMenu("File")
        self.separatorAct = self.filemenu.addSeparator()
        self.filemenu.addAction(self.newAct)
        self.filemenu.addAction(self.openAct)
        self.filemenu.addAction(self.saveAct)
        self.filemenu.addAction(self.saveAsAct)
        self.filemenu.addSeparator()
        for i in range(self.MaxRecentFiles):
            self.filemenu.addAction(self.recentFileActs[i])
        self.updateRecentFileActions()
        self.filemenu.addSeparator()
        self.clearRecentAct = QAction(
            "clear Recent Files List", self, triggered=self.clearRecentFiles)
        self.clearRecentAct.setIcon(QIcon.fromTheme("edit-clear"))
        self.filemenu.addAction(self.clearRecentAct)
        self.filemenu.addSeparator()

        editmenu = bar.addMenu("Edit")
        editmenu.addAction(
            QAction(QIcon.fromTheme('edit-undo'), "Undo", self, triggered=self.editor.undo, shortcut="Ctrl+u"))
        editmenu.addAction(
            QAction(QIcon.fromTheme('edit-redo'), "Redo", self, triggered=self.editor.redo, shortcut="Shift+Ctrl+u"))
        editmenu.addSeparator()
        editmenu.addAction(
            QAction(QIcon.fromTheme('edit-copy'), "Copy", self, triggered=self.editor.copy, shortcut="Ctrl+c"))
        editmenu.addAction(
            QAction(QIcon.fromTheme('edit-cut'), "Cut", self, triggered=self.editor.cut, shortcut="Ctrl+x"))
        editmenu.addAction(
            QAction(QIcon.fromTheme('edit-paste'), "Paste", self, triggered=self.editor.paste, shortcut="Ctrl+v"))
        editmenu.addAction(
            QAction(QIcon.fromTheme('edit-delete'), "Delete", self, triggered=self.editor.cut, shortcut="Del"))
        editmenu.addSeparator()
        editmenu.addAction(
            QAction(QIcon.fromTheme('edit-select-all'), "Select All", self, triggered=self.editor.selectAll,
                    shortcut="Ctrl+a"))
        editmenu.addSeparator()
        editmenu.addAction(self.commentAct)
        editmenu.addAction(self.uncommentAct)
        editmenu.addSeparator()
        editmenu.addAction(self.commentBlockAct)
        editmenu.addAction(self.uncommentBlockAct)
        editmenu.addSeparator()
        editmenu.addAction(self.py2Act)
        editmenu.addAction(self.py3Act)
        editmenu.addSeparator()
        editmenu.addAction(self.jumpToAct)
        editmenu.addSeparator()
        editmenu.addAction(self.indentAct)
        editmenu.addAction(self.indentLessAct)
        layoutV.addWidget(bar)
        layoutV.addWidget(tb)
        layoutV.addWidget(tbf)
        self.editorArea = QWidget()
        self.editorArea.setLayout(layoutH)
        layoutH.setContentsMargins(0, 0, 0, 0)
        layoutV.addWidget(self.editorArea)
        self.mylabel.setMinimumHeight(28)
        self.mylabel.setStyleSheet(stylesheet2(self))
        #        self.statusBar().showMessage("Welcome to PyEdit2")
        layoutV.addWidget(self.mylabel)
        # main window
        mq = QWidget(self)
        self.mainLayouts = QVBoxLayout()
        self.mainLayouts.addWidget(layoutV)
        mq.setLayout(self.mainLayouts)
        self.setCentralWidget(mq)

        # Event Filter ...
        self.installEventFilter(self)
        self.editor.setFocus()
        self.cursor = QTextCursor()
        self.editor.setTextCursor(self.cursor)
        self.editor.setPlainText(self.mainText)
        self.editor.moveCursor(self.cursor.End)
        self.editor.document().modificationChanged.connect(self.setWindowModified)

        # Brackets ExtraSelection ...
        self.left_selected_bracket = QTextEdit.ExtraSelection()
        self.right_selected_bracket = QTextEdit.ExtraSelection()

        # shell settings
        self.process = QProcess(self)
        self.process.setProcessChannelMode(QProcess.MergedChannels)
        self.process.readyRead.connect(self.dataReady)
        self.process.started.connect(
            lambda: self.mylabel.append("starting shell"))
        self.process.finished.connect(
            lambda: self.mylabel.append("shell ended"))

        self.editor.setContextMenuPolicy(Qt.CustomContextMenu)
        self.editor.customContextMenuRequested.connect(
            self.contextMenuRequested)

        self.loadTemplates()

    def loadTemplates(self):
        folder = self.appfolder + "/templates"
        if QDir().exists(folder):
            self.currentDir = QDir(folder)
            count = self.currentDir.count()
            fileName = "*"
            files = self.currentDir.entryList([fileName],
                                              QDir.Files | QDir.NoSymLinks)
            #            self.statusBar().showMessage(','.join(files))
            for i in range(count - 2):
                file = (files[i])
                if file.endswith(".txt"):
                    self.templates.addItem(file.replace(
                        self.appfolder + "/templates", "").replace(".txt", ""))

    def Test(self):
        #        self.editor.moveCursor(QTextCursor.StartOfWord, QTextCursor.MoveAnchor)
        #        self.editor.moveCursor(QTextCursor.EndOfWord, QTextCursor.KeepAnchor)
        #        self.findBookmark(self.editor.textCursor().selectedText())
        #        self.statusBar().showMessage("found bookmark")
        self.editor.selectAll()

    def reindentText(self):
        self.editor.selectAll()
        tab = "\t"
        oldtext = self.editor.textCursor().selectedText()
        newtext = oldtext.replace("    ", tab)
        self.editor.textCursor().insertText(newtext)
        self.statusBar().showMessage("reindented")

    def insertColor(self):
        col = QColorDialog.getColor(QColor("#000000"), self)
        if not col.isValid():
            return
        else:
            colorname = 'QColor("' + col.name() + '")'
            self.editor.textCursor().insertText(colorname)

    def changeColor(self):
        if not self.editor.textCursor().selectedText() == "":
            col = QColorDialog.getColor(
                QColor("#" + self.editor.textCursor().selectedText()), self)
            if not col.isValid():
                return
            else:
                colorname = col.name()
                self.editor.textCursor().insertText(colorname.replace("#", ""))

    def contextMenuRequested(self, point):
        cmenu = QMenu()
        cmenu = self.editor.createStandardContextMenu()
        cmenu.addSeparator()
        cmenu.addAction(self.jumpToAct)
        cmenu.addSeparator()
        cmenu.addAction(QIcon.fromTheme("gtk-find-and-replace"),
                        "replace all occurrences with", self.replaceThis)
        cmenu.addSeparator()
        cmenu.addAction(self.py2Act)
        cmenu.addAction(self.py3Act)
        cmenu.addSeparator()
        cmenu.addAction(self.commentAct)
        cmenu.addAction(self.uncommentAct)
        cmenu.addSeparator()
        cmenu.addAction(self.commentBlockAct)
        cmenu.addAction(self.uncommentBlockAct)
        cmenu.addSeparator()
        cmenu.addAction(self.indentAct)
        cmenu.addAction(self.indentLessAct)
        cmenu.addSeparator()
        cmenu.addAction(QIcon(self.appfolder + "/icons/color2"),
                        "insert Color", self.insertColor)
        cmenu.addSeparator()
        cmenu.addAction(QIcon(self.appfolder + "/icons/color1"),
                        "change Color", self.changeColor)
        cmenu.exec_(self.editor.mapToGlobal(point))

    def replaceThis(self):
        rtext = self.editor.textCursor().selectedText()
        text = QInputDialog.getText(
            self, ("replace with"), (""), QLineEdit.Normal, "")
        oldtext = self.editor.document().toPlainText()
        if not (text[0] == ""):
            newtext = oldtext.replace(rtext, text[0])
            self.editor.setPlainText(newtext)
            self.setModified(True)

    def indentLine(self):
        if not self.editor.textCursor().selectedText() == "":
            newline = u"\u2029"
            list = []
            ot = self.editor.textCursor().selectedText()
            theList = ot.splitlines()
            self.statusBar().showMessage(theList[1])
            linecount = ot.count(newline)
            for i in range(linecount):
                list.insert(i, tab + theList[i])
            self.editor.textCursor().insertText(newline.join(list))
            self.setModified(True)
            self.statusBar().showMessage("tabs indented")

    def indentLessLine(self):
        if not self.editor.textCursor().selectedText() == "":
            newline = u"\u2029"
            list = []
            ot = self.editor.textCursor().selectedText()
            theList = ot.splitlines()
            self.statusBar().showMessage(theList[1])
            linecount = ot.count(newline)
            for i in range(linecount):
                list.insert(i, (theList[i]).replace(tab, "", 1))
            self.editor.textCursor().insertText(newline.join(list))
            self.setModified(True)
            self.statusBar().showMessage("tabs indented")

    def dataReady(self):
        out = ""
        try:
            out = str(self.process.readAll(), encoding='utf8').rstrip()
        except TypeError:
            self.msgbox("Error", str(self.process.readAll(), encoding='utf8'))
            out = str(self.process.readAll()).rstrip()
        self.mylabel.append(out)
        self.mylabel.moveCursor(self.cursor.Start)
        if self.mylabel.find("line"):
            s = self.mylabel.toPlainText().partition("line")[
                2].partition("\n")[0]
            self.gotoErrorLine(int(s))
        self.mylabel.moveCursor(self.cursor.End)
        self.mylabel.ensureCursorVisible()

    def createActions(self):
        for i in range(self.MaxRecentFiles):
            self.recentFileActs.append(
                QAction(self, visible=False,
                        triggered=self.openRecentFile))

    def addBookmark(self):
        linenumber = self.getLineNumber()
        linetext = self.editor.textCursor().block().text().strip()
        self.bookmarks.addItem(linetext, linenumber)

    def getLineNumber(self):
        self.editor.moveCursor(self.cursor.StartOfLine)
        linenumber = self.editor.textCursor().blockNumber() + 1
        return linenumber

    def gotoLine(self):
        ln = int(self.gotofield.text())
        linecursor = QTextCursor(
            self.editor.document().findBlockByLineNumber(ln - 1))
        self.editor.moveCursor(QTextCursor.End)
        self.editor.setTextCursor(linecursor)

    def gotoErrorLine(self, ln):
        linecursor = QTextCursor(
            self.editor.document().findBlockByLineNumber(ln - 1))
        self.editor.moveCursor(QTextCursor.End)
        self.editor.setTextCursor(linecursor)
        self.editor.moveCursor(QTextCursor.EndOfLine, QTextCursor.KeepAnchor)

    def gotoBookmark(self):
        if self.editor.find(self.bookmarks.itemText(self.bookmarks.currentIndex())):
            pass
        else:
            self.editor.moveCursor(QTextCursor.Start)
            self.editor.find(self.bookmarks.itemText(
                self.bookmarks.currentIndex()))

        self.editor.centerCursor()
        self.editor.moveCursor(self.cursor.StartOfLine, self.cursor.MoveAnchor)

    def gotoBookmarkFromMenu(self):
        if self.editor.textCursor().selectedText() == "":
            self.editor.moveCursor(
                QTextCursor.StartOfWord, QTextCursor.MoveAnchor)
            self.editor.moveCursor(QTextCursor.EndOfWord,
                                   QTextCursor.KeepAnchor)
        toFind = self.editor.textCursor().selectedText()
        self.bookmarks.setCurrentIndex(0)
        if self.bookmarks.findText(toFind, Qt.MatchContains):
            row = self.bookmarks.findText(toFind, Qt.MatchContains)
            self.statusBar().showMessage("found '" + toFind + "' at bookmark " + str(row))
            self.bookmarks.setCurrentIndex(row)
            self.gotoBookmark()
        else:
            self.statusBar().showMessage("def not found")

    def clearBookmarks(self):
        self.bookmarks.clear()

    # find lines with def or class
    def findBookmarks(self):
        self.editor.setFocus()
        self.editor.moveCursor(QTextCursor.Start)
        if self.editor.textCursor().selectedText() == "":
            self.clearBookmarks()
            newline = u"\u2029"  # "\u2029"
            fr = "from"
            im = "import"
            d = "def"
            d2 = "    def"
            c = "class"
            sn = str("if __name__ ==")
            line = ""
            list = []
            self.editor.selectAll()
            ot = self.editor.textCursor().selectedText()
            theList = ot.splitlines()
            linecount = ot.count(newline)
            for i in range(linecount):
                if theList[i].startswith(im):
                    line = str(theList[i]).replace(
                        "'\t','[", "").replace("]", "")
                    self.bookmarks.addItem(str(line), i)
                elif theList[i].startswith(fr):
                    line = str(theList[i]).replace(
                        "'\t','[", "").replace("]", "")
                    self.bookmarks.addItem(str(line), i)
                elif theList[i].startswith(c):
                    line = str(theList[i]).replace(
                        "'\t','[", "").replace("]", "")
                    self.bookmarks.addItem(str(line), i)
                elif theList[i].startswith(tab + d):
                    line = str(theList[i]).replace(tab, "").replace(
                        "'\t','[", "").replace("]", "")
                    self.bookmarks.addItem(str(line), i)
                elif theList[i].startswith(d2):
                    line = str(theList[i]).replace(tab, "").replace(
                        "'\t','[", "").replace("]", "")
                    self.bookmarks.addItem(str(line), i)
                elif theList[i].startswith(sn):
                    line = str(theList[i]).replace(
                        "'\t','[", "").replace("]", "")
                    self.bookmarks.addItem(str(line), i)

        self.editor.moveCursor(QTextCursor.Start)
        self.statusBar().showMessage("bookmarks changed")

    def clearLabel(self):
        self.mylabel.setText("")

    def openRecentFile(self):
        action = self.sender()
        if action:
            if (self.maybeSave()):
                self.openFileOnStart(action.data())

        # New File

    def newFile(self):
        if self.maybeSave():
            self.editor.clear()
            self.editor.setPlainText(self.mainText)
            self.filename = ""
            self.setModified(False)
            self.editor.moveCursor(self.cursor.End)
            self.statusBar().showMessage("new File created.")
            self.editor.setFocus()
            self.bookmarks.clear()
            self.setWindowTitle("new File[*]")

    # open File
    def openFileOnStart(self, path=None):
        self.editor.setReadOnly(False)
        if path:
            inFile = QFile(path)
            if inFile.open(QFile.ReadWrite | QFile.Text):
                text = inFile.readAll()
                try:
                    text = str(text, encoding='UTF-8')
                except:
                    text = str(text)
                    self.editor.setReadOnly(True)
                try:
                    self.editor.setPlainText(text)
                except:
                    return
                self.setModified(False)
                self.setCurrentFile(path)
                self.editor.setFocus()
                self.findBookmarks()

                self.statusBar().showMessage(
                    "File '" + path + "' loaded succesfully & bookmarks added")

        # open File

    def openFile(self, path=None):
        if self.maybeSave():
            if not path:
                path, _ = QFileDialog.getOpenFileName(self, "Open File", self.dirpath,
                                                      "Python Files (*.py)")

            if path:
                self.openFileOnStart(path)

    def fileSave(self):
        if (self.filename != ""):
            file = QFile(self.filename)
            if not file.open(QFile.WriteOnly | QFile.Text):
                QMessageBox.warning(self, "Error",
                                    "Cannot write file %s:\n%s." % (self.filename, file.errorString()))
                return

            outstr = QTextStream(file)
            QApplication.setOverrideCursor(Qt.WaitCursor)
            outstr << self.editor.toPlainText()
            QApplication.restoreOverrideCursor()
            self.setModified(False)
            self.fname = QFileInfo(self.filename).fileName()
            self.setWindowTitle(self.fname + "[*]")
            self.statusBar().showMessage("File saved.")
            self.setCurrentFile(self.filename)
            self.editor.setFocus()

        else:
            self.fileSaveAs()

            # save File

    def fileSaveAs(self):
        fn, _ = QFileDialog.getSaveFileName(self, "Save as...", self.filename,
                                            "Python files (*.py)")

        if not fn:
            print("Error saving")
            return False

        lfn = fn.lower()
        if not lfn.endswith('.py'):
            fn += '.py'

        self.filename = fn
        self.fname = path.splitext(str(fn))[0].split("/")[-1]
        return self.fileSave()

    def closeEvent(self, e):
        if self.maybeSave():
            e.accept()
        else:
            e.ignore()

        # ask to save

    def maybeSave(self):
        if not self.isModified():
            return True

        if self.filename.startswith(':/'):
            return True

        ret = QMessageBox.question(self, "Message",
                                   "<h4><p>The document was modified.</p>\n"
                                   "<p>Do you want to save changes?</p></h4>",
                                   QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)

        if ret == QMessageBox.Yes:
            if self.filename == "":
                self.fileSaveAs()
                return False
            else:
                self.fileSave()
                return True

        if ret == QMessageBox.Cancel:
            return False

        return True

    def about(self):
        link = "<p><a title='Axel Schneider' href='http://goodoldsongs.jimdo.com' target='_blank'>Axel Schneider</a></p>"
        title = "about PyEdit"
        message = "<span style='color: #1F9CDD; font-size: 24pt;font-weight: bold;'\
                    >PyEdit 1.0</strong></span></p><h2>Python Editor</h2>created by <h3>" + link + "</h3> with PyQt5<br>" \
                  + "<br>Copyright © 2017 The Qt Company Ltd and other contributors." \
                  + "<br>Qt and the Qt logo are trademarks of The Qt Company Ltd."
        info = "<span style='color: #1F9CDD; font-size: 14pt;'>©2017 Axel Schneider</strong></span></p>"
        detail = "PyEdit 1.0"
        self.infobox(title, message, info, detail)

    def runPy3(self):
        if not self.editor.toPlainText() == self.mainText:
            if self.filename:
                self.mypython = "2"
                self.statusBar().showMessage("running " + self.filename + " in Python 2")
                self.fileSave()
                cmd = "python"
                self.readData(cmd)
            else:
                self.filename = "/tmp/tmp3.py"
                self.fileSave()
                self.runPy3()
        else:
            self.statusBar().showMessage("no code to run")

    def runPy2(self):
        if not self.editor.toPlainText() == self.mainText:
            if self.filename:
                self.mypython = "2"
                self.statusBar().showMessage("running " + self.filename + " in Python 2")
                self.fileSave()
                cmd = "python"
                self.readData(cmd)
            else:
                self.filename = "/tmp/tmp2.py"
                self.fileSave()
                self.runPy2()
        else:
            self.statusBar().showMessage("no code to run")

    def readData(self, cmd):
        self.mylabel.clear()
        dname = path.abspath(path.join(self.filename, pardir)) + "/"
        self.process.start(
            cmd, ['-u', dname + self.strippedName(self.filename)])

    def killPython(self):
        if (self.mypython == "3"):
            cmd = "killall python3"
        elif (self.mypython == "2"):
            cmd = "killall python"
        self.readData(cmd)

    def commentBlock(self):
        self.editor.copy()
        clipboard = QApplication.clipboard()
        originalText = clipboard.text()
        mt1 = "'''" + "\n"
        mt2 = "\n" + "'''"
        mt = mt1 + originalText + mt2
        clipboard.setText(mt)
        self.editor.paste()

    def uncommentBlock(self):
        self.editor.copy()
        clipboard = QApplication.clipboard()
        originalText = clipboard.text()
        mt1 = "'''" + "\n"
        mt2 = "\n" + "'''"
        clipboard.setText(originalText.replace(mt1, "").replace(mt2, ""))
        self.editor.paste()

        self.statusBar().showMessage("added block comment")

    def commentLine(self):
        if not self.editor.textCursor().selectedText() == "":
            newline = u"\u2029"
            comment = "#"
            list = []
            ot = self.editor.textCursor().selectedText()
            theList = ot.splitlines()
            self.statusBar().showMessage(theList[1])
            linecount = ot.count(newline)
            for i in range(linecount + 1):
                list.insert(i, comment + theList[i])
            self.editor.textCursor().insertText(newline.join(list))
            self.setModified(True)
            self.statusBar().showMessage("added comment")

    def uncommentLine(self):
        if not self.editor.textCursor().selectedText() == "":
            comment = "#"
            newline = u"\u2029"
            list = []
            ot = self.editor.textCursor().selectedText()
            theList = ot.splitlines()
            self.statusBar().showMessage(theList[1])
            linecount = ot.count(newline)
            for i in range(linecount + 1):
                list.insert(i, (theList[i]).replace(comment, "", 1))
            self.editor.textCursor().insertText(newline.join(list))
            self.setModified(True)
            self.statusBar().showMessage("comment removed")

    def goToLine(self, ft):
        self.editor.moveCursor(int(self.gofield.currentText()),
                               QTextCursor.MoveAnchor)  # not working

    def findText(self):
        word = self.findfield.text()
        if self.editor.find(word):
            linenumber = self.editor.textCursor().blockNumber() + 1
            self.statusBar().showMessage("found <b>'" + self.findfield.text() +
                                         "'</b> at Line: " + str(linenumber))
            self.editor.centerCursor()
        else:
            self.statusBar().showMessage("<b>'" + self.findfield.text() + "'</b> not found")
            self.editor.moveCursor(QTextCursor.Start)
            if self.editor.find(word):
                linenumber = self.editor.textCursor().blockNumber() + 1
                self.statusBar().showMessage("found <b>'" + self.findfield.text() +
                                             "'</b> at Line: " + str(linenumber))
                self.editor.centerCursor()

    def findBookmark(self, word):
        if self.editor.find(word):
            linenumber = self.getLineNumber()  # self.editor.textCursor().blockNumber() + 1
            self.statusBar().showMessage("found <b>'" + self.findfield.text() +
                                         "'</b> at Line: " + str(linenumber))

    def set_numbers_visible(self, value=True):
        self.numbers.setVisible(False)

    def match_left(self, block, character, start, found):
        map = {'{': '}', '(': ')', '[': ']'}

        while block.isValid():
            data = block.userData()
            if data is not None:
                braces = data.braces
                N = len(braces)

                for k in range(start, N):
                    if braces[k].character == character:
                        found += 1

                    if braces[k].character == map[character]:
                        if not found:
                            return braces[k].position + block.position()
                        else:
                            found -= 1

                block = block.next()
                start = 0

    def match_right(self, block, character, start, found):
        map = {'}': '{', ')': '(', ']': '['}

        while block.isValid():
            data = block.userData()

            if data is not None:
                braces = data.braces

                if start is None:
                    start = len(braces)
                for k in range(start - 1, -1, -1):
                    if braces[k].character == character:
                        found += 1
                    if braces[k].character == map[character]:
                        if found == 0:
                            return braces[k].position + block.position()
                        else:
                            found -= 1
            block = block.previous()
            start = None

        cursor = self.editor.textCursor()
        block = cursor.block()
        data = block.userData()
        previous, next = None, None

        if data is not None:
            position = cursor.position()
            block_position = cursor.block().position()
            braces = data.braces
            N = len(braces)

            for k in range(0, N):
                if braces[k].position == position - block_position or braces[
                        k].position == position - block_position - 1:
                    previous = braces[k].position + block_position
                    if braces[k].character in ['{', '(', '[']:
                        next = self.match_left(block,
                                               braces[k].character,
                                               k + 1, 0)
                    elif braces[k].character in ['}', ')', ']']:
                        next = self.match_right(block,
                                                braces[k].character,
                                                k, 0)
                    if next is None:
                        next = -1

        if next is not None and next > 0:
            if next == 0 and next >= 0:
                format = QTextCharFormat()

            cursor.setPosition(previous)
            cursor.movePosition(QTextCursor.NextCharacter,
                                QTextCursor.KeepAnchor)

            format.setBackground(QColor('white'))
            self.left_selected_bracket.format = format
            self.left_selected_bracket.cursor = cursor

            cursor.setPosition(next)
            cursor.movePosition(QTextCursor.NextCharacter,
                                QTextCursor.KeepAnchor)

            format.setBackground(QColor('white'))
            self.right_selected_bracket.format = format
            self.right_selected_bracket.cursor = cursor

    def paintEvent(self, event):
        highlighted_line = QTextEdit.ExtraSelection()
        highlighted_line.format.setBackground(lineHighlightColor)
        highlighted_line.format.setProperty(QTextFormat
                                            .FullWidthSelection,
                                            QVariant(True))
        highlighted_line.cursor = self.editor.textCursor()
        highlighted_line.cursor.clearSelection()
        self.editor.setExtraSelections([highlighted_line,
                                        self.left_selected_bracket,
                                        self.right_selected_bracket])

    def document(self):
        return self.editor.document

    def isModified(self):
        return self.editor.document().isModified()

    def setModified(self, modified):
        self.editor.document().setModified(modified)

    def setLineWrapMode(self, mode):
        self.editor.setLineWrapMode(mode)

    def clear(self):
        self.editor.clear()

    def setPlainText(self, *args, **kwargs):
        self.editor.setPlainText(*args, **kwargs)

    def setDocumentTitle(self, *args, **kwargs):
        self.editor.setDocumentTitle(*args, **kwargs)

    def set_number_bar_visible(self, value):
        self.numbers.setVisible(value)

    def replaceAll(self):
        print("replacing all")
        oldtext = self.editor.document().toPlainText()
        newtext = oldtext.replace(
            self.findfield.text(), self.replacefield.text())
        self.editor.setPlainText(newtext)
        self.setModified(True)

    def replaceOne(self):
        print("replacing all")
        oldtext = self.editor.document().toPlainText()
        newtext = oldtext.replace(
            self.findfield.text(), self.replacefield.text(), 1)
        self.editor.setPlainText(newtext)
        self.setModified(True)

    def setCurrentFile(self, fileName):
        self.filename = fileName
        if self.filename:
            self.setWindowTitle(self.strippedName(self.filename) + "[*]")
        else:
            self.setWindowTitle("no File")

        files = self.settings.value('recentFileList', [])

        try:
            files.remove(fileName)
        except ValueError:
            pass

        files.insert(0, fileName)
        del files[self.MaxRecentFiles:]

        self.settings.setValue('recentFileList', files)

        for widget in QApplication.topLevelWidgets():
            if isinstance(widget, EditorPanel):
                widget.updateRecentFileActions()

    def updateRecentFileActions(self):
        mytext = ""
        files = self.settings.value('recentFileList', [])

        numRecentFiles = min(len(files), self.MaxRecentFiles)

        for i in range(numRecentFiles):
            text = "&%d %s" % (i + 1, self.strippedName(files[i]))
            self.recentFileActs[i].setText(text)
            self.recentFileActs[i].setData(files[i])
            self.recentFileActs[i].setVisible(True)
            self.recentFileActs[i].setIcon(
                QIcon.fromTheme("gnome-mime-text-x-python"))

        for j in range(numRecentFiles, self.MaxRecentFiles):
            self.recentFileActs[j].setVisible(False)

        self.separatorAct.setVisible((numRecentFiles > 0))

    def strippedName(self, fullFileName):
        return QFileInfo(fullFileName).fileName()

    def clearRecentFiles(self):
        self.settings.clear()
        self.updateRecentFileActions()

    def msgbox(self, title, message):
        QMessageBox.warning(self, title, message)

    def infobox(self, title, message, info, detail):
        QMessageBox(QMessageBox.Information, title, message, QMessageBox.NoButton, self,
                    Qt.Dialog | Qt.NoDropShadowWindowHint).show()

    def insertTemplate(self):
        line = int(self.getLineNumber())
        path = self.appfolder + "/templates/" + \
            self.templates.itemText(self.templates.currentIndex()) + ".txt"
        if path:
            inFile = QFile(path)
            if inFile.open(QFile.ReadOnly | QFile.Text):
                text = inFile.readAll()
                self.editor.setFocus()
                try:  # python 3
                    self.editor.textCursor().insertText(str(text, encoding='utf8'))
                except TypeError:  # python 2
                    self.editor.textCursor().insertText(str(text))
                self.setModified(True)
                self.findBookmarks()
                self.statusBar().showMessage(
                    "'" + self.templates.itemText(self.templates.currentIndex()) + "' inserted")
                inFile.close()
                text = ""
                self.selectLine(line)
            else:
                self.statusBar().showMessage("error loadind Template")

    def selectLine(self, line):
        linecursor = QTextCursor(
            self.editor.document().findBlockByLineNumber(line - 1))
        self.editor.moveCursor(QTextCursor.End)
        self.editor.setTextCursor(linecursor)

    def handlePrint(self):
        if self.editor.toPlainText() == "":
            self.statusBar().showMessage("no text")
        else:
            dialog = QtPrintSupport.QPrintDialog()
            if dialog.exec_() == QDialog.Accepted:
                self.handlePaintRequest(dialog.printer())
                self.statusBar().showMessage("Document printed")

    def handlePrintPreview(self):
        if self.editor.toPlainText() == "":
            self.statusBar().showMessage("no text")
        else:
            dialog = QtPrintSupport.QPrintPreviewDialog()
            dialog.setFixedSize(900, 650)
            dialog.paintRequested.connect(self.handlePaintRequest)
            dialog.exec_()
            self.statusBar().showMessage("Print Preview closed")

    def handlePaintRequest(self, printer):
        printer.setDocName(self.filename)
        document = self.editor.document()
        document.print_(printer)


def stylesheet2(self):
    return """
QPlainTextEdit
{
background: #141414;
color: rgb(200, 200, 200);
border: 0px solid rgb(50, 50, 50);
}
QTextEdit
{
background: #101010;
color: rgb(200, 200, 200);
padding-left: 6px;
border: 1px solid rgb(50, 50, 50);
}
QStatusBar
{
height: 22px;
background: transparent;
color: #4F4F4F;
font-size: 12pt;
}
    """
