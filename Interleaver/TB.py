from myhdl import *
from random import randrange
from Interleaver.model import interleaver
def test_interleaver():
    Input, Reset, Clock, Output = [Signal(intbv(0)[16:]) for i in range(4)]
    dut = interleaver(Input, Reset, Clock, Output)

    HALF_PERIOD = delay(10)

    @always(HALF_PERIOD)
    def clock_generator():
        Clock.next = not Clock

    @instance
    def stimulus():
        Reset.next = 1
        yield Clock.posedge
        Reset.next = 0

        for i in range(48):
            Input.next = randrange(2**16)
            yield Clock.posedge

        # Wait for the last output to be valid
        yield Clock.posedge
        yield Clock.posedge

        raise StopSimulation

    return dut, clock_generator, stimulus

tb = traceSignals(test_interleaver)
sim = Simulation(tb)
sim.run()
