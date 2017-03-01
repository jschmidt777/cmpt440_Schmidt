/**
 * file: ManWolf.java
 * author: Joseph Schmidt
 * course: CMPT 440
 * assignment: Homework 1
 * due date: March 20, 2017
 * version: 1.0
 * 
 * This file takes a string from the command line 
 * and reports whether or not it represents a solution to the man-wolf-goat-cabbage problem
 * in Chapter 2 of the textbook.
 */
package mwgc_flac; //The package encapsulating the two classes ManWolf and driverDFA
import java.io.*; 
//TODO: Block comments
public class ManWolf {
//reused from the book on page 40
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
