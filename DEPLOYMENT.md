# Vercel Deployment Guide

## Important Notes

### Model File
The trained model file (`vegetable_classification.h5`) is too large for Git and Vercel's deployment limits. You have these options:

1. **Use External Storage (Recommended)**
   - Upload your model to cloud storage (AWS S3, Google Cloud Storage, etc.)
   - Download it at runtime using environment variables
   - Add download logic in `flask/app.py`

2. **Use Vercel Blob Storage**
   - Upload model to Vercel Blob
   - Reference it in your app

3. **Deploy Without Model (Demo Mode)**
   - The app will run but show "Model not loaded" message
   - Good for testing deployment pipeline

### Deployment Steps

1. Install Vercel CLI:
   ```bash
   npm i -g vercel
   ```

2. Login to Vercel:
   ```bash
   vercel login
   ```

3. Deploy from the project root:
   ```bash
   cd green-classify-deeplearning2026
   vercel
   ```

4. Follow the prompts to link your project

### Configuration Files Created

- `vercel.json` - Vercel configuration
- `api/index.py` - Entrypoint for Vercel
- `.vercelignore` - Files to exclude from deployment

### Important Considerations

- Vercel has a 250MB deployment size limit
- Serverless functions have execution time limits (10s for Hobby, 60s for Pro)
- Model inference might be slow on cold starts
- Consider using a smaller model or quantization for production
