import java.util.Scanner;
public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int Kim = sc.nextInt();
        int Lim = sc.nextInt();

        
        /* 
         * 김지민이 임한수를 몇번째에 만나느냐가 제일 중요함.
         * 
         * 김지민이 부전승으로 올라가는 경우에는 어떻게?
         * 
         *  
         */
        int cnt = 1;
        while (N>1) {
//        	cnt += 1;
        	if(Kim%2 == 1 && Kim + 1 == Lim || Lim%2 == 1 && Lim + 1 == Kim){
        		System.out.println(cnt);
        	}
        	cnt += 1;
        	Kim = (Kim+1)/2;
        	Lim = (Lim+1)/2;
        	N = (N%2 == 0)?N/2 : N/2+1;
        }
        
        
        // kim 이 더 큰 수라고 생각하자

//        int tmp = Math.min(Kim,Lim);
//        Kim = Math.max(Kim,Lim);
//        Lim = tmp;
//        // 2분법으로 나누면서 들어가다가 
//        // 만날때? 가 몇번째인지
//
//        // 1만큼 차이나면 1라운드에 바로 만날 수도 있지만
//        // 아닐 수도 있음
//        // 그냥 어느쪽에 치우쳐져있는지를 확인하면 될 것.
//        // 반을 쪼개서 왼쪽과 오른쪽으로 나뉜다? 그럼 해당 라운드에서 만남
//
//
//        /*
//         * 1 ~ 16
//         * 1 ~ 8
//         * 9 ~ 16
//         * 
//         * 1 ~ 15
//         * 1 ~ 7
//         * 8 ~ 14
//         */
////        boolean flag = true;
//        int start = 1;
//        int end = N;
//        int cnt = 0;
//        tmp =  N;
//        while (N > 1) {
//        	N = (N/2*2 == N)?N/2 : N/2+1;
//        	cnt ++;
//        }
//        while (start < end){
//            int middle = (start+end)/2;
//
//            if (Lim <=middle && Kim > middle){
//                System.out.println(cnt);
//                break;
//
//            }
//            else{
//                if(Lim > middle){
////                Lim -= middle;
////                Kim -= middle;
//                	start = middle+1;
//                }
//                else end = middle;
////                N = (N == middle*2)?N/2:N/2+1;
//                	
//            }
//
//            cnt --;
//        }
    }
}