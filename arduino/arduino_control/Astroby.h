#include "Motor.h"

int max = 1;
int med = 0.75;

class Astroby
{
	private:
		int speed;
		Motor l, r;

	public:
		Astroby();

		void forward(int pwm);
		void backward(int pwm);
		void stop();

		void lforward(int pwm);
		void lbackward(int pwm);
		void lstop();

		void rforward(int pwm);
		void rbackward(int pwm);
		void rstop();

		void toggle_speed();
};


// class definitions
Astroby::Astroby() : speed(1), l(Motor(8, 9)), r(Motor(10, 11)) {}

void Astroby::forward(int pwm = 0) {
	if (!pwm)
		pwm = speed;

	l.forward(pwm);
	r.forward(pwm);
}

void Astroby::backward(int pwm = 0) {
	if (!pwm)
		pwm = speed;

	l.backward(pwm);
	r.backward(pwm);
}

void Astroby::stop() {
	l.stop();
	r.stop();
};

void Astroby::lforward(int pwm = 0) {
	if (!pwm)
		pwm = speed;

	l.forward(pwm);
}

void Astroby::lbackward(int pwm = 0) {
	if (!pwm)
		pwm = speed;

	l.backward(pwm);
}

void Astroby::lstop() {
	l.stop();
};

void Astroby::rforward(int pwm = 0) {
	if (!pwm)
		pwm = speed;

	r.forward(pwm);
}

void Astroby::rbackward(int pwm = 0) {
	if (!pwm)
		pwm = speed;
	
	r.backward(pwm);
}

void Astroby::rstop() {
	r.stop();
};

void Astroby::toggle_speed() {
	if (speed == max)
		speed = med;
	else if (speed == med)
		speed = max;
}