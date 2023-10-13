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

        ArrayList<Integer> prime = new ArrayList<>();
        for(int i = 2; i <= 500_000/2 ; i ++){
            if (!prime_num[i])
                continue;
            prime.add(i);
            for(long j = i*2; j < 500_001; j += i){
                prime_num[(int)j] = false;
            }
        }
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int K = Integer.parseInt(br.readLine());

        System.out.println(prime.get(K-1));
    }
}