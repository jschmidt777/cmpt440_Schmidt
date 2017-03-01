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
package mwgc_flac; /*The package encapsulating the two classes ManWolf and driverDFA*/
import java.io.*;
//TODO:Block comments
public class driverDFA {
  public static void main(String[] args) {
    throws IOException {
      driverDFA d = new driverDFA; //The dfa created in the driverDFA class
      
      BufferedReader in = //Standard input for reading the command line
        new BufferedReader (new InputStreamReader(System.in));
      
      //Read and echo lines until EOF
      
      String s = in.readLine();
      while (s!=null){
        m.reset();
        m.process(s);
        if (m.accepted()){
          System.out.println(s);
        }
        s = in.readLine();
      }
    }
  }
  
}
