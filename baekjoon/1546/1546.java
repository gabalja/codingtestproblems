/*
평균 Java 풀이
https://doctcoder.tistory.com/entry/%ED%8F%89%EA%B7%A0-%ED%92%80%EC%9D%B4
*/
import java.util.Scanner;

class Main 
{
  public static void main(String[] args)
  {
      Scanner sc = new Scanner(System.in);
      double[] arr=new double[1000];
      double maxs=-1;
      double result=0;
      int n = sc.nextInt();
      for(int i=0;i<n;i++)
      {
      	double inp = sc.nextDouble();
        if(inp>maxs) maxs=inp;
        arr[i]=inp;
      }
      for(int i=0;i<n;i++)
      {
      	arr[i]=arr[i]/maxs*100;
        result+=arr[i];
      }
      result/=n;
      System.out.println(result);
  }
}
