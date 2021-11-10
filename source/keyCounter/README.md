# keyCounter
___
An example program that may or may not be useful--it logs the number of button clicks. Demonstrates the variable-loop logic used for the NumKey system in a condensed package.

1. INSTALLATION
  
Simply copy & paste the provided variables list into the aircraft project file you would like to have this package installed for.
  
2. USAGE

To use this with a button part, the button part must have the properties outlined in line 4 of the source code. That is, the button should have the `interactionType` of `Once`, an `inputId` of `buttonValue`, and finally a `outputValue` that is a non-zero value (but normally it would be something like `1`).

3. WARNINGS

You should not alter the order of the variables. The order of the evaluation cycle is critical to normal operation of the program, and change in their order will destroy the logic used.

4. LICENSE

This program is licensed under the MIT license. You may freely use it in your builds.
