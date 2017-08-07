#include<bits/stdc++.h>
using namespace std;

double calc_avg(vector<float >v);

double varience(vector<float >v);

int min_max_norm(vector<float> v);

int zscore_norm(vector<float>v);

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

	cout<<endl<<"..............................................."<<endl;
	cout<<"z-score normalization:"<<endl;
	zscore_norm(v);
	cout<<"..............................................."<<endl;
	cout<<"min-max normalization:"<<endl;
	min_max_norm(v);
	cout<<"..............................................."<<endl;
	return 0;
}

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
	double sum=0,mean_val;
	int i;
	mean_val=calc_avg(v);
	for(i=0;i<v.size();i++)
	{
		sum+=(mean_val-v[i])*(mean_val-v[i]);
	}
	sum/=(v.size()-1);
	return sqrt(sum);
}

int min_max_norm(vector<float>v)
{
	int mn,mx,i;
	cout<<"Range(Min-max values respectively):- ";
	cin>>mn>>mx;
	sort(v.begin(),v.end());
	vector< float>f;
		
	for(i=0;i<v.size();i++)
	{
		f.push_back(v[i]);
		f[i]=((float((v[i]-v[0])/(v[v.size()-1]-v[0])))*(mx-mn))+mn;
	}

	for(i=0;i<f.size();i++)
	{
		cout<<f[i]<<" ";
	}
	cout<<endl;
	return 0;
		
}

int zscore_norm(vector<float>v)
{
	
	double vari=varience(v),avg=calc_avg(v);
	vector<double> z;
	int i;
	for(i=0;i<v.size();i++)
	{
		z.push_back((v[i]-avg)/vari);
	}
	sort(z.begin(),z.end());
	for(i=0;i<z.size();i++)
	{
		cout<<z[i]<<" ";
	}
	cout<<endl;
	return 0;

}



