# Quick Vercel Deployment

## Files Created
- ✅ `vercel.json` - Vercel configuration
- ✅ `api/index.py` - Flask entrypoint for Vercel
- ✅ `.vercelignore` - Excludes large files from deployment

## Deploy Now

```bash
cd green-classify-deeplearning2026
vercel
```

## What Was Fixed
The error occurred because Vercel couldn't find the Flask app at the root level. The app was in `flask/app.py`, but Vercel expects it in standard locations like `api/index.py`.

Solution: Created `api/index.py` that imports your Flask app from the `flask/` directory.

## Note About Model File
Your model file (`vegetable_classification.h5`) is gitignored and won't be deployed. The app will run but show "Model not loaded" until you:
- Upload the model to cloud storage and download it at runtime, OR
- Use Vercel Blob storage, OR
- Deploy without the model for testing purposes

See `DEPLOYMENT.md` for detailed options.
