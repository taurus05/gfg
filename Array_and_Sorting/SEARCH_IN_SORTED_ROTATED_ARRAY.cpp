#include <iostream>
using namespace std;

int bin(int s, int e, int k, int arr[])
{

    int m;
    while(s<=e){
        m = (int)(s+e)/2;
        if(arr[m] == k){
            // cout<<"if(arr[m] == k)";
            return m;}
        else if(k>arr[m]){
            // cout<<"else if(k>arr[m])";
              s = m+1;}
        else if(k<arr[m]){
            // cout<<"else if(k<arr[m])";
              e = m-1;}
    }
  return -1;
}
int main() {
    int t,n,i,maxi=0,max=0,k,h1,h2;
    cin>>t;
    while(t--){

        cin>>n;
        maxi = 0;
        max = 0;
        int arr[n];
        for(i=0;i<n;i++){
            cin>>arr[i];
            if(arr[i] > max){
                max = arr[i];
                maxi = i;
            }
        }

        // cout<<max<<" "<<maxi;
        cin>>k;

        h1 = bin(0,maxi,k,arr);
        h2 = bin(maxi+1,n-1,k,arr);
        // cout<<init<<fin;
        if((h1 == -1) && (h2 == -1)){
            cout<<-1<<"\n";
        }
        else if((h1 != -1) && (h2 == -1)){
            cout<<h1<<"\n";
        }
        else if((h1 == -1)&& (h2 != -1)){
            cout<<h2<<"\n";
        }
    }
	//code
	return 0;
}
