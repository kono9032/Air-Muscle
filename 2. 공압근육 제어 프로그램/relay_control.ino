#define relay1 11
#define relay2 10


void setup() {
  Serial.begin(9600);
  pinMode(relay1, OUTPUT);
  pinMode(relay2, OUTPUT);
}

void loop() {
  double value = analogRead(A0);
  Serial.println(((value * 5) / 1024 - 0.5) * 37.5);

  if (Serial.available())
  {
    char value = Serial.read();
    if (value == '1')
    {
      static boolean output = HIGH;
      digitalWrite(relay1, output);
      output = !output;
    }
    if (value == '2')
    {
      static boolean output = HIGH;
      digitalWrite(relay2, output);
      output = !output;
    }
  }
}
