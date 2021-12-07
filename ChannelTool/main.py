import sys
import os
import datetime
import time
import json
import csv

import xlrd
import xlwt
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush
from PyQt5.QtWidgets import QMainWindow, QApplication, QTreeWidgetItem, QMessageBox

from ChannelTool.window import Ui_MainWindow
from ChannelTool.myMessage import MyMessageBox
from ChannelTool.station_spyder import crawl
from ChannelTool.myProgress import MyProgress

# proxies = {
#     "http": "http://127.0.0.1:1082",
#     "https": "http://127.0.0.1:1082"
# }
proxies = None


class UiMain(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(UiMain, self).__init__(parent)
        self.setupUi(self)
        self.excel_data = []
        self.component_list = {}
        self.item_index = -1
        self.crawl_status = False
        self.bing_signal()
        self.progress = MyProgress()

    def bing_signal(self):
        self.upload_excel_btn.clicked.connect(self.choose_excel)
        self.crawl_btn.clicked.connect(self.crawl)
        self.next_btn.clicked.connect(self.next)
        self.prior_btn.clicked.connect(self.prior)
        self.treeWidget.itemClicked.connect(self.tree_item_clicked)
        self.listWidget.itemClicked.connect(self.list_item_clicked)
        self.save_btn.clicked.connect(self.save_clicked)
        self.reload_btn.clicked.connect(self.reload_clicked)


    def keyPressEvent(self, *args, **kwargs):
        key = args[0].key()
        if key == Qt.Key_A and QApplication.keyboardModifiers() == Qt.ControlModifier:
            self.prior()
        elif key == Qt.Key_D and QApplication.keyboardModifiers() == Qt.ControlModifier:
            self.next()

    def choose_excel(self):
        if self.crawl_status:
            message_box = MyMessageBox()
            message_box.setContent("请等待", "请等待数据读取完成")
            message_box.exec_()
            return
        fileName_choose, filetype = QtWidgets.QFileDialog.getOpenFileName(self,
                                                                          "选取文件",
                                                                          os.getcwd(),  # 起始路径
                                                                          "Execl Files (*.xlsx;*.xls)")  # 设置文件扩展名过滤,用双分号间隔

        if fileName_choose == "":
            return
        # 重置软件状态
        self.reset_data()

        self.excel_path_edit.setText(fileName_choose)
        # 解析excel文件
        self.parse_excel(fileName_choose)
        # 填充listWidget
        self.listWidget.clear()
        for item in self.excel_data:
            self.listWidget.addItem(str(item['network'] + '/' + item['station']))

    # 解析excel
    def parse_excel(self, file_path):
        # 清除原有数据
        self.excel_data = []

        # 打开上传 excel 表格
        file = xlrd.open_workbook(file_path)
        # 打开文件
        sheet_1 = file.sheet_by_index(0)  # 根据sheet页的排序选取sheet
        row_content = sheet_1.row_values(0)  # 获取指定行的数据，返回列表，排序自0开始
        row_number = sheet_1.nrows  # 获取有数据的最大行
        for i in range(1, row_number):
            station = sheet_1.cell(i, 0).value
            network = sheet_1.cell(i, 1).value
            start_time = sheet_1.cell(i, 2).value
            end_time = sheet_1.cell(i, 3).value
            self.excel_data.append({
                'station': station,
                'network': network,
                'start_time': start_time,
                'end_time': end_time,
                'data': None,
                'select_item': []
            })

        self.crawl_btn.setEnabled(True)
        self.crawl_btn.setStyleSheet('font: 10pt "Microsoft YaHei UI";background-color:#455ab3;color:#fff;')

    def crawl(self):
        if not self.excel_data:
            message_box = MyMessageBox()
            message_box.setContent("请选择", "请选择参数文件")
            message_box.exec_()
            return

        pass
        # 选择爬取结果保存路径
        info_name = 'crawl_info_' + datetime.datetime.now().strftime('%Y%m%d_%H%M') + '.json'
        reportname = os.path.join(os.getcwd(), info_name)
        fileName_choose, filetype = QtWidgets.QFileDialog.getSaveFileName(self,
                                                                          "保存文件",
                                                                          reportname,
                                                                          "csv Files (*.json;)")
        if fileName_choose == "":
            return

        self.crawl_status = True
        self.progress.setContent("进度", "数据爬取中")
        self.progress.setValue(1)
        self.progress.show()
        QApplication.processEvents()

        for index, item in enumerate(self.excel_data):
            time.sleep(5)
            item['data'] = crawl(item['station'], item['network'], item['start_time'], item['end_time'], proxies)
            progress_value = (index + 1) / len(self.excel_data) * 100
            self.progress.setValue(progress_value)
            self.progress.show()
            QApplication.processEvents()

        self.crawl_status = False
        self.progress.hide()
        # 保存数据
        # info_name = 'crawl_info_' + datetime.datetime.now().strftime('%Y%m%d_%H%M') + '.json'
        with open(fileName_choose, 'w', encoding='utf-8') as f:
            f.write(json.dumps(self.excel_data))

        self.next()

    def next(self):
        if not [item['data'] for item in self.excel_data if item['data'] is not None]:
            return
        if self.item_index >= len(self.excel_data) - 1:
            message_box = MyMessageBox()
            message_box.setContent("选择完成", "是否保存数据文件？")
            message_box.exec_()
            if message_box.reply == QMessageBox.Ok:
                # 选择路径与文件名
                reportname = os.path.join(os.getcwd(), 'report.csv')
                fileName_choose, filetype = QtWidgets.QFileDialog.getSaveFileName(self,
                                                                                  "导出文件",
                                                                                  reportname,  # 起始路径
                                                                                  "csv Files (*.csv;)")  # 设置文件扩展名过滤,用双分号间隔
                if fileName_choose == "":
                    return

                # 保存文件
                self.component_select_status()
                self.report_file(fileName_choose)
            return

        self.component_select_status()
        self.item_index = self.item_index + 1
        self.update_index_lable()
        self.desc_label.setText('network: ' + self.excel_data[self.item_index]['network'] + '\n' + 'station: ' +
                                self.excel_data[self.item_index]['station'])
        item = self.excel_data[self.item_index]
        self.updata_tree(item)

    def prior(self):
        if self.item_index <= 0:
            return
        self.component_select_status()
        self.item_index = self.item_index - 1
        self.update_index_lable()
        self.desc_label.setText('network: ' + self.excel_data[self.item_index]['network'] + '\n' + 'station: ' +
                                self.excel_data[self.item_index]['station'])
        item = self.excel_data[self.item_index]
        self.updata_tree(item)

    def component_select_status(self):
        select_item = []
        for key, item in self.component_list.items():
            if item.checkState(0) == Qt.Checked:
                select_item.append(key)
            else:
                pass
        self.excel_data[self.item_index]['select_item'] = select_item
        # 修改list颜色
        if select_item:
            item = self.listWidget.item(self.item_index)
            if item:
                item.setBackground(QtGui.QColor('cyan'))

    def report_file(self, filename):

        with open(filename, 'w', newline='') as csvfile:
            w = csv.writer(csvfile)
            header = ('network', 'name', 'start_time', 'end_time', 'latitude', 'longitude', 'elevation', 'components', 'location_code')
            w.writerow(header)

            row_list = []
            # 相同设备下同赫兹分量合并
            for item in self.excel_data:
                merge_dict = {}
                for key in item['select_item']:
                    block_index, location, device_name, hertz, c = key.split('||')
                    key = '||'.join([block_index, location, device_name, hertz])
                    if key not in merge_dict.keys():
                        merge_dict[key] = []
                    merge_dict[key].append(c)
                for key, cha_list in merge_dict.items():
                    block_index, location, device_name, hertz = key.split('||')
                    description = item['data'][int(block_index)]['description']
                    row = (item['network'], item['station'], item['start_time'].split('T')[0], item['end_time'].split('T')[0], str(description['latitude']), str(description['longitude']),
                           str(description['elevation']), ' '.join(cha_list), str(location))
                    # ['network', 'name', 'start_time', 'end_time', 'latitude', 'longitude', 'elevation', 'components', 'location_code']
                    # row = [item['station'], item['network'], item['start_time'], item['end_time'], location, hertz, ', '.join(cha_list)]
                    row_list.append(row)

            for row in row_list:
                w.writerow(row)




    def updata_tree(self, item):
        self.treeWidget.clear()
        data = item['data']
        self.component_list.clear()
        # 设置列数
        self.treeWidget.setColumnCount(1)
        # 设置树形控件头部的标题
        self.treeWidget.setHeaderLabels(['节点'])
        for index, content in enumerate(data):
            block = QTreeWidgetItem(self.treeWidget)
            block_text = 'block_' + str(index) + '     ' + content['description']['start'] + '   ' + \
                         content['description']['end']
            block.setText(0, block_text)
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
                        # 分量节点
                        for c in cha.keys():
                            ch = QTreeWidgetItem(hz)
                            ch.setText(0, c)
                            component_key = '||'.join([str(index), location, device_name, hertz, c])
                            if component_key in self.excel_data[self.item_index]['select_item']:
                                ch.setCheckState(0, Qt.Checked)
                            elif not self.excel_data[self.item_index]['select_item'] and auto_check is True:
                                ch.setCheckState(0, Qt.Checked)
                            else:
                                ch.setCheckState(0, Qt.Unchecked)
                            self.component_list[component_key] = ch

        self.treeWidget.expandAll()

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

    def save_clicked(self):
        if not self.excel_data:
            message_box = MyMessageBox()
            message_box.setContent("请选择", "请选择参数文件")
            message_box.exec_()
            return

        # 选择路径与文件名
        reportname = os.path.join(os.getcwd(), 'report.csv')
        fileName_choose, filetype = QtWidgets.QFileDialog.getSaveFileName(self,
                                                                          "导出文件",
                                                                          reportname,  # 起始路径
                                                                          "csv Files (*.csv;)")  # 设置文件扩展名过滤,用双分号间隔
        if fileName_choose == "":
            return

        # 保存文件
        self.component_select_status()
        self.report_file(fileName_choose)

    def reload_clicked(self):
        '''
        加载已经下好的数据
        :return:
        '''
        if self.crawl_status:
            message_box = MyMessageBox()
            message_box.setContent("请等待", "请等待数据读取完成")
            message_box.exec_()
            return
        fileName_choose, filetype = QtWidgets.QFileDialog.getOpenFileName(self,
                                                                          "选取文件",
                                                                          os.getcwd(),  # 起始路径
                                                                          "Json File (*.json)")  # 设置文件扩展名过滤,用双分号间隔

        if fileName_choose == "":
            return
        # 重置软件状态
        self.reset_data()

        with open(fileName_choose, 'r', encoding='utf-8') as f:
            # json_text = f.readline()
            excel_data = json.loads(f.readline())
            self.excel_data = excel_data
            self.excel_path_edit.setText(fileName_choose)
            # 填充listWidget
            self.listWidget.clear()
            for item in self.excel_data:
                self.listWidget.addItem(str(item['network'] + '/' + item['station']))
            self.next()


    def update_index_lable(self):
        select_number = len([item['select_item'] for item in self.excel_data if item['select_item']])
        self.index_label.setText(str(select_number) + '/' + str(len(self.excel_data)))

    def list_item_clicked(self, item):
        curr_index = self.listWidget.currentRow()
        if curr_index == self.item_index:
            return

        self.component_select_status()
        self.item_index = curr_index
        self.update_index_lable()
        self.desc_label.setText('network: ' + self.excel_data[self.item_index]['network'] + '\n' + 'station: ' +
                                self.excel_data[self.item_index]['station'])
        item = self.excel_data[self.item_index]
        self.updata_tree(item)

    def reset_data(self):
        self.excel_data.clear()
        self.crawl_status = False
        self.item_index = -1
        self.component_list = {}


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = UiMain()
    ui.show()
    sys.exit(app.exec_())
