


from myhdl import *
from model import scrambler

def convert_encoder(hdl):

    din = Signal(intbv(0)[7:])
    dout = Signal(intbv(0)[7:])
    reset= ResetSignal(0,active = 0,isasync =True)
    clk = Signal(bool(0))

    encd = scrambler(din, dout,clk, reset)
    encd.convert(hdl=hdl)

convert_encoder(hdl ='Verilog')
