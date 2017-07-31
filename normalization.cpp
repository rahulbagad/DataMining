#include<bits/stdc++.h>
using namespace std;
double calc_avg(vector<float >v)
{
	double avg=0;
	int i;
	for(i=0;i<v.size();i++)
	{
		avg+=v[i];

	}
	avg/=v.size();
	return avg;
}

double varience(vector<float >v)
{
	double sum=0,mean_var,i;
	mean_var=calc_avg(v);
	for(i=0;i<v.size();i++)
	{
		sum+=(mean_var-v[i])*(mean_var-v[i]);
	}
	sum/=v.size()-1;
	return sum;
}
int min_max_norm(vector<float> v)
{
	int mn,mx,i;
	cout<<"Min max respectively: ";
	cin>>mn>>mx;
	sort(v.begin(),v.end());
	vector< float>f;
		
	for(i=0;i<v.size();i++)
	{
		f.push_back(v[i]);
	}
	for(i=0;i<v.size();i++)
	{
		f[i]=((float((v[i]-v[0])/(v[v.size()-1]-v[0])))*(mx-mn))+mn;
	}
	for(i=0;i<v.size();i++)
	{
		cout<<f[i]<<" ";
	}
	cout<<endl;
	return 0;
		
}

int zscore_norm(vector<float>v)
{
	
	double vari=varience(v),avg=calc_avg(v);
	int i;
	for(i=0;i<v.size();i++)
	{
		v[i]=(v[i]-avg)/vari;
	}
	for(i=0;i<v.size();i++)
	{
		cout<<v[i]<<" ";
	}
	cout<<endl;
	return 0;

}


int main()
{
	vector<float>v;
	int len,i;
	cout<<"no. of elements:";
	cin>>len;
	cout<<"Enter elements:";
	for(i=0;i<len;i++)
	{
		int x;
		cin>>x;
		v.push_back(x);
	}
	cout<<"min max normalization:"<<" ";
	min_max_norm(v);
	cout<<" z score normalization: "<<" ";
	zscore_norm(v);
	return 0;
}

