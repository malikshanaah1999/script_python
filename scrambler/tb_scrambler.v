module tb_scrambler;

reg [6:0] din;
wire [6:0] dout;
reg clk;
reg reset;

initial begin
    $from_myhdl(
        din,
        clk,
        reset
    );
    $to_myhdl(
        dout
    );
end

scrambler dut(
    din,
    dout,
    clk,
    reset
);

endmodule
