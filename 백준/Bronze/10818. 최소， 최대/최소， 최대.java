import java.util.*;
import java.io.*;
import java.math.*;
	


public class Main {
	public static void main(String[] args) throws IOException {
		Scanner scanner = new Scanner(System.in); 
		
		int a = scanner.nextInt();
		int[] arr = new int[a];
		
		for(int i=0;i<a;i++) {
			arr[i] = scanner.nextInt();
		}
		Arrays.sort(arr);
		System.out.print(arr[0]+" "+arr[a-1]);
		
		
	}
		
}

	