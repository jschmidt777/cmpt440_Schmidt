/**
 * file: ManWolf.java author: Joseph Schmidt course: CMPT 440 assignment:
 * Homework 1 due date: March 20, 2017 version: 1.0
 * 
 * This file takes a string from the command line and reports whether or not it
 * represents a solution to the man-wolf-goat-cabbage problem in Chapter 2 of
 * the textbook.
 */

// TODO: Block comments

public class ManWolf {
  // reused from the book on page 40
  // reusing code from the book from pages 37-42
  /*
   * Based on the DFA diagram on page 11 Need these states to account for the
   * possible inputs, plus an error state
   */
  private static final int q0 = 0;
  private static final int q1 = 1;
  private static final int q2 = 2;
  private static final int q3 = 3;
  private static final int q4 = 4;
  private static final int q5 = 5;
  private static final int q6 = 6;
  private static final int q7 = 7;
  private static final int q8 = 8;
  private static final int q9 = 9;
  private static final int q10 = 10;

  private int state = 0; // initialize at zero; this is the start of the dfa

  private static int[][] delta =
  /* G W C N */
  { { q1, q10, q10, q10 },// q0
      { q0, q10, q10, q2 },// q1
      { q10, q3, q4, q1 },// q2
      { q5, q2, q10, q10 },// q3
      { q6, q10, q2, q10 },// q4
      { q3, q10, q7, q10 },// q5
      { q4, q7, q10, q10 },// q6
      { q10, q6, q5, q8 },// q7
      { q9, q10, q10, q7 },// q8
      { q8, q10, q10, q10 } // q9
                            // q10 (error state)
  };

  /**
   * Makes transition on each char in the given string.
   * 
   * @param in
   *          : the string to use as input
   */

  public void process(String in) {
    for (int i = 0; i < in.length(); i++) {
      char c = in.charAt(i);
      try {
        state = delta[state][c - 'a']; // I think this should work
      } catch (ArrayIndexOutOfBoundsException ex) {
        state = delta[state][c]; // possible solution
      }
    }
  }

  /**
   * 
   * Reset the current state to the start state.
   */
  public void reset() {
    state = q0;
  }

  /**
   * 
   * @return true if the end state is an accepting state
   */
  public boolean accepted() {
    return state == q9;
  }
}
