#include<bits/stdc++.h>
using namespace std;
int main()
{
	vector<int>v;
	int n,i,j,no_of_bins,bin_size;
	cout<<"enter size(no. of elements):"<<endl;
	cin>>n;
	cout<<"enter "<<n<<" elements:";
	for(i=0;i<n;i++)
	{
		int x;
		cin>>x;
		v.push_back(x);
	}	
	cout<<"no of bins:";
	cin>>no_of_bins;

	sort(v.begin(),v.end());

	bin_size=(n/no_of_bins);
	if(n%2!=0)
		bin_size+=1;


	vector<int>bins[no_of_bins];

	int bno=0;
	
	for(i=0;i<n;i++)
	{

		bins[bno].push_back(v[i]);
		if(((i+1)%bin_size)==0)
			bno++;

	}

	cout<<"Equi-width Binning:"<<endl;
	for(i=0;i<no_of_bins;i++)
	{
		cout<<"bin_no -"<<i+1<<" : ";
		for(j=0;j<bins[i].size();j++)
		{
			cout<<bins[i][j]<<" ";
		}
		cout<<endl;
	}

	cout<<"-----------------------------------------------------------------"<<endl;

	cout<<"Bin Mean:"<<endl;
	double mean=0;
	for(i=0;i<no_of_bins;i++)
	{
		cout<<"bin_no -"<<i+1<<" : ";
		mean=0;
		for(j=0;j<bins[i].size();j++)
		{
			mean+=bins[i][j];
		}
		mean/=bins[i].size();
		for(j=0;j<bins[i].size();j++)
		{
			cout<<mean<<" ";
		}
		cout<<endl;
	}


	cout<<"--------------------------------------------------------------------"<<endl;
	cout<<"Bin Boundaries :"<<endl;
	mean=0;
	for(i=0;i<no_of_bins;i++)
	{
		cout<<"bin_no -"<<i+1<<" : ";
		int var_min=bins[i][0],var_max=bins[i][bins[i].size()-1];
		
		for(j=0;j<bins[i].size();j++)
		{
			if(j!=0&&j!=bins[i].size()-1)
			{
				if(abs(bins[i][j]-var_min)<=abs(bins[i][j]-var_max))
					cout<<var_min<<" ";
				else
					cout<<var_max<<" ";
			}		
				
			else
				cout<<bins[i][j]<<" ";
		}
		
		cout<<endl;
	}

	cout<<"----------------------------------------------------------------------"<<endl;

	return 0;
		
}
