#define LED 2

// Connect your LED in pin 2
void setup() {
    pinMode(LED, OUTPUT);
}

void loop() {
    for (int i = 0; i < 3; i++) {
        delay(500);
        digitalWrite(LED, HIGH);
        digitalWrite(LED, LOW);
    }
    delay(1500);
}