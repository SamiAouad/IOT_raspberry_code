#include <LiquidCrystal.h>

long key = 1234;
long challenge;

const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(10, 11, 12, 13, 14, 15, 16);

void setup() {
  // set up the LCD's number of columns and rows:
  lcd.begin(16, 2);
  lcd.print("Door is closed");
  // Print a message to the LCD.
  
  Serial.begin(9600);
  randomSeed(analogRead(4));
  challenge = 0;
}



void loop() {
  lcd.display();
  if (challenge == 0)
    challenge = random(100000);
  Serial.println(challenge);

  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');
    long receivedHash = strtoul(data.c_str(), 0, 10);
    

    long secret = ((challenge + key) * 15744) % 999;
    if (secret == receivedHash){
      Serial.println("opened");
      lcd.clear();
      lcd.print("Door is open");
      challenge = random(100000);
      delay(5000);
      lcd.clear();
      lcd.print("Door is closed");
      Serial.println("closed");
    }
    else{
      lcd.clear();
      lcd.print("Try again!");
      delay(1000);
      Serial.println("error");
    }
  }
  lcd.clear();
  lcd.print("Door is closed");
  delay(2000);
}