package codeup;

import java.util.Scanner;

public class 기초입출력1023 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String A = sc.next();
        String[] num = A.split("\\.");
        System.out.printf("%s\n%s", num[0], num[1]);
    }
}
