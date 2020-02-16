import 'dart:collection';

import 'package:flutter/material.dart';
import 'package:sms/sms.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Retrieve Text Input',
      home: MyCustomForm(),
    );
  }
}

// Define a custom Form widget.
class MyCustomForm extends StatefulWidget {
  @override
  _MyCustomFormState createState() => _MyCustomFormState();
}

// Define a corresponding State class.
// This class holds the data related to the Form.
class _MyCustomFormState extends State<MyCustomForm> {
  // Create a text controller and use it to retrieve the current value
  // of the TextField.
  final String TWILIO_NUMBER = "6474962175";
  final myController = TextEditingController();
  int numberOfSms = 0;
  Queue<String> messages;

  void sendToSms(String url_message) async {
    SmsSender sender = new SmsSender();
    String address = TWILIO_NUMBER;
    sender.sendSms(new SmsMessage(address, url_message));

    SmsReceiver receiver = new SmsReceiver();
    receiver.onSmsReceived.listen((SmsMessage msg) => print(msg.body));
  }

  void getNumbeOfSms(String message) {
    this.numberOfSms = int.parse(message.substring(38, message.length));
  }

  void appendQueue(String message) {

    this.numberOfSms--;
  }

  @override
  void dispose() {
    // Clean up the controller when the widget is disposed.
    myController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Type in a URL without Internet'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: TextField(
          controller: myController,
        ),
      ),
      floatingActionButton: FloatingActionButton(
          elevation: 10.0,
          child: Icon(Icons.wifi_lock),
          onPressed: (){
            sendToSms(myController.text);
          }
      ),
    );
  }
}