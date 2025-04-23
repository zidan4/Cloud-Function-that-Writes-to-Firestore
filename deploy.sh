gcloud functions deploy add_user \
  --runtime python311 \
  --trigger-http \
  --allow-unauthenticated \
  --entry-point add_user \
  --source .
