from random import random

from myhdl import block,always_comb, Signal, intbv, always,delay



from scrambler.model import scrambler


@block
def test_scrambler():

    din = Signal(intbv(0)[8:])
    dout = Signal(intbv(0)[8:])
    reset = Signal(bool(0))

    # Instantiate the scrambler block
    dut = scrambler(din=din, dout=dout, reset=reset)

    @always_comb
    def stimulus():
        # Generate random input data
        din.next = intbv(int(2 ** 8 * random()), min=0, max=256)

    @always_comb
    def monitor():
        # Print the input and output values
        print("Input = {}, Output = {}".format(din, dout))

    @always(delay(10))
    def reset_process():
        reset.next = True
        yield delay(5)
        reset.next = False

    return dut, stimulus, monitor, reset_process



