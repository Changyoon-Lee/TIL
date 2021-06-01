package codeup;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 기초삼항연산1064 {
    public static void main(String[] args) throws IOException {
        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
        String n[] = br.readLine().split(" ");
        int A = Integer.parseInt(n[0]);
        int B = Integer.parseInt(n[1]);
        int C = Integer.parseInt(n[2]);

        int min = A<B ? A : B;
        min = min<C ? min : C;
        System.out.println(min);
        }
    }

