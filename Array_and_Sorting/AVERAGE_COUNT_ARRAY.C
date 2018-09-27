#include <iostream>
using namespace std;

using namespace std;

int main() {
    int t,n,i,x;
    cin>>t;
    while(t--){
        cin>>n>>x;
        int arr[101] = {0};
        int temp[101] = {0};
        int count[101] = {0};

        for(i=0;i<n;i++){
            cin>>temp[i];
            arr[temp[i]]++;
        }

        for(i=0;i<n;i++){
            if(arr[temp[i]] >= 1){
                if(arr[(temp[i]+x)/2] >= 1){
                    count[temp[i]] = arr[(temp[i]+x)/2];
                }
            }
        }

        for(i=0;i<n;i++){
            cout<<count[temp[i]]<<" ";
        }
        cout<<"\n";
    }
	//code
	return 0;
}
