#coding=utf-8
import sys
# sys.path.append(r'D:\\Pycharm_workspace\\coding-269')
from util.excel_util import ExcelUtil
from keywordselenium.actionMethod import ActionMethod
class KeywordCase:
    def run_main(self):
        self.action_method = ActionMethod()       
        handle_excel = ExcelUtil('D:\\Pycharm_workspace\\coding-269\\config\\keyword.xls')
        #case行数
        case_lines = handle_excel.get_lines()
        if case_lines:
            for i in range(1,case_lines):
                #i行3列单元格数据
                is_run = handle_excel.get_col_value(i,3)
                if is_run == 'yes':
                    except_result_method = handle_excel.get_col_value(i,7)
                    print("lala",except_result_method)
                    except_result = handle_excel.get_col_value(i,8)
                    print(except_result)
                    method = handle_excel.get_col_value(i,4)
                    print(method)
                    send_value = handle_excel.get_col_value(i,5)
                    print(send_value)
                    handle_value = handle_excel.get_col_value(i,6)
                    print(handle_value)
                    self.run_method(method,send_value,handle_value)
                    #有值不为空
                    if except_result != '':
                        #返回切割后的值，list  ['element', 'password_error']
                        except_value = self.get_except_result_value(except_result)
                        print(except_value)
                        if except_value[0] == 'text':
                            result = self.run_method(except_result_method)
                            print(result)
                            if except_value[1] in result:
                                handle_excel.write_value(i,'pass')
                            else:
                                handle_excel.write_value(i,'fail')
                        elif except_value[0] == 'element':
                            result = self.run_method(except_result_method,except_value[1])
                            print(result)
                            if result:
                                handle_excel.write_value(i,'pass')
                            else:
                                handle_excel.write_value(i,'fail')
                        else:
                            print("没有else")
                    else:
                        print('预期结果为空')
                    


                        
    #获取预期结果值
    def get_except_result_value(self,data):
        return data.split('=')

    def run_method(self,method,send_value='',handle_value=''):
        '''

        :param method: 执行方法
        :param send_value:输入的数据
        :param handle_value:操作元素
        :return:
        '''
        #执行action_method里的某个函数
        method_value = getattr(self.action_method,method)
        if send_value == '' and handle_value !='':
            result = method_value(handle_value)
        elif send_value == '' and handle_value =='':
            result = method_value()
        elif send_value != '' and handle_value =='':
            result = method_value(send_value)
        else:
            result = method_value(send_value,handle_value)
        return result

if __name__ == '__main__':
    # data="element=password_error"
    # test = KeywordCase().get_except_result_value(data)
    # print(test)
    test = KeywordCase()
    test.run_main()