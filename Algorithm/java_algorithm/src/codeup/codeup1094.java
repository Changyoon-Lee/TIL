package codeup;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class codeup1094 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        br.readLine();
        String[] num = br.readLine().split(" ");
        for (int i = num.length-1; i>=0; i--){
            System.out.print(num[i]+" ");
        }
    }
}
