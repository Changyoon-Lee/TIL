package codeup;

import java.util.Scanner;

public class codeup1085 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int A = Integer.parseInt(sc.next());
        int B = Integer.parseInt(sc.next());
        int C = Integer.parseInt(sc.next());
        int D = Integer.parseInt(sc.next());

        float res = (float)A * B * C * D;
        System.out.printf("%.1f MB",res/8/1024/1024);

    }
}
