package codeup;

import java.util.Scanner;

public class 기초산술연산1046 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int A = Integer.valueOf(sc.next());
        int B = Integer.valueOf(sc.next());
        int C = Integer.valueOf(sc.next());

        System.out.printf("%s\n%.1f", (long)A+B+C, (float)(A+B+C)/3);
    }
}
