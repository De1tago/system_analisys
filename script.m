
data = importdata('dates/isi.txt');
data_subset = data(3:end);
cwt(data_subset, 'amor')
