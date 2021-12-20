import sys
import os
import datetime
import time
import json
import csv

import openpyxl

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QTreeWidgetItem, QMessageBox,QProgressDialog,QProgressBar

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True) #enable highdpi scaling
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True) #use highdpi icons

from ChannelTool.window import Ui_MainWindow
from ChannelTool.station_spyder import crawl

# proxies = {
#     "http": "http://127.0.0.1:1082",
#     "https": "http://127.0.0.1:1082"
# }
proxies = None


class UiMain(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(UiMain, self).__init__(parent)
        self.setupUi(self)
        self.component_list = {}
        self.currStationIndex=-1
        self.stations=[]
        self.progressDialog=None
        self.hasData=False
        self.crawl_btn.setEnabled(False)
        self.crawl_btn.setStyleSheet('font: 10pt "Microsoft YaHei UI";background-color:#455ab3;color:#fff;')

        self.bind_signal()



    def bind_signal(self):
        self.read_excel_btn.clicked.connect(self.read_excel_btn_clicked)
        self.crawl_btn.clicked.connect(self.crawl_btn_clicked)
        self.next_btn.clicked.connect(self.next_btn_clicked)
        self.prior_btn.clicked.connect(self.prior_btn_clicked)
        #self.treeWidget.itemClicked.connect(self.tree_item_clicked)
        self.listWidget.itemClicked.connect(self.station_item_clicked)
        self.treeWidget.itemChanged.connect(self.channelSelectionChanged)
        self.save_btn.clicked.connect( self.save_btn_clicked )
        self.export_cmp_btn.clicked.connect(self.export_cmp_btn_clicked)
        self.load_btn.clicked.connect(self.load_btn_clicked)

    def export_cmp_btn_clicked(self):
        fileName_choose, filetype = QtWidgets.QFileDialog.getSaveFileName(self, "导出台站信息", "",
                                                                          "csv Files (*.csv;)")
        if fileName_choose == "":
            return
        self.export_cmp_data(fileName_choose)
    def channelSelectionChanged(self,item, col):

        print("item changed:  "+str(datetime.datetime.now()) +item.text(0))
        parent_list=self.getItemParents(item)
        if len(parent_list)!=4:
             return
        #self.updateChannelStatus(item, parent_list)

    def getItemParents(self,item):

        result=[]
        while item.parent():
            result.insert(0, item.text(0))
            item = item.parent()
        result.insert(0, item.text(0))

        return result

    def updateChannelStatus(self, item,parent_list):
        data=self.stations[self.currStationIndex]["data"]
        for key in  parent_list:
            data=data[key]

        data["selected"]=item.checkState(0)

    def read_excel_btn_clicked(self):

        filename, filetype = QtWidgets.QFileDialog.getOpenFileName(self, "选取文件", os.getcwd(), "Execl Files (*.xlsx;*.xls)")  # 设置文件扩展名过滤,用双分号间隔

        if filename == "":
            return
        # 重置软件状态
        self.reset_data()
        self.excel_path_edit.setText(filename)
        # 解析excel文件
        self.parse_excel(filename)
        # 填充listWidget
        self.listWidget.clear()
        for station in self.stations:
            self.listWidget.addItem(str(station['network'] + '/' + station['name']))

    def crawl_btn_clicked(self):
        self.crawl()
        self.hasData=True
        self.currStationIndex=0
        self.listWidget.setCurrentRow(self.currStationIndex)
        self.update_tree()


    def keyPressEvent(self, *args, **kwargs):

        key = args[0].key()
        if key == Qt.Key_A and QApplication.keyboardModifiers() == Qt.ControlModifier:
            self.prior_btn_clicked()
        elif key == Qt.Key_D and QApplication.keyboardModifiers() == Qt.ControlModifier:
            self.next_btn_clicked()

    # 解析excel
    def parse_excel(self, file_path):
        # 清除原有数据
        self.stations = []

        # 打开上传 excel 表格
        wb = openpyxl.load_workbook(file_path)
        # 打开文件
        sheet_1 = wb.worksheets[0]  # 根据sheet页的排序选取sheet

        for i in range(2, sheet_1.max_row+1):
            station_name = sheet_1.cell(i, 1).value
            network = sheet_1.cell(i, 2).value
            start_time = sheet_1.cell(i, 3).value
            end_time = sheet_1.cell(i, 4).value
            if not station_name or not network:
                continue
            self.stations.append({
                'name': station_name,
                'network': network,
                'start_time': start_time,
                'end_time': end_time,
                'data': None,
                'select_item': []
            })

        self.crawl_btn.setEnabled(True)
        self.currStationIndex=0


    def crawl(self):
        if not self.stations:
            QMessageBox.warning(self, "警告", "还没有台站数据",QMessageBox.Ok)
            return

        self.progressDialog = QProgressDialog("爬取进行中，请耐心等待...", "取消", 0, 100, self)
        self.progressDialog.setWindowTitle("爬取进度")
        self.progressDialog.setMinimumSize(240,60)
        #self.progress.setContent("进度", "数据爬取中，请耐心等待")

        self.progressDialog.open()
        QApplication.processEvents()

        for index, station in enumerate(self.stations):
            time.sleep(5)
            station['data'] = crawl(station['name'], station['network'], station['start_time'], station['end_time'], proxies)
            progress_value = (index + 1) / len(self.stations) * 100
            self.progressDialog.setValue(int(progress_value))

            QApplication.processEvents()

        self.progressDialog.hide()

        return


    def next_btn_clicked(self):
        if not self.hasData:
            QMessageBox.warning(self, "警告", "没有台站工作时间数据，请先爬取",QMessageBox.Ok)
            return

        if self.currStationIndex == len(self.stations)-1 :
            QMessageBox.warning(self,"警告", "已经是最后一个台站了", QMessageBox.Ok)
            return

        self.currStationIndex = self.currStationIndex + 1

        self.listWidget.setCurrentRow(self.currStationIndex)
        self.update_index_lable()
        self.desc_label.setText('network: ' + self.stations[self.currStationIndex]['network'] + '\n' + 'station: ' +
                                self.stations[self.currStationIndex]['name'])

        self.update_tree()

    def prior_btn_clicked(self):
        if not self.hasData:
            QMessageBox.warning(self, "警告", "没有台站工作时间数据，请先爬取",QMessageBox.Ok)
            return
        if self.currStationIndex == 0:
            QMessageBox.warning(self, "警告", "已经是第一个台站了", QMessageBox.Ok)
            return
        self.component_select_status()
        self.currStationIndex = self.currStationIndex - 1
        self.listWidget.setCurrentRow(self.currStationIndex)

        self.desc_label.setText('network: ' + self.stations[self.currStationIndex]['network'] + '\n' + 'station: ' +
                                self.stations[self.currStationIndex]['name'])
        item = self.stations[self.currStationIndex]

        self.update_tree()

    def component_select_status(self):
        select_item = []
        for key, item in self.component_list.items():
            if item.checkState(0) == Qt.Checked:
                select_item.append(key)

        #self.stations[self.currStationIndex]['select_item'] = select_item
        # 修改list颜色
        if select_item:
            item = self.listWidget.item(self.currStationIndex)
            if item:
                item.setBackground(QtGui.QColor('cyan'))

    def export_cmp_data(self, filename):

        with open(filename, 'w', newline='') as csvfile:
            w = csv.writer(csvfile)
            header = ('network', 'name', 'start_time', 'end_time', 'latitude', 'longitude', 'elevation', 'components', 'location_code')
            w.writerow(header)

            row_list = []
            # 相同设备下同赫兹分量合并
            for station in self.stations:
                merge_dict = {}
                for key in station['select_item']:
                    block_index, location, device_name, hertz, c = key.split('||')
                    key = '||'.join([block_index, location, device_name, hertz])
                    if key not in merge_dict.keys():
                        merge_dict[key] = []
                    merge_dict[key].append(c)
                for key, cha_list in merge_dict.items():
                    block_index, location, device_name, hertz = key.split('||')
                    description = station['data'][int(block_index)]['description']
                    row = (station['network'], station['name'], station['start_time'].split('T')[0], station['end_time'].split('T')[0], str(description['latitude']), str(description['longitude']),
                           str(description['elevation']), ' '.join(cha_list), str(location))
                    row_list.append(row)

            for row in row_list:
                w.writerow(row)


    def update_tree(self):
        self.treeWidget.clear()
        data = self.stations[self.currStationIndex]['data']
        self.component_list.clear()
        # 设置列数
        self.treeWidget.setColumnCount(1)
        # 设置树形控件头部的标题
        self.treeWidget.setHeaderLabels(['节点'])
        for index, content in enumerate(data):
            block = QTreeWidgetItem(self.treeWidget)
            block_text = 'TimePeriod_' + str(index) + '     ' + content['description']['start'] + '   ' + \
                         content['description']['end']
            block.setText(0, block_text)
            #block.setToolTip(0, )
            # locations节点
            for location, device_list in content['locations'].items():
                loc = QTreeWidgetItem(block)
                loc_text = 'location:  ' + location
                loc.setText(0, loc_text)
                # 设备节点
                for device_name, cha_list in device_list.items():
                    device = QTreeWidgetItem(loc)
                    device_text = 'Device:  ' + device_name
                    device.setText(0, device_text)
                    # 频率节点
                    for hertz, cha in cha_list.items():
                        if len(content['locations']) == 1 and len(device_list) == 1 and len(cha_list) == 1:
                            auto_check = True
                        else:
                            auto_check = False
                        hz = QTreeWidgetItem(device)
                        hz.setText(0, hertz)
                        hz.setFlags(hz.flags() | Qt.ItemIsUserCheckable|Qt.ItemIsAutoTristate)
                        #hz.setCheckState(0, Qt.Unchecked)
                        # 分量节点
                        for c in cha.keys():
                            ch = QTreeWidgetItem(hz)
                            ch.setText(0, c)
                            component_key = '||'.join([str(index), location, device_name, hertz, c])
                            if component_key in self.stations[self.currStationIndex]['select_item']:
                                ch.setCheckState(0, Qt.Checked)
                            elif not self.stations[self.currStationIndex]['select_item'] and auto_check is True:
                                ch.setCheckState(0, Qt.Checked)
                            else:
                                ch.setCheckState(0, Qt.Unchecked)
                            self.component_list[component_key] = ch

        self.treeWidget.expandAll()

    def save_btn_clicked(self):
        if not self.hasData:
            QMessageBox.warning(self, "警告", "没有台站工作时间数据，请先爬取",QMessageBox.Ok)
            return

        # 选择路径与文件名

        fileName_choose, filetype = QtWidgets.QFileDialog.getSaveFileName(self, "保存台站信息", os.path.join(os.getcwd(), 'stations.json'),  "json Files (*.json;)")
        if fileName_choose == "":
            return
        # 保存文件
        self.component_select_status()
        self.save_stations(fileName_choose)

    def save_stations(self,fname):
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(json.dumps(self.stations))
        return

    def load_btn_clicked(self):
        '''
        加载已经下好的数据
        :return:
        '''

        fileName_choose, filetype = QtWidgets.QFileDialog.getOpenFileName(self, "选取文件", os.getcwd(), "Json File (*.json)")
        if fileName_choose == "":
            return

        # 重置软件状态
        self.reset_data()
        with open(fileName_choose, 'r') as f:
            self.stations = json.loads(f.read())
            self.excel_path_edit.setText(fileName_choose)
            # 填充listWidget
            self.listWidget.clear()
            for station in self.stations:
                self.listWidget.addItem(str(station['network'] + '/' + station['name']))
            # self.next()
        self.hasData=True
        self.desc_label.setText('network: ' + self.stations[self.currStationIndex]['network'] + '\n' + 'station: ' +
                                self.stations[self.currStationIndex]['name'])
        self.currStationIndex=0
        self.listWidget.setCurrentRow(self.currStationIndex)
        self.update_tree()
        self.update_index_lable()
        self.component_select_status()

    def update_index_lable(self):
        select_number = len([station['select_item'] for station in self.stations if station['select_item']])
        self.index_label.setText(str(select_number) + '/' + str(len(self.stations)))

    def station_item_clicked(self, item):

        curr_index = self.listWidget.currentRow()
        if not self.hasData:
            QMessageBox.warning(self, "警告", "没有台站工作时间数据，请先爬取",QMessageBox.Ok)
            return
        if curr_index == self.currStationIndex:
            return

        self.component_select_status()
        self.currStationIndex = curr_index
        self.update_index_lable()
        self.desc_label.setText('network: ' + self.stations[self.currStationIndex]['network'] + '\n' + 'station: ' +
                                self.stations[self.currStationIndex]['name'])

        self.update_tree()

    def reset_data(self):
        self.stations.clear()

        self.currStationIndex = -1
        self.component_list = {}

    def tree_item_clicked(self, item, col):
        item = self.treeWidget.currentItem()
        # 判断层级
        item_text = item.text(0)
        all_check = False  # 是全选，还是全部取消
        if 'block_' in item_text:
            location_list = [item.child(i) for i in range(item.childCount())]
            for location in location_list:
                device_list = [location.child(i) for i in range(location.childCount())]
                for device in device_list:
                    hertz_list = [device.child(i) for i in range(device.childCount())]
                    for hertz in hertz_list:
                        cha_list = [hertz.child(i) for i in range(hertz.childCount())]
                        for cha in cha_list:
                            if cha.checkState(0) == Qt.Unchecked:
                                # 如果出现一个未选中的，则全选
                                all_check = True
                                break
                        for cha in cha_list:
                            if all_check:
                                cha.setCheckState(0, Qt.Checked)
                            else:
                                cha.setCheckState(0, Qt.Unchecked)
        elif 'location:' in item_text:
            device_list = [item.child(i) for i in range(item.childCount())]
            for device in device_list:
                hertz_list = [device.child(i) for i in range(device.childCount())]
                for hertz in hertz_list:
                    cha_list = [hertz.child(i) for i in range(hertz.childCount())]
                    for cha in cha_list:
                        if cha.checkState(0) == Qt.Unchecked:
                            # 如果出现一个未选中的，则全选
                            all_check = True
                            break
                    for cha in cha_list:
                        if all_check:
                            cha.setCheckState(0, Qt.Checked)
                        else:
                            cha.setCheckState(0, Qt.Unchecked)
        elif 'Device:' in item_text:
            hertz_list = [item.child(i) for i in range(item.childCount())]
            for hertz in hertz_list:
                cha_list = [hertz.child(i) for i in range(hertz.childCount())]
                for cha in cha_list:
                    if cha.checkState(0) == Qt.Unchecked:
                        # 如果出现一个未选中的，则全选
                        all_check = True
                        break
                for cha in cha_list:
                    if all_check:
                        cha.setCheckState(0, Qt.Checked)
                    else:
                        cha.setCheckState(0, Qt.Unchecked)
        elif 'Hz' in item_text:
            cha_list = [item.child(i) for i in range(item.childCount())]
            for cha in cha_list:
                if cha.checkState(0) == Qt.Unchecked:
                    # 如果出现一个未选中的，则全选
                    all_check = True
                    break
            for cha in cha_list:
                if all_check:
                    cha.setCheckState(0, Qt.Checked)
                else:
                    cha.setCheckState(0, Qt.Unchecked)
        else:
            if item.checkState(0) == Qt.Checked:
                item.setCheckState(0, Qt.Unchecked)
            elif item.checkState(0) == Qt.Unchecked:
                item.setCheckState(0, Qt.Checked)
        return

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = UiMain()
    ui.show()
    sys.exit(app.exec_())
