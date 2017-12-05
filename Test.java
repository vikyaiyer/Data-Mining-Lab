// Program to compute t-weight and d-weight

// t-weight is sub-region wise %
// d-weight is complete region wise %

import java.util.*;
class Test{
	public static void main(String[] args){
		int numDept,g_total = 0,p_total = 0;
		double t_wgt,d_wgt;
		
		Scanner sc = new Scanner(System.in);
		
		System.out.println("Enter no. of departments: ");
		numDept = sc.nextInt();		
		
		int total[] = new int[numDept];
		int placed[] = new int[numDept];
		
		for(int i=0; i<numDept;i++){
			System.out.println("Enter the total student for department "+i+" : ");
			total[i] = sc.nextInt();
			System.out.println("Enter the students placed from department "+i+" : ");
			placed[i] = sc.nextInt();
			
			t_wgt = (double)placed[i]/total[i];
			t_wgt = t_wgt * 100.00;
			
			System.out.println("T-weight for department "+i+" is "+t_wgt+"\n");
			p_total = p_total + placed[i];
			g_total = g_total + total[i];			
		}
		
		System.out.println("Total number of students in clg: "+g_total);
		System.out.println("Total number of place students in clg: "+p_total);
		for(int i=0;i<numDept;i++){
			d_wgt = (double)placed[i]/p_total;
			d_wgt = d_wgt * 100.00;
			System.out.println("D-weight for department "+i+" is "+d_wgt);			
		}
		
	}
}