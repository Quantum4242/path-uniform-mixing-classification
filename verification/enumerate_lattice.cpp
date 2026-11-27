#include <iostream>
#include <vector>
#include <cstdlib>
using namespace std;
int n,d,r; vector<int> freeidx,piv,den,x,partial;vector<vector<int>> A;long long visits=0,found=0;
void rec(int j,int budget){
 if(j==d){++visits;int w=0;for(int i=0;i<r;i++){if(partial[i]%den[i])return;w+=abs(partial[i]/den[i]);if(w>budget)return;}if(budget==10&&w==0)return;for(int i=0;i<r;i++)x[piv[i]]=partial[i]/den[i];for(int i=0;i<n;i++)cout<<x[i]<<(i==n-1?'\n':' ');++found;return;}
 for(int v=-budget;v<=budget;v++){x[freeidx[j]]=v;for(int i=0;i<r;i++)partial[i]+=A[i][j]*v;rec(j+1,budget-abs(v));for(int i=0;i<r;i++)partial[i]-=A[i][j]*v;}
}
int main(){cin>>n>>d>>r;freeidx.resize(d);piv.resize(r);den.resize(r);x.resize(n);partial.resize(r);A.assign(r,vector<int>(d));for(int& i:freeidx)cin>>i;for(int i=0;i<r;i++){cin>>piv[i]>>den[i];for(int& a:A[i])cin>>a;}rec(0,10);cerr<<visits<<" free vectors; "<<found<<" nonzero short relations\n";}
