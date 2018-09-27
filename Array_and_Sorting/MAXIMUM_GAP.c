#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	//code
	int n,t,i,j,max;
	cin>>t;
	while(t--){
	    cin>>n;

	    int arr[n];
	    for(i=0;i<n;i++)
	        {cin>>arr[i];}

	    if(n==1)
	        {cout<<0<<"\n";}
	    else{
	    sort(arr,arr+n);

	    int diff[n-1];

	    for(j=0;j<n-1;j++){
	        diff[j] = arr[j+1] - arr[j];
	    }

	    max = diff[0];

	    for(j=1;j<n-1;j++){
	        if(diff[j] > max)
	        {
	            max = diff[j];
	        }
	    }
	    cout<<max<<"\n";
	    }
	}
	return 0;
}
