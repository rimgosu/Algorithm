class Solution {
    
    public long isSquare(long n) {
        double sqrt_n = Math.sqrt(n);
        long int_n = (long) sqrt_n;
        System.out.println(int_n+1);
        
        for (long i=1; i<sqrt_n +1 ; i++) {
            if (i * i == n) {
                return (i+1) * (i+1);
            }
        }
        return -1;
    }
    
    public long solution(long n) {
        long answer = 0;
        
        
        return isSquare(n);
    }
}