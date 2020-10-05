public class DigitalRoot{

    static int digitalRoot(int n){
        
        String nString = Integer.toString(n);

        int nLen = nString.length();
        
        int sum = 0;

        int c = 0;
        while(c < nLen){
            char single_string = nString.charAt(c);
            int single_number = Integer.parseInt(String.valueOf(single_string));

            sum += single_number;

            c++;
        }

        if(sum > 9){
            return digitalRoot(sum);
        }
        else{
            return sum;
        }

    }

    static int digitalRoot2(int n){
        
        String nString = Integer.toString(n);

        int nLen = nString.length();

        while(true){

            int sum = 0;
            
            int c = 0;
            while(c < nLen){
                char single_string = nString.charAt(c);
                int single_number = Integer.parseInt(String.valueOf(single_string));
    
                sum += single_number;
    
                c++;
            }
            

            if(sum > 9){
                n = sum;
                nString = Integer.toString(sum);
                nLen = nString.length();
            }
            else{
                return sum;
            }

        }
    }

    public static void main(String args[]){
        System.out.println(digitalRoot(165));
        System.out.println(digitalRoot2(165));
    }
}