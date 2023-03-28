from myhdl import *
from myhdl.conversion import toVerilog

@block
def interleaver(Input, Reset, Clock, Output):
    N_CBPS = 48
    N_COLS = 16
    N_ROWS = N_CBPS // 16

    j_col_IN = Signal(intbv(0)[4:])
    i_row_IN = Signal(intbv(0)[2:])
    MEM_IN = [Signal(intbv(0)[16:]) for i in range(N_ROWS)]
    j_col_OUT = Signal(intbv(0)[4:])
    i_row_OUT = Signal(intbv(0)[2:])
    MEM_OUT = [Signal(intbv(0)[16:]) for i in range(N_ROWS)]
    counter = Signal(intbv(1)[8:])

    @always_seq(Clock.posedge, reset=Reset)
    def interleaver_logic():
        if Reset:
            # Here is the initialization process
            j_col_IN.next = 0
            i_row_IN.next = 0
            for k in range(N_ROWS):
                MEM_IN[k].next = 0
            j_col_OUT.next = 0
            i_row_OUT.next = 0
            for k in range(N_ROWS):
                MEM_OUT[k].next = 0
            counter.next = 1
        else:
            counter.next = counter + 1
            if counter == N_CBPS:
                for k in range(N_ROWS):
                    MEM_OUT[k].next = MEM_IN[k]
                j_col_IN.next = 0
                i_row_IN.next = 0
                j_col_OUT.next = 0
                i_row_OUT.next = 0
                counter.next = 1
                MEM_OUT[i_row_IN][j_col_IN].next = Input
            else:
                MEM_IN[i_row_IN][j_col_IN].next = Input
                j_col_IN.next = j_col_IN + 1
                if j_col_IN == 15:
                    i_row_IN.next = i_row_IN + 1
                i_row_OUT.next = i_row_OUT + 1
                if i_row_OUT + 1 == N_ROWS:
                    j_col_OUT.next = j_col_OUT + 1
                    i_row_OUT.next = 0

    @always_comb
    def output_logic():
        Output.next = MEM_OUT[i_row_OUT][j_col_OUT]

    return interleaver_logic, output_logic
