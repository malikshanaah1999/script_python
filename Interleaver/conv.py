from myhdl import Signal, ResetSignal, intbv
from model import interleaver


def convert_interleaver(hdl):

    Input= Signal(bool(0))
    Reset= ResetSignal(0,active = 0,isasync =True)
    Clock= Signal(bool(0))
    Output= Signal(bool(0))

    inter = interleaver(Input , Reset , Clock ,Output)
    inter.convert(hdl=hdl)

convert_interleaver(hdl ='Verilog')


