module WriteToMaster(
    input SLK,
    input CS,
	 input bit7,
	 input bit6,
	 input bit5,
	 input bit4,
	 input bit3,
	 input bit2,
	 input bit1,
	 input bit0,
    output reg MISO
    
);
wire [7:0] bits;

assign bits[7] = bit0;
assign bits[6] = bit1;
assign bits[5] = bit2;
assign bits[4] = bit3;
assign bits[3] = bit4;
assign bits[2] = bit5;
assign bits[1] = bit6;
assign bits[0] = bit7;

reg [2:0] counter;


always @ (posedge SLK & CS) begin
		MISO <= bits[counter];
		counter<=counter+3'b001;
end 

endmodule