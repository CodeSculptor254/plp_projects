import 'dart:io';

void main() {
  // Example of int data type
  int myInt = 10;
  print("Integer example: $myInt");  // Output: Integer example: 10
  
  // Example of double data type
  double myDouble = 10.5;
  print("Double example: $myDouble");  // Output: Double example: 10.5
  
  // Example of String data type
  String myString = "Hello, Dart!";
  print("String example: $myString");  // Output: String example: Hello, Dart!
  
  // Example of List data type
  List<int> myList = [1, 2, 3, 4, 5];
  print("List example: $myList");  // Output: List example: [1, 2, 3, 4, 5]
  
  // Example of accessing List elements
  int firstElement = myList[0];
  print("First element of List: $firstElement");  // Output: First element of List: 1
  
  // Example of Map data type
  Map<String, int> myMap = {
    'one': 1,
    'two': 2,
    'three': 3,
  };
  print("Map example: $myMap");  // Output: Map example: {one: 1, two: 2, three: 3}
  
  // Example of accessing Map elements
  int valueForTwo = myMap['two']!;
  print("Value for key 'two' in Map: $valueForTwo");  // Output: Value for key 'two' in Map: 2
  
  // Prompt user for a number
  stdout.write("Enter a number: ");
  String input = stdin.readLineSync()!;
  
  try {
    int number = int.parse(input);
    
    // Checking the number and printing a message
    if (number > 10) {
      print("Your number is greater than 10");
    } else if (number < 10) {
      print("Your number is less than 10");
    } else {
      print("Your number is equal to 10");
    }
    
  } catch (FormatException) {
    print("Invalid input. Please enter a valid number.");
  }
}
