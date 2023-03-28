from myhdl import Signal, ResetSignal, intbv
from Encoder.model import encoder
def convert_encoder(hdl):

    clk = Signal(bool(0))
    rst = ResetSignal(0,active = 0,isasync =True)
    in_bit = Signal(bool(0))
    x_encoded = Signal(intbv(0)[2:])

    encd = encoder(clk , rst , in_bit ,x_encoded)
    encd.convert(hdl=hdl)

convert_encoder(hdl ='Verilog')


