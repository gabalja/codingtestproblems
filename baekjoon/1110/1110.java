/*
더하기 사이클 Java 풀이
https://doctcoder.tistory.com/entry/%EB%8D%94%ED%95%98%EA%B8%B0-%EC%82%AC%EC%9D%B4%ED%81%B4-%ED%92%80%EC%9D%B4
*/
import java.util.Scanner;

class Main 
{
  public static void main(String[] args)
  {
      Scanner sc = new Scanner(System.in);
      int n = sc.nextInt();
      int nn=n;
      int cycle=0;
      while(true)
      {
      	nn=(nn%10)*10+(nn/10+(nn%10))%10;
        cycle++;
        if(nn==n) break;
      }
      System.out.println(cycle);
  }
}
