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
    file_name = Get_specified_field("ls *.map")
    field_prog = 'PROGRAM_FLASH'

    prog_start_addr = Get_specified_field("""
    cat {} | grep __top_PROGRAM_FLASH | cut -d '=' -f 2 | awk '{{$1=$1}};1'
    """.format(file_name))

    prog_end_addr= 'TBD'
    prog_size= 'TBD'
    prog_free= 'TBD'
    prog_used= 'TBD'
    prog_usage= 'TBD'

    allure.attach(f"""<head></head><body> XMicro1 Memory Map Table
        </body>
        <h1>Data acquired from *.map</h1>
        <table  style="border:3px #cccccc solid;" width="400" cellpadding="10" border='1'>
          <tr>
            <th width="200">Region</th>
            <th width="200">Start address</th>
            <th width="200">End address</th>
            <th width="200">Size</th>
            <th width="200">Free</th>
            <th width="200">Used</th>
            <th width="200">Usage</th>
          </tr>
          <tr align="center">
            <td width="200">{field_prog}</th>
            <td width="200">{prog_start_addr}</th>
            <td width="200">{prog_end_addr}</th>
            <td width="200">{prog_size}</th>
            <td width="200">{prog_free}</th>
            <td width="200">{prog_used}</th>
            <td width="200">{prog_usage}</th>         
          </tr>
        </table>""", '擷取build code後的文檔數據', allure.attachment_type.HTML)
