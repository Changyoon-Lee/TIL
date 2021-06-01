package codeup;

import java.io.IOException;
import java.util.Scanner;

public class 기초논리연산1054 {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int A = Integer.parseInt(sc.next());
        int B = Integer.parseInt(sc.next());
        if ((A==1)||(B==1)) System.out.println(1);
        else System.out.println(0);

    }
}
