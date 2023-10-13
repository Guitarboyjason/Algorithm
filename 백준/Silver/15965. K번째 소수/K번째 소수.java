import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.sql.Array;
import java.util.ArrayList;

public class Main {
    static boolean [] prime_num;
    public static void main(String[] args) throws IOException {
        prime_num = new boolean[500_001];
        for(int i = 0 ; i < 500_001; i ++){
            prime_num[i] = true;
        }
        prime_num[0] = false;
        prime_num[1] = false;

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int K = Integer.parseInt(br.readLine());
        ArrayList<Integer> prime = new ArrayList<>();
        for(int i = 2; i <= (int)Math.pow(500_000,0.5) ; i ++){
//            if (!prime_num[i])
//                continue;
//            prime.add(i);
            if (prime_num[i]) {
                for (int j = i+i; j < 500_000; j += i) {
                    prime_num[j] = false;
                }
            }
        }
//        System.out.println(prime);
        for(int i = 0 ; i <= 500_000 ; i ++){
            if(prime_num[i])
//                System.out.println(prime_num[i]);
                prime.add(i);
        }

        System.out.println(prime.get(K-1));
    }
}