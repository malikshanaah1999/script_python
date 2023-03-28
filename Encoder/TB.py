import random
from myhdl import block, instance, delay, Signal, intbv, StopSimulation, concat

from Encoder.model import encoder

@block
def testbench():
    clk = Signal(bool(0))
    rst = Signal(bool(1))
    in_bit = Signal(bool(0))
    x_encoded = [Signal(bool(0)), Signal(bool(0))]


    encoder_1 = encoder(clk, rst, in_bit, x_encoded)

    @instance
    def clk_gen():
        while True:
            clk.next = not clk
            yield delay(5)

    @instance
    def stimulus():
        yield delay(10)
        for i in range(10):
            in_bit.next = bool(random.getrandbits(1))
            yield delay(10)

        raise StopSimulation

    @instance
    def monitor():
        yield delay(10)
        for i in range(10):
            x = concat(x_encoded[1], x_encoded[0])
            print("in_bit = {}, x_encoded = {}".format(int(in_bit), bin(x)))
            yield delay(10)

        raise StopSimulation

    return encoder_1, clk_gen, stimulus, monitor

tb = testbench()
tb.run_sim()
