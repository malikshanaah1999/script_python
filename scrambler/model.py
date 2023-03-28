from myhdl import block, always_seq, Signal, intbv, always_comb


@block
def scrambler(din, dout, clk, reset):
    state = Signal(intbv(0)[7:])
    feedback = (state[6] ^ state[3])
    temp = (state[6]^ state[5]^ state[4]^state[3]^ state[2]^ state[1]^feedback)
    dout_reg = Signal(intbv(0)[len(dout):])

    @always_seq(clk.posedge, reset=reset)
    def scramble_logic():
        if reset:
            state.next = intbv(0x7F)[7:]
        else:
            state.next = temp
        dout_reg.next = dout_reg.val

    @always_comb
    def output_logic():
        dout.next = dout_reg

    return scramble_logic, output_logic
