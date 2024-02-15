`timescale 1ps/1ns
module tb_something();
    reg a, b;
    wire s;
    something instant(.a(a), .b(b), .s(s));
    begin
        
    end
endmodule

always @(a)
begin
    case(a):
        2'b01:
        2'b10:
        2'b11:
        default:
    endcase
end

        output reg [3:0] a;
        output reg [3:0] b [0:2];
parameter N = 2;
time delay = 200;
assign #delay a = b & c

genvar i;
generate
    for (i = 0; i < N; i = i + 1)
    begin
        s[i] or whatever;
    end
endgenerate

module clock(a);
output reg a;
initial
begin
    a = 0;
end
always
begin
    #10;
    a = ~a;
end
endmodule
