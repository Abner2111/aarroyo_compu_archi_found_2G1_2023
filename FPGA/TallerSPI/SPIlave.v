module SPIlave(
    input SLK,
    input MOSI,
    input CS,
    output reg MISO,
    output reg [3:0] LED,
    output [6:0] display,
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


PWM_module pwm1(.Porcentaje(LED), .SLK(SLK), .Velocidad(Velocidad));

BCD_module bdc1(LED[3], LED[2], LED[1], LED[0], display);

always @ (posedge SLK) begin
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
    
    MISO <= bit7 & CS;
    
end

endmodule


		