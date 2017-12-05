import java.io.*;
import java.util.*;
class Normalization
{
	public static void main(String [] args)
	{
		int n;
		double ur,lr;
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter number of Elements");
		n=sc.nextInt();		
		double arr[]=new double[n];
		
		double a[]=new double[n];
		double b[]=new double[n];
		System.out.println("Enter Data");
		for(int i=0;i<n;i++)
		{
		    arr[i]=sc.nextDouble();
		    a[i]=arr[i];	
		    b[i]=arr[i];	
		}
		System.out.println("Enter the range you want to input");

		System.out.println("lower limit:");
		   lr=sc.nextDouble();
				

		System.out.println("upper limit:");
		   ur=sc.nextDouble();
		
			
		Arrays.sort(arr);
		double min=arr[0];
		double max=arr[arr.length-1];	
		
		for(int i=0;i<n;i++)		
		{
			arr[i]=(((arr[i]-min)/(max-min))*(ur-lr))+lr;
		}

		System.out.println("Data After Min Max Normaliztion is :");
		for(int i=0;i<n;i++)	
			System.out.println(arr[i]);




		double mean=0;
		for(int i=0;i<a.length;i++)			
		{
						
			mean=mean+a[i];
			

		}
		
		mean=mean/a.length;
		double std=0,num=0;
		for(int i=0;i<a.length;i++)	
		{
			num+=(a[i]-mean)*(a[i]-mean);		
		}
		num=num/(a.length-1);
		std=Math.sqrt(num);
		
		for(int i=0;i<a.length;i++)
		{
			a[i]=(a[i]-mean)/std;
		}
		System.out.println("Data After Z score Normalization");
		for(int i=0;i<a.length;i++)
		{
			System.out.println(a[i]);	
		}
		
		System.out.println("Enter The value of N for Divide by N normalization Technique");		
		int s=sc.nextInt();
		
		for(int i=0;i<n;i++)
		    b[i]=b[i]/s;

		System.out.println("Data After Divide By N Normlization");
		for(int i=0;i<n;i++)
			System.out.println(b[i]);	


		}
		
}
	
