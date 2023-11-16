module SPIlave(
    input SLK,
    input MOSI,
    input CS,
    output wire MISO,
    output reg [3:0] LED,
    output wire [6:0] display,
    output wire Velocidad
);

reg bit7;
reg bit6;
reg bit5;
reg bit4;
reg bit3;
reg bit2;
reg bit1;
reg bit0;


wire [19:0] din;
wire [19:0] clk;
assign din = ~clk;

divideClock div0(.clk(SLK), .d(din[0]), .q(clk[0]));
divideClock div1(.clk(clk[0]), .d(din[1]), .q(clk[1]));
divideClock div2(.clk(clk[1]), .d(din[2]), .q(clk[2]));
divideClock div3(.clk(clk[2]), .d(din[3]), .q(clk[3]));
divideClock div4(.clk(clk[3]), .d(din[4]), .q(clk[4]));
divideClock div5(.clk(clk[4]), .d(din[5]), .q(clk[5]));
divideClock div6(.clk(clk[5]), .d(din[6]), .q(clk[6]));
divideClock div7(.clk(clk[6]), .d(din[7]), .q(clk[7]));
divideClock div8(.clk(clk[7]), .d(din[8]), .q(clk[8]));
divideClock div9(.clk(clk[8]), .d(din[9]), .q(clk[9]));
divideClock div10(.clk(clk[9]), .d(din[10]), .q(clk[10]));
divideClock div11(.clk(clk[1]), .d(din[11]), .q(clk[11]));
divideClock div12(.clk(clk[11]), .d(din[12]), .q(clk[12]));
divideClock div13(.clk(clk[12]), .d(din[13]), .q(clk[13]));
divideClock div14(.clk(clk[13]), .d(din[14]), .q(clk[14]));
divideClock div15(.clk(clk[14]), .d(din[15]), .q(clk[15]));
divideClock div16(.clk(clk[15]), .d(din[16]), .q(clk[16]));
divideClock div17(.clk(clk[16]), .d(din[17]), .q(clk[17]));
divideClock div18(.clk(clk[17]), .d(din[18]), .q(clk[18]));
divideClock div19(.clk(clk[18]), .d(din[19]), .q(clk[19]));




PWM_module pwm1(.Porcentaje(LED), .SLK(clk[2]), .pwm(Velocidad));

BCD_module bdc1(.A(LED[3]), .B(LED[2]), .C(LED[1]), .D(LED[0]), .display(display));

WriteToMaster wtm(.SLK(SLK), .CS(CS), .bit7(bit7), .bit6(bit6), .bit5(bit5), .bit4(bit4), .bit3(bit3), .bit2(bit2), .bit1(bit1), .bit0(bit0), .MISO(MISO)); 

always @ (posedge SLK & !CS) begin
    bit7 <= bit6;
    bit6 <= bit5;
    bit5 <= bit4;
    bit4 <= bit3;
    bit3 <= bit2;
    bit2 <= bit1;
    bit1 <= bit0;
    bit0 <= MOSI;
    
    LED[0] <= bit0;
    LED[1] <= bit1;
    LED[2] <= bit2;
    LED[3] <= bit3;
end

endmodule


		