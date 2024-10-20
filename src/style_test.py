BLUE_STYLE = """*{
selection-background-color: rgb(67, 128, 179);
selection-color: rgb(255, 255, 255);
}

QMainWindow,QWidget
{
color:rgb(0,0,0);
background:rgb(255,255,255);
}

QMenuBar
{
color:rgb(120,120,120);
background:rgb(230,230,230);
}
QMenuBar::item:selected
{
color:rgb(100,100,100);
background:rgb(200,200,200);
}
QMenu
{
color:rgb(90,90,90);
background:rgb(230,230,230);
padding: 3;
}
QMenu::item:selected
{
color:rgb(90,90,90);
background:rgb(200,200,200);
}
QMenu::separator {
background:rgb(200,200,200);
height:1px;
}


QTabBar::tab {
color:rgb(150,150,150);
background:rgb(240,240,240);
height:30;
width:80;
border: rgb(240,240,240);
border-width: 0 0 2px 0;
padding-left:10;
}

QTabBar::tab:selected {
background:white;
color:rgb(100,100,100);
border: solid rgb(0,150,255);
border-width: 0 0 5px 0;
}
QTableWidget QTableCornerButton::section {
background-color: rgb(255, 255, 255);
}
QLineEdit,QTextBrowser,QTextEdit,QPlainTextEdit
{
color:rgb(20,20,20);
background-color:white;
border: solid lightgrey;
border-width: 0 0 2px 0;
border-bottom-left-radius: 5;
border-bottom-right-radius: 5;
}

QLineEdit:disabled
{
color:rgb(160, 150, 150);
background-color:rgb(255, 240, 240);
border: solid rgb(253, 14, 14);
border-width: 0 0 2px 0;
border-bottom-left-radius: 5;
border-bottom-right-radius: 5;
}

QComboBox
{
color:rgb(0,115,170);
background-color:rgb(255, 255, 255);
min-width: 5px;
padding: 1px 0px 1px 3px;
border: 1px solid rgb(0,115,170);
}

QComboBox:hover
{
color:rgb(0,115,170);
background-color: white;
}

QComboBox:selected
{
color:rgb(0,115,170);
selection-background-color: rgb(255, 255, 255);
}

QComboBox::drop-down
{
width: 30px;
background-color:rgb(0,115,170);
}

QComboBox::down-arrow
{
image: url(assets/UI/Icons/interface_icons/arrow_down.png);
width: 14px;
height: 14px;
}


QCheckBox
{
background: rgb(255, 255, 255);
color:rgb(25, 29, 32);
padding: 6;
}
QToolBox::tab
{
color:darkgrey;
background:lightgrey;
}
QToolBox::tab::selected
{
color:grey;
background:rgb(250, 250,250);
}
QToolBox::tab::hover
{
color:white;
background:rgb(0,115,170);
}
QProgressBar {
color:grey;
text-align: center;
font-size:13px;
}
QProgressBar::chunk {
background:rgb(0, 193, 50);
}
QPushButton
{
border: 1px solid lightgrey;
color:white;
background:rgb(0,115,170);
min-height:30;
min-width: 50;
}
QPushButton:hover
{
border: 1px solid lightgrey;
color:white;
background:rgb(0, 120, 210);
}

QPushButton:pressed
{
border: 1px solid lightgrey;
color:white;
background:rgb(0, 53, 100);
}
QLCDNumber
{
color:rgb(0,115,170);
border:2 solid rgb(100,100,100);
}
QTableView,
QTableWidget
{
alternate-background-color: rgb(240, 250, 255);
}
QTreeView
{
background: rgb(250,250,250);
color: rgb(180,180,180);
}
QTableView::item:selected,
QListView::item:selected,
QTableView::item:hover,
QListView::item:hover,
QTreeView::item:hover
{
background:rgb(0,115,170);
color:rgb(250,250,250);
}
QTableView::item,
QListView::item,
QTreeView::item
{
color:rgb(100,100,100);
}
QTreeView::item:selected,QListView::item:selected,QTableView::item:selected
{
color:rgb(37, 62, 71);
background:rgb(209, 241, 252);
}
QHeaderView::section
{
color:rgb(133, 133, 133);
background:white;
border:transparent;
text-align:center;
padding:1;
}
QCalendarView
{
color: rgb(20,20,20);
background-color: rgb(240,240,240);
alternate-background-color: rgb(0,115,170);
selection-background-color: white;
selection-color: black;
}
QAbstractItemView
{
color:rgb(200,200,200);
}



QSlider::groove:horizontal,QSlider::add-page:horizontal
{
background: rgb(255, 255, 255);
height: 27px;
}
QSlider::sub-page:horizontal {
height: 10px;
background: rgb(0,115,170);
}
QSlider::handle:horizontal {
margin-right: -10px;
margin-left: -10px;
background: rgb(0,115,170);
}
QSlider::handle:horizontal:hover {
background:rgb(0,115,170);
}


QSlider::handle
{
border-radius: 3px;
}

QSlider::groove:vertical,QSlider::add-page:vertical,QSlider::sub-page:vertical
{
width: 20px;
background: rgb(255, 255, 255);
}

QSlider::handle:vertical {
margin-top: -10px;
margin-bottom: -10px;
background: rgb(0,115,170);
}
QSlider::handle:vertical:hover {
background: rgb(0,115,170);
}


QScrollBar::groove:horizontal{
background: white;
height: 17px;
}
QScrollBar::sub-page:horizontal,QScrollBar::add-page:horizontal  {
height: 10px;
background: rgb(255, 255, 255);
}
QScrollBar::handle:horizontal {
margin-right: -5px;
background: rgb(0,115,170);
}
QScrollBar::handle:horizontal:hover {
background: rgb(0,115,170);
}


QScrollBar:vertical {
background: white;
width: 15px;
margin: 22px 0 22px 0;
}
QScrollBar::handle:vertical {
background: rgb(0,115,170);
min-height: 20px;
}

QScrollBar::up-arrow:vertical {
image: url(assets/UI/Icons/interface_icons/arrow_up.png);
width: 10px;
height: 10px;
}
QScrollBar::down-arrow:vertical {
image: url(assets/UI/Icons/interface_icons/arrow_down.png);
width: 10px;
height: 10px;
}
QScrollBar::sub-line:vertical {
background: rgb(0,115,170);
height: 20px;
subcontrol-position: top;
subcontrol-origin: margin;
}
QScrollBar::add-line:vertical {
background: rgb(0,115,170);
height: 20px;
subcontrol-position: bottom;
subcontrol-origin: margin;
}
QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
background: none;
}
QToolBar {
background: rgb(35,40,45);
spacing: 20;

}
QToolBar:separator
{
background: rgb(80, 80, 80);
height: 2;
}
QToolButton
{
color: rgb(255, 255, 255);
background:rgb(35,40,45);
}

QToolButton:hover,QToolButton:pressed
{
background-color: rgb(64, 73, 82);
}

QMessageBox QLabel
{
color: red;
}
"""
