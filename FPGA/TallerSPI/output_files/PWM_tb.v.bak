module PWM_tb();

	reg [3:0] Porcentaje;
	reg SLK;
	reg pwm;
	
	PWM_module #(.Porcentaje(Porcentaje), .SLK(SLK), .pwm(pwm));
	
	initial begin
	
		SLK = 0;
		repeat (100)
			begin
				#1 SLK = ~SLK;
			end
	
	end
	
	initial begin
	
		Porcentaje = 3;
		#10
		Porcentaje = 8;
		#10
		Porcentje = 10;
		#10;
	
	end

endmodule