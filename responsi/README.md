RESPONSI 

# Import package pandas dulu untuk mengambil datanya 
```python
import pandas as pd
import numpy as pd
```

# untuk menampilkan data insurancenya 

```python
data_olah = 'insurance.csv'
dataset = pd.read_csv(data_olah)
dataset.head(20)

	age	sex	bmi	children	smoker	region	charges
0	19	female	27.900	0	yes	southwest	16884.92400
1	18	male	33.770	1	no	southeast	1725.55230
2	28	male	33.000	3	no	southeast	4449.46200
3	33	male	22.705	0	no	northwest	21984.47061
4	32	male	28.880	0	no	northwest	3866.85520
5	31	female	25.740	0	no	southeast	3756.62160
6	46	female	33.440	1	no	southeast	8240.58960
7	37	female	27.740	3	no	northwest	7281.50560
8	37	male	29.830	2	no	northeast	6406.41070
9	60	female	25.840	0	no	northwest	28923.13692
10	25	male	26.220	0	no	northeast	2721.32080
11	62	female	26.290	0	yes	southeast	27808.72510
12	23	male	34.400	0	no	southwest	1826.84300
13	56	female	39.820	0	no	southeast	11090.71780
14	27	male	42.130	0	yes	southeast	39611.75770
15	19	male	24.600	1	no	southwest	1837.23700
16	52	female	30.780	1	no	northeast	10797.33620
17	23	male	23.845	0	no	northeast	2395.17155
18	56	male	40.300	0	no	southwest	10602.38500
19	30	male	35.300	0	yes	southwest	36837.46700
```

# menampilkan bagian data pada kolom sex, bmi serta children 

```python
dataset.isnull().sum()

age         0
sex         0
bmi         0
children    0
smoker      0
region      0
charges     0
dtype: int64
```

# menampilkan 5 data awal 

```python
print(dataset.head(5))

   age     sex     bmi  children smoker     region      charges
0   19  female  27.900         0    yes  southwest  16884.92400
1   18    male  33.770         1     no  southeast   1725.55230
2   28    male  33.000         3     no  southeast   4449.46200
3   33    male  22.705         0     no  northwest  21984.47061
4   32    male  28.880         0     no  northwest   3866.85520
```

# menampilkan data dari kolom 1 sampai 3

```python
data = dataset.iloc[:,1:4]
data

	sex	bmi	children
0	female	27.900	0
1	male	33.770	1
2	male	33.000	3
3	male	22.705	0
4	male	28.880	0
...	...	...	...
1333	male	30.970	3
1334	female	31.920	0
1335	female	36.850	0
1336	female	25.800	0
1337	female	29.070	0
1338 rows × 3 columns
```