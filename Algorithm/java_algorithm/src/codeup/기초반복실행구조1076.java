package codeup;

import java.util.Scanner;

public class 기초반복실행구조1076 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        char a = 'a';
        char x = sc.nextLine().charAt(0);
        do {
            System.out.println(a);
            a+=1;

        } while (a<=x);

    }
}
