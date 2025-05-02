import pulumi
import pulumi_gcp as gcp



# Create a GCS bucket
perigon_tableman_test_bucket = gcp.storage.Bucket(
    'perigon-tableman-test',
    name='perigon-tableman-test',
    location='us-central1',
    project='perigon-central-data-repo',
    uniform_bucket_level_access=True
)


# Export the DNS name of the bucket
#trivial
pulumi.export('bucket_url', bucket.url)

