void setup() 
{
  Serial.begin(115200);
  Serial.println("UART setup is done");
}

void loop() {
  int count=0;
  Serial.printf("count=%d\n",count++);
  delay(2000);

}