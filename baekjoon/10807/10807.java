/*
개수 세기 Java 풀이
https://doctcoder.tistory.com/entry/%EA%B0%9C%EC%88%98-%EC%84%B8%EA%B8%B0-%ED%92%80%EC%9D%B4
*/
import java.util.Scanner;

class Main 
{
  public static void main(String[] args)
  {
      Scanner sc = new Scanner(System.in);
			int n = sc.nextInt();
			int[] num=new int[100];
			for(int i=0;i<n;i++)
			{
				num[i]=sc.nextInt();
			}
			int v = sc.nextInt();
			int cnt=0;
			for(int i=0;i<n;i++)
			{
				if(num[i]==v) cnt++;
			}
			System.out.println(cnt);
  }
}
