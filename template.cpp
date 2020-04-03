#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <climits>
#include <cstring>
#include <utility>
#include <cmath>
using namespace std;

#define IOS ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);

#define F first
#define S second 
#define pb push_back
#define all(x) x.begin(),x.end()
#define endl "\n"


void print() { cout << endl; }

template <typename T, typename... Types>
void print(T arg, Types... args) {
    cout << arg << " ";
    print(args...);
}

typedef long long ll;
typedef long double ld;
typedef pair< int, int > pii;
typedef vector < int > vi;

const int mod = 1e9 + 7;
const int N = 2e5 + 7;


ll gcdExtended(ll a, ll b, ll *x, ll *y){
    if (a == 0){
        *x = 0, *y = 1;
        return b;
    }
    ll x1, y1;
    ll gcd = gcdExtended(b%a, a, &x1, &y1);
    *x = y1 - (b/a) * x1;
    *y = x1;
    return gcd;
}

ll modInv(ll a, ll m){
    ll x, y;
    ll g = gcdExtended(a, m, &x, &y);
    ll res = (x%m + m) % m;
    return res;
}
 
 
ll mpower(ll x, ll y, ll p){
    ll res = 1;
    x = x % p;
    while(y > 0){
        if(y & 1) res = (res*x) % p;
        y = y>>1;
        x = (x*x) % p;
    }
    return res;
}
 
ll power(ll x, ll y){
    ll res = 1;
    while (y > 0){
        if (y & 1) res = res*x;
        y = y>>1;
        x = x*x;
    }
    return res;
}
 
bool isPrime(ll n){
    if (n <= 1)  return false;
    if (n <= 3)  return true;
    if (n%2 == 0 || n%3 == 0) return false;
    ll p=sqrt(n);
    for(int i=5;i<=p;i=i+6)
        if (n%i == 0 || n%(i+2) == 0)
            return false;
    return true;
}



int main()
{
    IOS;
    int tc = 1, n;
    cin >> tc;
    while (tc--)
    {
    	
    }
    return 0;
}
