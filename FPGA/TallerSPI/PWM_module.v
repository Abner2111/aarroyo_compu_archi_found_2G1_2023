module PWM_module (
	input [3:0] Porcentaje,
	input SLK,
   output reg Velocidad
   
);


reg [3:0] numero_cliclos;

reg [3:0] counter; //0-9

reg maxCont;

reg completed;

reg [3:0] comparison;


initial begin
		numero_cliclos <= 10;
end




	always @ (posedge SLK) begin
	
		counter <= counter + 4'b0001;
		
		Velocidad <= Porcentaje > counter;
	
      comparison <= ~(counter ^ numero_cliclos); //cuando sean iguales b'1111

		completed <= comparison[0] & comparison[1] & comparison[2] & comparison[3]; //cuando comparison es 1111 completed 1

		counter <= counter + 4'b0001 &  completed + 4'b0001 &  completed + 4'b0001 & completed + 4'b0001 &  completed+ 4'b0001 &  completed;
   end 
	
	//assign Velocidad = velo1;

endmodule 
