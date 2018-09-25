int main() {
    int t,i,j;
    scanf("%d",&t);
    while(t--){
        int n,temp=0;
        scanf("%d",&n);
        int arr[n];
        for(i=0;i<n;i++)
            scanf("%d",&arr[i]);
        int k;
        scanf("%d",&k);

        for(i=0;i<n-k+1;i++){
            temp = 0;
            for(j=i;j<i+k;j++){
                if(arr[j] < 0){
                    temp = arr[j];
                    break;
                }
            }
            printf("%d ",temp);
        }
        printf("\n");
    }
	//code
	return 0;
}
