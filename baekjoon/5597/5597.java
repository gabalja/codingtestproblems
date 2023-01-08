/*
과제 안 내신 분..? Java 풀이
https://doctcoder.tistory.com/entry/%EA%B3%BC%EC%A0%9C-%EC%95%88-%EB%82%B4%EC%8B%A0-%EB%B6%84-%ED%92%80%EC%9D%B4
*/
import java.util.Scanner;

class Main 
{
  public static void main(String[] args)
  {
      Scanner sc = new Scanner(System.in);
      int[] stu=new int[30];
      for(int i=0;i<28;i++)
      {
      	int inp = sc.nextInt();
        stu[inp-1]++;
      }
      for(int i=0;i<30;i++)
      {
      	if(stu[i]==0) System.out.println(i+1);
      }
  }
}
