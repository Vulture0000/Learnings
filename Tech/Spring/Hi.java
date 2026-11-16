import java.util.*;
public class Hi{
    public static void main(String[] args ){
        int[] arr = {1,3,5,2,4,6,1,2,3};
        for(int i=0;i<arr.length-1;i++){
            for(int j =0;j<arr.length-i-1;j++){
                if(arr[j] > arr[j+1]){
                    int t = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] =t;
                }
            }
        }
        System.out.println(Arrays.toString(arr));
    }
}