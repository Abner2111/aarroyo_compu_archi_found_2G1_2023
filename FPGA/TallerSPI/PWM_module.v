module PWM_module (
	input [3:0] Porcentaje,
	input SLK,
   output reg pwm
   
);


//reg [3:0] numero_cliclos;

reg [3:0] counter; //0-9


//reg completed;

//reg [3:0] comparison;

reg [3:0] mappedInput;

initial begin
		
		//numero_cliclos <= 10;
		//counter <= 4'b0;
end




	always @ (posedge SLK) begin
	
		mappedInput <= Porcentaje + 4'b0100;
		pwm <= mappedInput > counter;
		counter <= counter + 4'b0001;
      //comparison <= ~(counter ^ 4'b1010); //cuando sean iguales b'1111
		
		

		//completed <= comparison[0] & comparison[1] & comparison[2] & comparison[3]; //cuando comparison es 1111 completed 1
		//counter <= counter + 4'b0001;
		
		//counter <= counter + (4'b1 &  completed) + (4'b1 &  {{4{completed}},ext_completed}) + (4'b1 &  completed)  +  (4'b1 &  completed) +  (4'b1 &  completed) +  (4'b1 &  completed) ;

   end 
	
	

endmodule 
