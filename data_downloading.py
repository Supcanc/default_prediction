import kagglehub

path = kagglehub.dataset_download(
    "alexdister/credit-risk-dataset",
    output_dir='dataset/'
)

print("Path to dataset files:", path)