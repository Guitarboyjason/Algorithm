import java.util.Scanner;
public class 중앙_이동_알고리즘{
    public static void main(String [] args){
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int tmp = 2;
        for (int i = 0 ; i < N ; i ++){
            tmp = tmp + tmp-1;
        }
        System.out.println(tmp*tmp);
    }
}

/*
 * 0 -> 4   2**2
 * 1 -> 9   == 4 + 5        9 -> 4      3*3 (3-1)**2
 * 2 -> 25  == 9 + 20 - 4   25 -> 16    5*5 (5-1)**2
 * 3 -> 25 + 20 * 5 - 24 == 101     
 * 3 -> 25 + 20 * 5 - 3*4*2
 * 
 * 
 * 
 * 0 -> 4
 * 1 -> 4 * 4 - 3 - 3 == 9
 * 2 -> 9 * 4 - 5 * 3 == 36-15 = 21
 * 
 * 
 * 2**2
 * 3**2
 * 5**2
 * 9**2
 * 17**2
 */