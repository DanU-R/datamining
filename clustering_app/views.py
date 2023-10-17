from django.shortcuts import render
from .forms import ClusterForm
from sklearn.cluster import KMeans
import pandas as pd
from .models import Customer

def customer_segmentation(request):
    forms = ClusterForm(request.POST or None)
    clusters = None

    if request.method == 'POST' and form.is_valid():
        # Ambil data pelanggan dari basis data
        customers = Customer.objects.all()

        # Ambil data yang akan digunakan untuk clustering (age dan income)
        data = pd.DataFrame(customers.values('id', 'username', 'email', 'age', 'income'))

        # Fitur-fitur yang digunakan untuk clustering
        features = ['age', 'income']

        # Ambil jumlah cluster dari formulir
        num_clusters = form.cleaned_data['clusters']

        # Lakukan K-Means Clustering
        kmeans = KMeans(n_clusters=num_clusters, random_state=0).fit(data[features])

        # Tambahkan kolom 'cluster' ke DataFrame
        data['cluster'] = kmeans.labels_

        # Hitung nilai rata-rata dalam setiap cluster
        clusters = data.groupby('cluster').mean()

    return render(request, 'clustering_app/segmentation.html', {'form': form, 'clusters': clusters})
