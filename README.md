# algorithm
algorithm repo
import java.util.Scanner;
public class test{

	public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a= sc.nextInt();
        if(a<0){ a= sc.nextInt(); }
        int b = sc.nextInt();
        if(b>=10){ b= sc.nextInt();}
        System.out.println(a+b);
    }
}