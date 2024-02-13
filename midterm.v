module FlipFlop(clk, d, q, qbar);
  input d, clk;
  output reg q, qbar;
  always @(posedge clk)
    begin
      q = ~(d & q);
      qbar = ~q;
    end
endmodule

output [3:0] P;
wire S;
assign S[0] = a[0] and b[0];
assign P[0] = S[0] | a[0];

out = a | b;

//Cannot detect overflow

module Problem3 ( r , code , a c t i v e ) ;
    input [3:0] r ;
    output [1:0] code ;
    output active;
  always @(r)
  begin
    if (input != 4'b0000)
        active = 1;
    if (input[3] == 1)
        code = 2'b11;
    else if (input[2] == 1)
        code = 2'b10;
    else if (input[1] == 1)
        code = 2'b01;
    else
        code = 2'b00;
  end
endmodule

module shiftreg(data, clk, load, d, q) ;
  input data, clk, load;
  input [0:3] d;
  output [0:3] q;
  always @(data, posedge clk, load)
    begin name
      integer i;
      reg q_temp = data;
      for (i = 0; i < 4; i = i+1)
      begin
          shift_reg_cell(.a = d[i], .b = q_temp, .clk = clk, .load = load, .q = q_temp)
          q[i] = q_temp;
      end
endmodule

module shiftreg(data, clk, load, d, q) ;
  parameter N;
  input data, clk, load;
  input [0:3] d;
  output [0:3] q;
  always @(data, posedge clk, load)
    begin name
      integer i;
      reg q_temp = data;
      for (i = 0; i < N; i = i+1)
      begin
          shift_reg_cell(.a = d[i], .b = q_temp, .clk = clk, .load = load, .q = q_temp)
          q[i] = q_temp;
      end
endmodule
