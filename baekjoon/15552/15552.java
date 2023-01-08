/*
빠른 A+B Java 풀이
https://doctcoder.tistory.com/entry/%EB%B9%A0%EB%A5%B8-AB-%ED%92%80%EC%9D%B4
*/
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.util.Scanner;

class Main 
{
  public static void main(String[] args) throws IOException
  {
      BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
      BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
      int t = Integer.parseInt(bf.readLine());
      for(int i=0;i<t;i++)
      {
      	String s=bf.readLine();
        int a=Integer.parseInt(s.split(" ")[0]);
        int b=Integer.parseInt(s.split(" ")[1]);
        bw.write((a+b)+"\n");
      }
      bw.flush();
  }
}
