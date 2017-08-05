#include "Astroby.h"

Astroby bot;

void setup()
{
	bot = Astroby();
	Serial.begin(9600);
}


void loop()
{
	String command;

	if (Serial.available() > 0)
		command = Serial.readString();


	if (command == "forward")
		bot.forward();
	else if (command == "backward")
		bot.backward();
	else if (command == "stop")
		bot.stop();

	else if (command == "lforward")
		bot.lforward();
	else if (command == "lbackward")
		bot.lbackward();
	else if (command == "lstop")
		bot.lstop();

	else if (command == "rforward")
		bot.rforward();
	else if (command == "rbackward")
		bot.rbackward();
	else if (command == "rstop")
		bot.rstop();

	else if (command == "toggle_speed")
		bot.toggle_speed();
}
