from Operations import Calc_block as Calc
from Logger import result_logger as write_log
import Transformation as Trans
import Start

def button_click():
    j = Trans.data_formatting(Start.input_data())
    calc_result = Calc(j)
    Start.view_data(calc_result, 'Ответ')
    write_log(j, calc_result)

button_click()
