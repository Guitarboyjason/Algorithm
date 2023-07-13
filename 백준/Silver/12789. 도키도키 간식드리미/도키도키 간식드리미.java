// stack을 구현해야겠네

// import java.util.Arrays;
import java.util.Scanner;


class ArrayStack{
    int top;
    int size;
    int [] stack;
    public ArrayStack(int size){
        this.size = size;
        stack = new int[size];
        top = -1;
    }

    public void push(int item){
        stack[++top] = item;
        // System.out.println(stack[top] + " Pushed");

    }

    public int pop(){
        // System.out.println(stack[top] + " Popped");
        int pop = stack[top--];
        return pop;
        // stack[top--] = 0;
        // return pop;
    }

    public int peek(){
        // System.out.println(stack[top]+" Peek");
        return stack[top];
    }
}

public class Main{

    public static void main(String[] args){
        // System.out.println("Hello");/
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        ArrayStack origin_stack = new ArrayStack(N);
        ArrayStack other_stack = new ArrayStack(N);


        int [] arr = new int [N];
        for (int i = 0 ; i < N ; i ++){
            // origin_stack.push(sc.nextInt());
            arr[i] = sc.nextInt();
        }
        for(int i = N-1 ; i >= 0 ; i -- ){
            origin_stack.push(arr[i]);
        }
        int next = 1;
        boolean flag = false;

        while (origin_stack.top != -1 || other_stack.top != -1){
            flag = false;
            if(origin_stack.top != -1 && origin_stack.peek() == next){
                origin_stack.pop();
                next ++;
                flag = true;
            }
            if (other_stack.top != -1 && other_stack.peek() == next){
                other_stack.pop();
                next++;
                flag = true;
            }
            
            if (!flag){
                if (origin_stack.top == -1)
                    break;
                else{
                    other_stack.push(origin_stack.pop());
                }
            }
        }
        if(flag){
            System.out.println("Nice");
        }
        else System.out.println("Sad");

        
    }
}

