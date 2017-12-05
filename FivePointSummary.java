import java.util.*;

public class FivePointSummary {
	public static void main(String[] args){
		Scanner sc=new Scanner(System.in);
		
		System.out.println("Enter no. of values");
		int n=sc.nextInt();
		ArrayList<Integer> dataset=new ArrayList<Integer>(n);
		Double min,q1,median,q3,max;
		int first,second,fq,tq;
		
		System.out.println("Enter "+n+" records values:");
		for(int i=0;i<n;i++)
			dataset.add(sc.nextInt());
				
		Collections.sort(dataset);
		
		System.out.println(dataset);
		
		min=(double)Collections.min(dataset);
		max=(double)Collections.max(dataset);
		

		fq=(int)(n*(25/100.0f));
		tq=(int)(n*(75/100.0f));
		
		if(n%2==0){
				first=(n/2);
				second=(n/2)+1;
				median=(dataset.get(first)+dataset.get(second))/2.0;
			}
			else{
				median=(double)dataset.get(n/2);
			}
		
		q1=(double)dataset.get(fq);
		q3=(double)dataset.get(tq);
		
		System.out.println("Minimum="+min);
		System.out.println("First Quartile Q1="+q1);
		System.out.println("Median Q2="+median);
		System.out.println("Third Quartile="+q3);
		System.out.println("Maximum="+max);
	}
}
