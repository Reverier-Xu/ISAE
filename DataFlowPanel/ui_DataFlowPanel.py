from DataFlowPanel.DataFlowNodeEditor import *
from DataFlowPanel.OptionEditBox import *
from DataFlowPanel.DataFlowDragList import *


class ui_DataFlowPanel(QtWidgets.QWidget):
    def __init__(self):
        super(ui_DataFlowPanel, self).__init__(flags=Qt.WindowFlags())
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.CryptoMainSplitter = uni_Widget.ICTFESplitter(self)

        self.CryptoMainSplitter.setOrientation(QtCore.Qt.Horizontal)
        self.CryptoMainSplitter.setObjectName("CryptoMainSplitter")
        self.ToolsArea = uni_Widget.ICTFEScrollArea(self.CryptoMainSplitter)
        self.ToolsArea.setWidgetResizable(True)
        self.ToolsArea.setObjectName("ToolsArea")
        self.ToolsAreaPanel = QtWidgets.QWidget(flags=Qt.WindowFlags())
        self.ToolsAreaPanel.setGeometry(QtCore.QRect(0, 0, 386, 698))
        self.ToolsAreaPanel.setObjectName("ToolsAreaPanel")
        self.ToolsAreaPanel.setStyleSheet('QWidget#ToolsAreaPanel{background-color: rgb(20, 20, 20);}')
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.ToolsAreaPanel)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.ToolsSearchBox = uni_Widget.ICTFELineBox(self.ToolsAreaPanel)
        self.ToolsSearchBox.setStyleSheet('color: white;'
                                          'border: 1px solid gray;'
                                          'border-radius: 0px;'
                                          'padding: 5px;'
                                          'background: rgb(20, 20, 20);'
                                          'selection-background-color: blue;')
        self.ToolsSearchBox.setPlaceholderText('搜索...')
        self.ToolsSearchBox.setObjectName("ToolsSearchBox")
        self.verticalLayout_5.addWidget(self.ToolsSearchBox, alignment=Qt.Alignment())
        self.ToolsList = DragList(self.ToolsAreaPanel)
        self.ToolsList.setStyleSheet("QTreeWidget::item:hover{color: lightgrey; background-color: rgb(50,50,50)}"
                                     "QTreeWidget::item:selected{color: lightgrey; background-color:rgb(80,110,205)}"
                                     "QTreeWidget{border: 1px solid grey; color: lightgrey; background-color: rgb(20, 20, 20)}")
        self.ToolsList.setObjectName("ToolsList")
        self.verticalLayout_5.addWidget(self.ToolsList, alignment=Qt.Alignment())
        self.ToolsArea.setWidget(self.ToolsAreaPanel)
        self.widget = QtWidgets.QWidget(self.CryptoMainSplitter, flags=Qt.WindowFlags())
        self.widget.setObjectName("widget")
        self.NodeEditorLayout = QtWidgets.QVBoxLayout(self.widget)
        self.NodeEditorLayout.setContentsMargins(0, 0, 0, 0)
        self.NodeEditorLayout.setObjectName("NodeEditorLayout")
        self.NodeEditorLayout.setSpacing(0)
        scene = FlowScene()
        self.CryptoToolNodeEditor = CryptoFlowView(scene)
        self.CryptoToolNodeEditor.setStyleSheet('#CryptoToolNodeEditor{border: 0px solid grey;}')
        self.CryptoToolNodeEditor.setObjectName("CryptoToolNodeEditor")
        self.NodeEditorLayout.addWidget(self.CryptoToolNodeEditor, alignment=Qt.Alignment())
        self.NodeEditorLayout.addWidget(self.CryptoToolNodeEditor, alignment=Qt.Alignment())
        self.FileAndOptionsLayout = uni_Widget.ICTFESplitter(self.CryptoMainSplitter)
        self.FileAndOptionsLayout.setOrientation(QtCore.Qt.Vertical)
        self.FileAndOptionsLayout.setObjectName("FileAndOptionsLayout")
        self.OptionsArea = uni_Widget.ICTFEScrollArea(self.FileAndOptionsLayout)
        self.OptionsArea.setWidgetResizable(True)
        self.OptionsArea.setObjectName("OptionsArea")
        self.OptionsAreaPanel = QtWidgets.QWidget(flags=Qt.WindowFlags())
        self.OptionsAreaPanel.setGeometry(QtCore.QRect(0, 0, 386, 348))
        self.OptionsAreaPanel.setObjectName("OptionsAreaPanel")
        self.OptionsAreaPanel.setStyleSheet('QWidget#OptionsAreaPanel{'
                                            'background-color: rgb(20, 20, 20);'
                                            'border: 0px solid rgb(40, 40, 40);'
                                            'color: white;'
                                            '}')
        self.verticalLayout = QtWidgets.QVBoxLayout(self.OptionsAreaPanel)
        self.verticalLayout.setObjectName("verticalLayout")
        self.OptionsTips = uni_Widget.ICTFELabel(self.OptionsAreaPanel)
        self.OptionsTips.setObjectName("OptionsTips")
        self.OptionTipsLayout = QtWidgets.QHBoxLayout()
        self.OptionTipsLayout.setContentsMargins(0, 0, 0, 0)
        self.OptionTipsLayout.addWidget(self.OptionsTips, alignment=Qt.Alignment())
        self.verticalLayout.addLayout(self.OptionTipsLayout)
        self.OptionsBox = OptionsEditBox()
        self.OptionsBox.setObjectName("OptionsBox")
        self.verticalLayout.addWidget(self.OptionsBox, alignment=Qt.Alignment())
        self.OptionsArea.setWidget(self.OptionsAreaPanel)
        self.horizontalLayout_2.addWidget(self.CryptoMainSplitter, alignment=Qt.Alignment())

        self.reTranslateUi()

    def reTranslateUi(self):
        self.OptionsTips.setText("节点选项")
