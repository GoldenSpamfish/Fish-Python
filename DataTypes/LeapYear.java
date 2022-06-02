public class LeapYear {
    
    public static void main(String[] args) {
        
        int year = Integer.parseInt(args[0]);
        
        boolean result = year % 4 == 0;
        result = result && year % 100 != 0;
        result = result || year % 400 == 0;
        
        System.out.println(result);
    }
}