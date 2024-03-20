#define trig 8
#define echo 9

unsigned long duration;
double old_distance, new_distance, distance;

void setup() {
  Serial.begin(9600);
  pinMode(trig, OUTPUT);
  pinMode(echo, INPUT);
}


void loop() {
  digitalWrite(trig, LOW);
  digitalWrite(echo, LOW);
  delayMicroseconds(2);
  digitalWrite(trig, HIGH);
  delayMicroseconds(10);
  digitalWrite(trig, LOW);
  duration = pulseIn(echo, HIGH);
  double value = analogRead(A0);

  distance = 18.5 - (duration / 29.0 / 2.0 - 4.57);
  new_distance = distance;
  
  if ((new_distance < (old_distance - 0.05)) || (new_distance > (old_distance + 0.05))) {
    old_distance = new_distance;
  }

  Serial.print(((value * 5) / 1024 - 0.5) * 37.5);
  Serial.print(",");
  Serial.println(old_distance);
}
