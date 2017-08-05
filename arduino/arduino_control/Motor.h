class Motor
{
	private:
		int inp1;
		int inp2;

	public:
		Motor(int val1, int val2);
	
		void forward(int pwm);
		void backward(int pwm);
		void stop();
};


Motor::Motor(int val1, int val2) : inp1(val1), inp2(val2) {
	pinMode(inp1, OUTPUT);
	pinMode(inp2, OUTPUT);
}

void Motor::forward(int pwm=1) {
	analogWrite(inp1, pwm * 255);
	analogWrite(inp2, 0);	
}

void Motor::backward(int pwm=1) {
	analogWrite(inp2, pwm * 255);
	analogWrite(inp1, 0);
}

void Motor::stop() {
	digitalWrite(inp1, LOW);
	digitalWrite(inp2, LOW);
}