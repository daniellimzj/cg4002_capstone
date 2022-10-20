void setup() {
  Serial.begin(115200);
  
}

void loop() {
  delay(30);
  if (Serial.available()) {
    Serial.println(Serial.read());
  }
}
