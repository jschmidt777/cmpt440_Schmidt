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

import java.io.*;

//TODO:Block comments
public class driverDFA {
  public static void main(String[] args) throws IOException {
    ManWolf d = new ManWolf(); // The dfa created in the ManWolf class
    System.out.println("Please enter a combination of the letters "
                        + "'wgcn' to see if they make a solution.");
    BufferedReader in = // Standard input for reading the command line
    new BufferedReader(new InputStreamReader(System.in));

    // Read and echo lines until EOF

    String s = in.readLine();
    while (s != null) {
      d.reset();
      d.process(s);
      if (d.accepted()) {
        System.out.println("This is a solution.");
        System.out.println(s);
      }else{
        System.out.println("This is not a solution.");
      }
      s = in.readLine();
    }

  }
}
