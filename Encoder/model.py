from myhdl import always, always_comb, Signal, intbv, block

@block
def encoder(clk, rst, in_bit, x_encoded):
    state = Signal(intbv(0)[7:])

    @always_comb
    def comb_logic():
        x_encoded[1].next = in_bit ^ state[6] ^ state[5] ^ state[3] ^ state[1]
        x_encoded[0].next = in_bit ^ state[1] ^ state[4] ^ state[3] ^ state[2]

    @always(clk.posedge, rst.negedge)
    def seq():
        if not rst:
            state.next = 0
        else:
            state[5:0].next = state[6:1]
            state[1:0].next = in_bit
    return seq, comb_logic

