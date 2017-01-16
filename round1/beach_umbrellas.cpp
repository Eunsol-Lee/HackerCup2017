#include <algorithm>
#include <iostream>

#define max 1000003000
#define mod 1000000007

using namespace std;

long long fact[max];



long long solve()
{

  long long x[2001];
  long long total=0;
  long long result = 0;
  long long space;
  long long rest;
  long long n, m;

  cin >> n >> m;

  for (int i=0; i<n; i++){
    cin >> x[i];
    total += x[i];
  }
  total *= 2;

  if (n == 1){
    return m;
  }

  for (int i=0;i<n; i++){
    for (int j=0;j<n;j++){
      if (i!=j) {
        space= total-x[i]-x[j];
        rest=(m-1)-space;
        if (rest >= 0) {
          cout << "pp" << fact[n+rest] << "   " << fact[rest] << "    " << n << endl;
          result += fact[n+rest]/fact[rest]/n/(n-1);
          result %= mod;
        }
      }
    }
  }

  return result;
}

int main(void){

  int t;

  fact[0] = 1;
  for (int i=1; i<max; i ++){
    fact[i] = fact[i-1]*i % mod;

  }

  cin >> t;

  for (int i=0;i<t;i++){
    cout << "Case #" << i+1 << ": " << solve() << endl;
  }

  return 0;
}
