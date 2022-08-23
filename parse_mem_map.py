# Author: lindafang
# Date: 2020-10-05 15:00
# File: test_attach_html_png.py
import allure
import os

def Get_specified_field(cmd_str):
    result = os.popen(cmd_str)
    field_str = ""
    # 返回的结果是一个<class 'os._wrap_close'>对象，需要读取后才能处理
    context = result.read()
    #print("\n" + context + "sad")
    #return (context)
    for line in context.splitlines():
        field_str = line
        break
        #print(line)
    result.close()
    print("\n" + field_str)
    return field_str

def test_multiple_attachments():
    #result = os.popen("cat XMicro1_baremetal_v1.0.0.map | grep __top_PROGRAM_FLASH | cut -d '=' -f 2")
    # 返回的结果是一个<class 'os._wrap_close'>对象，需要读取后才能处理
    #context = result.read()
    #print(context)
    field_name = Get_specified_field("ls *.map")

    field_prog = Get_specified_field("""
    cat {} | grep __top_PROGRAM_FLASH | cut -d '=' -f 2 | awk '{{$1=$1}};1'
    """.format(field_name))
    #cat {} | grep __top_PROGRAM_FLASH | cut -d '=' -f 2 | awk '{$1=$1};1'
    #for line in context.splitlines():
    #   print(line)
    #result.close()

    varTest= '100'
    #allure.attach.file('1.jpg', attachment_type=allure.attachment_type.JPG)
    #allure.attach.file('2.yaml', attachment_type=allure.attachment_type.YAML)
    allure.attach("""<head></head><body> 这是个网页说明
        </body>
        <h1>文檔數據擷取</h1>
        <table  style="border:3px #cccccc solid;" width="400" cellpadding="10" border='1'>
          <tr>
            <th width="200">名字</th>
            <th width="200">年齡</th>
          </tr>
          <tr align="center">
            <td width="200">{}</th>
            <td width="200">{}</th>
          </tr>
        </table>""".format(field_prog, varTest), '擷取build code後的文檔數據', allure.attachment_type.HTML)
