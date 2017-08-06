class Motor
{
	private:
		int inp1;
		int inp2;

	public:
		Motor(int val1, int val2);
	
		void forward(float pwm);
		void backward(float pwm);
		void stop();
};


Motor::Motor(int val1, int val2) : inp1(val1), inp2(val2) {
	pinMode(inp1, OUTPUT);
	pinMode(inp2, OUTPUT);
}

void Motor::forward(float pwm=1) {
	analogWrite(inp1, pwm * 255);
	analogWrite(inp2, 0);	
}

void Motor::backward(float pwm=1) {
	analogWrite(inp2, pwm * 255);
	analogWrite(inp1, 0);
}

void Motor::stop() {
	digitalWrite(inp1, LOW);
	digitalWrite(inp2, LOW);
}