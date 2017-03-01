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
//TODO:Block comments
public class driverDFA {
//reusing code from the book from pages 37-42
  /*
   * Based on the DFA diagram on page 11
   * Need these states to account for the possible inputs, plus an error state
   */
  private static final int q0  = 0;
  private static final int q1  = 1;
  private static final int q2  = 2;
  private static final int q3  = 3;
  private static final int q4  = 4;
  private static final int q5  = 5;
  private static final int q6  = 6;
  private static final int q7  = 7;
  private static final int q8  = 8;
  private static final int q9  = 9;
  private static final int q10 = 10;
  
  private int state = 0; //initialize at zero; this is the start of the dfa
  
  private static int[][] delta =
      /* G   W   C   N */
    {{},//q0
     {},//q2
     {},//q3
     {},//q4
     {},//q5
     {},//q6
     {},//q7
     {},//q8
     {},//q9
     {},//q10 (error state) 
    };
}
