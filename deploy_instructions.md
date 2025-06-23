# Deploy Instructions

## Deploying the Landing Page

This project is a static landing page (HTML/CSS/JS) and can be deployed on any static hosting provider (GitHub Pages, Vercel, Netlify, etc.) or served locally.

### 1. Deploy to GitHub Pages
- Go to your repository settings on GitHub
- Under "Pages", select the `main` branch and `/ (root)` folder
- Save and wait for the deployment URL (e.g., `https://bluma05.github.io/llm-function-calling-system-prompts-paper/`)

### 2. Deploy to Vercel
- Go to [Vercel](https://vercel.com/)
- Import the repository from GitHub
- Vercel will auto-detect and deploy the static site
- Access via the generated Vercel URL

### 3. Deploy to Netlify
- Go to [Netlify](https://netlify.com/)
- Connect your GitHub repository
- Set the publish directory to `/`
- Deploy and access via the Netlify URL

### 4. Serve Locally
- Open a terminal in the project directory
- Run: `python -m http.server 8080`
- Access: [http://localhost:8080](http://localhost:8080)

## After Deploy
- The landing page will be available at the chosen URL
- All features (navigation, copy code, etc.) work out-of-the-box

## Notes
- No build step required
- For custom domains, configure DNS with your provider
- For CI/CD, see `.github/workflows/ci.yml`
