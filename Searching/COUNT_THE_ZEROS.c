#include <stdio.h>
#include <math.h>
int fun(int b, int e, int n,int arr[]){
    int m;
    while(b<e){
    m = ceil((float)(b+e)/2);

    if(arr[m] == 1)
        b = m;

    else{
        if(m > 0 && arr[m] == 0){
            if(arr[m-1]!=0)
                return n-m;

            else
                e = m;
            }
        if(e == 1)
            if(arr[m-1] == 0)
                return n;
            else
                return n-1;
        }
    }
    if(b == e)
        if (arr[b] == 1)
            return 0;
        else
            return 1;

}

int main() {
	//code
	int t,n,count=0;
	scanf("%d",&t);
	while(t--){
	    scanf("%d",&n);
	    int arr[n];
	    for(int i=0;i<n;i++){
	        scanf("%d",&arr[i]);
	    }
	   count = fun(0,n-1,n,arr);
	   printf("%d\n",count);
	}
	return 0;
}
