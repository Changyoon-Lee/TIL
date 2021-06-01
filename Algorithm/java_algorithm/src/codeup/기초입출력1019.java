package codeup;

import java.util.Scanner;

public class 기초입출력1019 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        String[] arr = a.split("\\.");
        int A = Integer.valueOf(arr[0]);
        int B = Integer.valueOf(arr[1]);
        int C = Integer.valueOf(arr[2]);
        System.out.printf("%04d.%02d.%02d", A,B,C);
    }
}
