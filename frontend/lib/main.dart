import 'dart:async';
import 'dart:collection';
import 'package:webview_flutter/webview_flutter.dart';
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
  final String TWILIO_NUMBER = "6479311893";
  final myController = TextEditingController();
  WebViewController _controller;
  
  int numberOfSms = 0;
  List<String> messages = new List<String>();
  String htmlText = "";

  void sendToSms(String url_message) {
    print((this.numberOfSms).toString());
    SmsSender sender = new SmsSender();
    String address = TWILIO_NUMBER;
    sender.sendSms(new SmsMessage(address, url_message));
    SmsReceiver receiver = new SmsReceiver();
    receiver.onSmsReceived.listen((SmsMessage msg) => this.handleSms(msg.body));
    // if(this.numberOfSms == 0) {
    //   receiver.onSmsReceived.listen((SmsMessage msg) => this.getNumbeOfSms(msg.body));
    // } else {
    //   receiver.onSmsReceived.listen((SmsMessage msg) => this.appendQueue(msg.body));
    // }
  }

  void handleSms(String message) {
    if (this.numberOfSms == 0){
      print("NUMBERS: " + (this.numberOfSms).toString());
      this.numberOfSms = int.parse(message.substring(38, message.length));
      print("NUMBERS: " + (this.numberOfSms).toString());
    }
    else {
      print("APPENDING: ");
      print(message.substring(38, message.length));
      this.messages.add(message.substring(38, message.length));
      String temp = message.substring(38, message.length); 
      this.messages.insert(int.parse(temp.substring(0, temp.indexOf(" ")+1)), temp.substring(temp.indexOf(" ")+1));
      print(messages.toString());
      this.numberOfSms--;
      if(this.numberOfSms == 0) {
        print(this.messages.join());
        this.htmlText = this.messages.join();
        print("Making the Webview");
        _controller.loadUrl( Uri.dataFromString(
          this.htmlText,
          mimeType: 'text/html',
        ).toString());
      }
      print((this.numberOfSms).toString());
    }
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
        title: TextField(
          cursorColor: Color(0xFFFFFFFF),
          style: TextStyle(
            fontFamily: "raleway",
            color : Color(0xFFFFFFFF), 
          ),
          controller: myController,
        ),
      ),
      body: WebView(
        initialUrl: "",
        onWebViewCreated: (WebViewController webViewController) {
          this._controller = webViewController;
        },
      ),
      floatingActionButton: FloatingActionButton(
          elevation: 10.0,
          child: Icon(Icons.wifi_lock),
          onPressed: (){
            sendToSms(myController.text);
          }
      ),
      persistentFooterButtons: <Widget>[FlatButton(
          child: Icon(Icons.add_alarm),
          onPressed: (){
          }      
        )
      ],
    );
  }
}