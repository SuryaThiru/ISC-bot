#include "Motor.h"

float max = 1;
float med = 0.60;

class Astroby
{
	private:
		float speed;
		Motor l, r;

	public:
		Astroby();

		void forward(float pwm);
		void backward(float pwm);
		void stop();

		void lforward(float pwm);
		void lbackward(float pwm);
		void lstop();

		void rforward(float pwm);
		void rbackward(float pwm);
		void rstop();

		void toggle_speed();
};


// class definitions
Astroby::Astroby() : speed(1), l(Motor(5, 6)), r(Motor(10, 11)) {}

void Astroby::forward(float pwm = 0) {
	if (!pwm)
		pwm = speed;

	l.forward(pwm);
	r.forward(pwm);
}

void Astroby::backward(float pwm = 0) {
	if (!pwm)
		pwm = speed;

	l.backward(pwm);
	r.backward(pwm);
}

void Astroby::stop() {
	l.stop();
	r.stop();
};

void Astroby::lforward(float pwm = 0) {
	if (!pwm)
		pwm = speed;

	l.forward(pwm);
}

void Astroby::lbackward(float pwm = 0) {
	if (!pwm)
		pwm = speed;

	l.backward(pwm);
}

void Astroby::lstop() {
	l.stop();
};

void Astroby::rforward(float pwm = 0) {
	if (!pwm)
		pwm = speed;

	r.forward(pwm);
}

void Astroby::rbackward(float pwm = 0) {
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