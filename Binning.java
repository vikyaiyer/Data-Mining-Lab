import java.util.*;
public class Binning 
{
   
    ArrayList<Integer> list=new ArrayList<>();
    ArrayList bins[];

    int size, width, binCnt;
    void input()
    {
	 Scanner sc=new Scanner(System.in);       
	 System.out.println("Enter the number of Elements  :");
        size = sc.nextInt();
        System.out.println("Enter width of each  bin :");
        width = sc.nextInt();         
        System.out.println("Enter "+size+" numbers :");
        for(int i=0;i<size;i++)
            list.add(sc.nextInt());
          if(size%width==0)
			binCnt=size/width;
	  else
		binCnt=size/width+1;	
        Collections.sort(list);           
    }
    void binEquiWidth()
    {
        bins = null;
        bins = new ArrayList[binCnt];
        int cnt=0;
        for(int i=0;i<binCnt;i++)
	{
            bins[i]=new ArrayList<>();
            for(int j=0;j<width && cnt<list.size();j++)
		{
                	bins[i].add(list.get(cnt));
                	cnt++;
    		}
    	}
    }
    
    void binBoundaries()
    {

        int left, right, near;
        for(int i=0;i<binCnt;i++)
	{
            left =(int) bins[i].get(0);
            right =(int)bins[i].get((bins[i].size()-1));
            for(int j=1;j<bins[i].size()-1;j++)
	     {
                int no = (int)bins[i].get(j);
		if(no-left<=right-no)
			near=left;
		else
			near=right;
             		bins[i].set(j, near);
            }
        }
    }
    
    void binMean()
	{
	        for(int i=0;i<binCnt;i++)
		{
	            int a=0;
		    double mean;
	            for(int k=0;k<bins[i].size();k++)
	                a +=(int) bins[i].get(k);
	            mean = (double)a/bins[i].size();
	            for(int j=0;j<bins[i].size();j++)
		     {
	                bins[i].set(j, mean);
     	  	     }
        	}
    }
    
    void output()
	{
	        for(int i=0;i<binCnt;i++)
		{
		   int k=i+1;
		   System.out.println("Bin "+k+":");
 	           for(int j=0;j<bins[i].size();j++)
			{
               		 	System.out.print(bins[i].get(j)+" ");
            		}
            		System.out.println();
			System.out.println();
        	}
    	}
    
    public static void main(String []arg)
	{
	        Binning b = new Binning();
	        b.input();
	        System.out.println("\nEqui Width Binning :");
	        b.binEquiWidth();
	        b.output();
	        System.out.println("\nBin Boundaries :");
	       	b.binBoundaries();
	        b.output();
	        System.out.println("\nBin Mean :");
	        b.binEquiWidth();
	        b.binMean();
	        b.output();
       }
}

