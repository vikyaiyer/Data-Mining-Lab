import java.util.*;
import java.io.*;

public class Classification {
    String table[][], line="", qry="";
    Map<String,Integer> counts[];
    StringTokenizer st;
    int rows=0, columns=0;
    float ans=1.0f, tmp, proYes=1.0f, proNo=1.0f;
    Scanner sc;
    
    public Classification(){
        sc = new Scanner(System.in);
    }
    
    void dataInput(){
    	try{
			FileReader file = new FileReader("plant.csv");
			BufferedReader br = new BufferedReader(file);
			line = br.readLine();
		    columns = (line.split(",")).length;
		    counts = new LinkedHashMap[columns];
		    do{
		    	rows++;
		    }while((line = br.readLine())!=null);
		    
		    file = new FileReader("plant.csv");
			br = new BufferedReader(file);
		    table = new String[rows][columns];
		    for(int i=0;i<rows;i++){
		    	st = new StringTokenizer(br.readLine(),",");
		    	for(int j=0;j<columns;j++)
		    		table[i][j]=st.nextToken();
		    }
		    qry="";
		    for(int j=0;j<columns-1;j++)
		    	qry+=table[0][j]+',';
		    qry = qry.substring(0,qry.length()-1);
		    System.out.println("Enter comma separated query ("+qry+") :");
		    qry=sc.nextLine();
        }catch(Exception e){
        	e.printStackTrace();
       	}
    }
    
    void calcultions(){
    	for(int i=0;i<columns;i++){
    		counts[i] = new LinkedHashMap<>();
		    for(int j=1;j<rows;j++){
		    	if(!counts[i].containsKey(table[j][i]))
		    		counts[i].put(table[j][i],1);
		    	else
		    		counts[i].put(table[j][i],counts[i].get(table[j][i])+1);
		    }
		}
		
		StringTokenizer st = new StringTokenizer(qry,",");
		
		for(int i=0;i<columns-1;i++){
			tmp = findProbability(i,st.nextToken(),"Yes");
			ans = ans*tmp;
		}
		proYes = ans;// * counts[columns-1].get("Yes")/(rows-1);
		
		ans=1.0f;
		st = new StringTokenizer(qry,",");
		for(int i=0;i<columns-1;i++){
			tmp = findProbability(i,st.nextToken(),"No");
			ans = ans*tmp;
		}
		proNo = ans;// * counts[columns-1].get("No")/(rows-1);
    }
    
    float findProbability(int col, String key, String app){
    	int yes = 0;
    	for(int i=0;i<rows;i++){
			if(table[i][col].equals(key) && table[i][columns-1].equals(app))
				yes++;
		}
		return (float)yes/counts[columns-1].get(app);//counts[col].get(key);
    }
              
    void output(){
        for(int i=0;i<rows;i++){
            for(int j=0;j<columns;j++){
                System.out.print(table[i][j]+"\t|");
            }
            System.out.println();
        }
        String s = (proYes>proNo?"Yes":"No");
        System.out.println(proYes+","+proNo);
        System.out.println("\nQuery : "+qry+"\n"+table[0][columns-1]+" : "+s);           
    }
    
    public static void main(String args[]){
        Classification obj = new Classification();
        System.out.println("\nData is taken from 'plant.csv'.\n");
        obj.dataInput();
        obj.calcultions();
        obj.output();
        System.out.println();
    }
}
//Orange,Soft,Yes,Smooth
