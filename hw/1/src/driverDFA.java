/**
 * file: driverDFA.java
 * author: Joseph Schmidt
 * course: CMPT 440
 * assignment: Homework 1
 * due date: March 20, 2017
 * version: 1.0
 * 
 * This file reads from standard input, calls the functions of
 * the ManWolf class, and prints the result to standard output.
 */
import java.io.IOException;
/**
 * driverDFA
 * 
 * This class creates an instance of the class ManWolf and 
 * then reads the argument provided by the user of a possible
 * solution to the man-wolf-goat-cabbage problem. It then tells
 * the user whether or not the solution is correct or not.
 */
public class driverDFA {
  public static void main(String[] args) throws IOException{
      try{ 
        ManWolf d = new ManWolf(); // The dfa created by the ManWolf class
        String input = args[0]; //This reads an argument from the command line
        while (input != null) {
            d.reset();
            d.process(input);
            if (d.accepted()) {
              System.out.println("That is a solution.");
              System.exit(0);
            }else{
              System.out.println("That is not a solution.");
              System.exit(0);
            }
        }
      }catch (ArrayIndexOutOfBoundsException ex){
        System.out.println("Error: Please provide an argument.");
      }
    }
}
