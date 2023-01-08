/*
X보다 작은 수 Java 풀이
https://doctcoder.tistory.com/entry/X%EB%B3%B4%EB%8B%A4-%EC%9E%91%EC%9D%80-%EC%88%98-%ED%92%80%EC%9D%B4
*/
import java.util.Scanner;

class Main 
{
  public static void main(String[] args)
  {
      Scanner sc = new Scanner(System.in);
			int n = sc.nextInt();
		  int x = sc.nextInt();
			int[] num=new int[10000];
			for(int i=0;i<n;i++)
			{
				num[i]=sc.nextInt();
			}
			for(int i=0;i<n;i++)
			{
				if(num[i]<x) System.out.print(num[i]+" ");
			}
  }
}
